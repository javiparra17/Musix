function init() {
    var inputFile = document.getElementById('id_photo');
    inputFile.addEventListener('change', showImagen, false);
}

function showImagen(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(event) {
        var img = document.getElementById('output');
        img.src= event.target.result;
    };
    reader.readAsDataURL(file);
}

window.addEventListener('load', init, false);