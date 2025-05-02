/*document.addEventListener('DOMContentLoaded', function() {
    var myModal = new bootstrap.Modal(document.getElementById('inicioModal'));
    myModal.show();
});*/



function mostrarContenido(seccion) {
 
    var secciones = document.querySelectorAll('main div[id]');
    secciones.forEach(function (sec) {
        sec.style.display = 'none';
    });

    var seccionAMostrar = document.getElementById(seccion);
    if (seccionAMostrar) {
        seccionAMostrar.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    mostrarContenido('inicio'); 
});

