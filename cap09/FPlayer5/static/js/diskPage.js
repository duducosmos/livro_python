var current = 0;

var playing = false;

var mysound;
var source;
var progressBar;
var onProgChange = false;
var musics;

function set_ListOfMusics(mlist) {
    musics = mlist;
}

function startMusic() {
    mysound = document.getElementById('myplay');
    soundImg = document.getElementById('coverImg');
    progressBar = document.getElementById("rangeProgr");

    source = document.getElementById('audioSource');
    source.src = musics[0].fileUrl;
    soundImg.src = musics[0].coverURL;
    mysound.load();
    mysound.play();
    changeColorMusic();
    changeArtistTitle();
    playing = true;
    mysound.addEventListener("ended", function() {
        if (current < musics.length - 1) {
            current += 1;

            source.src = musics[current].fileUrl;
            document.getElementById('coverImg').src = musics[current].coverURL;
            mysound.load();
            mysound.play();
        }
        changeColorMusic();
        changeArtistTitle();

        if(current == musics.length - 1){
            var mylink = document.getElementById("lim_" + current.toString())
            mylink.style.color = "blue";
        }

        updateTime();

    });

    mysound.addEventListener("timeupdate", function() {
        var currentTime = mysound.currentTime;
        var duration = mysound.duration;
        var per = (currentTime / duration) * 100;
        if (onProgChange == false) {
            progressBar.value = per;
            updateTime();
        }

    });


    progressBar.addEventListener('mouseup', function() {
        var newTime = this.value * mysound.duration / 100;
        mysound.currentTime = newTime;
        onProgChange = false;
        updateTime();

    });

    progressBar.addEventListener('mousedown', function() {
        onProgChange = true;

    });

    progressBar.addEventListener('touchend', function() {
        var newTime = this.value * mysound.duration / 100;
        mysound.currentTime = newTime;
        onProgChange = false;
        updateTime();

    });

    progressBar.addEventListener('touchstart', function() {
        onProgChange = true;

    });


}

function changeMusic(newSound) {

    current = musics.map(function(d) {
        return d['fileUrl'];
    }).indexOf(newSound);
    changeColorMusic();
    changeArtistTitle();


    source.src = newSound;
    document.getElementById('coverImg').src = musics[current].coverURL;
    mysound.load();
    mysound.play();
    updateTime();

}

function changeArtistTitle(){
    var artist = document.getElementById("artista");
    var titulo = document.getElementById("titulo");
    if(musics[current].Tags != null){
        artist.innerHTML = musics[current].Tags.TPE1;
        titulo.innerHTML = musics[current].Tags.TIT2;
    }else{
        artist.innerHTML = " unknown ";
        titulo.innerHTML = musics[current].fileName;
    }
}


function changeColorMusic(){
    var mylink;

    for(i=0; i < musics.length; i++){
        mylink = document.getElementById("lim_" + i.toString());
        if(i == current){
            mylink.style.color = "red";
        }else{
            mylink.style.color = "blue";
        }
    }
}


function onPlay() {
    if (playing == false) {
        document.getElementById('myplay').play();
        playing = true;
        document.getElementById("playbutton").innerHTML = 'play_arrow';

    } else {
        document.getElementById('myplay').pause();
        playing = false;
        document.getElementById("playbutton").innerHTML = 'pause';
    }
    updateTime();

}

function skip_next() {
    if (current == musics.length - 1) {
        current = 0;
        source.src = musics[current].fileUrl;
        document.getElementById('coverImg').src = musics[current].coverURL;
        mysound.load();
        mysound.play();
    } else {
        current += 1;
        source.src = musics[current].fileUrl;
        document.getElementById('coverImg').src = musics[current].coverURL;
        mysound.load();
        mysound.play();
    }
    changeColorMusic();
    changeArtistTitle();
    updateTime();
}

function skip_previous() {
    if (current == 0) {
        current = 0;
        source.src = musics[current].fileUrl;
        document.getElementById('coverImg').src = musics[current].coverURL;
        mysound.load();
        mysound.play();
    } else {
        current -= 1;
        source.src = musics[current].fileUrl;
        document.getElementById('coverImg').src = musics[current].coverURL;
        mysound.load();
        mysound.play();
    }
    changeColorMusic();
    changeArtistTitle();
    updateTime();
}


function updateTime() {
    document.getElementById("ctime").innerHTML = sec2minString(mysound.currentTime);
    document.getElementById("totalTime").innerHTML = sec2minString(mysound.duration);
}

function sec2minString(mytime) {
    var minutes = Number(mytime) / 60;
    var tmp = minutes.toString().split('.');
    minutes = tmp[0];
    seconds = "0." + tmp[1];
    seconds = Math.round(Number(seconds) * 60);
    if (seconds < 10) {
        seconds = '0' + seconds.toString();
    } else {
        seconds = seconds.toString();
    }
    return minutes + ":" + seconds;


}