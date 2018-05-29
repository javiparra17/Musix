function playAllTracks(tracks){
    var i;
    for (i = 0; i < tracks.length; i++) {
        var aux = "trackSound" + tracks[i].toString();
        var audio = document.getElementById(aux);
        audio.play();
    }

    var playButton = document.getElementById("playButton");
    playButton.disabled = true;
    playButton.className = "btn-default";

    var pauseButton = document.getElementById("pauseButton");
    pauseButton.disabled = false;
    pauseButton.className = "btn-warning";

    var stopButton = document.getElementById("stopButton");
    stopButton.disabled = false;
    stopButton.className = "btn-danger";
}

function pauseAllTracks(tracks){
    var i;
    for (i = 0; i < tracks.length; i++) {
        var aux = "trackSound" + tracks[i].toString();
        var audio = document.getElementById(aux);
        audio.pause();
    }

    var playButton = document.getElementById("playButton");
    playButton.disabled = false;
    playButton.className = "btn-success";

    var pauseButton = document.getElementById("pauseButton");
    pauseButton.disabled = true;
    pauseButton.className = "btn-default";

    var stopButton = document.getElementById("stopButton");
    stopButton.disabled = false;
    stopButton.className = "btn-danger";
}

function stopAllTracks(tracks){
    var i;
    for (i = 0; i < tracks.length; i++) {
        var aux = "trackSound" + tracks[i].toString();
        var audio = document.getElementById(aux);
        audio.pause();
        audio.currentTime = 0;
    }

    var playButton = document.getElementById("playButton");
    playButton.disabled = false;
    playButton.className = "btn-success";

    var pauseButton = document.getElementById("pauseButton");
    pauseButton.disabled = true;
    pauseButton.className = "btn-default";

    var stopButton = document.getElementById("stopButton");
    stopButton.disabled = true;
    stopButton.className = "btn-default";
}