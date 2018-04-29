// Lista de Objetos contendo as informações necessárias para criar a playList
var musicList = [{
        name: "Mazurka em C",
        file: "sounds/2830_mazurka-in-c-major.mp3",
        id: "m0"
    },
    {
        name: "Allegetto em F#",
        file: "sounds/2853_allegretto-in-f-sharp-major.mp3",
        id: "m1"
    },
    {
        name: "Andantio \"Spring\" em  B",
        file: "sounds/Andantino_Spring_B.mp3",
        id: "m2"
    }
];

// Representa a tabela presente no HTML com a lista de músicas;
var playTable;

//Representa o tocador de música dado pela tag audio;
var audioPlayer;

//Representa o atributo source da tag audio, o qual iremos trocar dinamicamente
// para trocar o arquivo que está sendo executado
var sourceAudio;

function setElements(pTable, aPlayer, sAudio) {
    /*
    Função de inicialização das variáveis auxiliares globias
    e que inicializa a tabela de músicas no HTML
    */
    playTable = document.getElementById(pTable);
    audioPlayer = document.getElementById(aPlayer);
    sourceAudio = document.getElementById(sAudio);
    playList();
}

function playList(){
    /*
    Função que cria uma tabela contendo as músicas a serem executadas.
    */
    var table = document.createElement('table');
    for(var i = 0; i < musicList.length; i++){
        var tr = document.createElement("tr");
        var td = document.createElement("td");
        var a = document.createElement("a");
        a.id = musicList[i].id;
        a.setAttribute("onclick", "loadMusic(\'" + musicList[i].file + "\');");
        a.innerHTML = musicList[i].name;
        a.style="color:blue;"
        td.appendChild(a);
        tr.appendChild(td);
        table.appendChild(tr);
    }
    playTable.appendChild(table);
}

function loadMusic(source){
    /*
    Modifica o arquivo fonte e inicia a execução desse novo arquivo.
    */
    //alert(source);
    sourceAudio.src = source;
    audioPlayer.load();
    audioPlayer.play();
}
