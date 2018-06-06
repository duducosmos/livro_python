#!/usr/bin/env python
# -*- Coding: UTF-8 -*-

'''
Módulo tools com funcoes auxiliares para o fplayer.
'''

from flask import url_for
import glob

from mutagen import File
from model import model

MUSICFOLDER = 'static/musics/'

def updatemusic():
    db = model()
    musiclist = glob.glob(MUSICFOLDER + "*.mp3")
    musicnames = [mi.split("/")[-1] for mi in musiclist]

    indb = [msi.arquivo for msi in db().iterselect(db.musica.arquivo)
            if msi.arquivo in musicnames]
    notindb = list(set(musicnames) - set(indb))

    for msi in notindb:
        tag = File(MUSICFOLDER + msi)
        if('TIT2' in tag.keys()):
            db.musica.insert(nome=tag['TIT2'].text[0],
                             cantor=tag['TPE1'].text[0],
                             arquivo=msi,
                             tempo=sec2minString(
                File(MUSICFOLDER + msi).info.length)
            )
        else:
            db.musica.insert(arquivo=msi,
                             tempo=sec2minString(
                                 File(MUSICFOLDER + msi).info.length)
                             )

    notindir = [msi.arquivo for msi in db().iterselect(db.musica.arquivo)
                if msi.arquivo not in musicnames]

    for msi in notindir:
        db(db.musica.arquivo == msi).delete()
    db.commit()


def get_musics():
    db = model()
    musiclist = db().select(db.musica.arquivo,
                            db.musica.tempo,
                            db.musica.cantor,
                            db.musica.nome,
                            orderby=~db.musica.arquivo | db.musica.nome
                            )
    if len(musiclist) > 0:

        musicJ = [{"fileName": mi.arquivo,
                   "coverURL": url_for('coverImage',
                                       music=MUSICFOLDER + mi.arquivo),
                   'fileUrl': url_for('sounds',

                                      music=MUSICFOLDER + mi.arquivo),
                   'length': mi.tempo,
                   'Tags': None
                   } for mi in musiclist]

        for i in range(len(musicJ)):
            if musiclist[i].cantor is not None:
                musicJ[i]['Tags'] = {
                    'TIT2': musiclist[i].nome, 'TPE1': musiclist[i].cantor}
    else:
        musicJ = []
    return musicJ


def sec2minString(sec):
    mi = sec / 60.0
    mi = str(mi).split(".")
    seci = int(float('0.' + mi[1]) * 60.0)
    if(seci < 10):
        seci = '0' + str(seci)
    else:
        seci = str(seci)

    return mi[0] + ":" + seci