function listenAllTracks(tracks){
    var i;
    for (i = 0; i < tracks.length; i++) {
        var aux = "trackSound" + tracks[i].toString();
        var audio = document.getElementById(aux);
        audio.play();
    }


    // for(t in tracks){
    //     var aux = "trackSound" + t.toString();
    //     var audio = document.getElementById(aux);
    //     audio.play();
    // }
    // var n = 11;
    // var aux = "trackSound" + n.toString();
    // var audio = document.getElementById(aux);
    // audio.play();
}