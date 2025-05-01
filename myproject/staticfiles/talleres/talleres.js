function mostrarHorarios() {
    var taller = document.getElementById('taller').value;
    var horarios = document.getElementById('horarios');
    horarios.innerHTML = ''; 

    var opcionesHorarios = {
        "ajedrez": [
            { dia: "Lunes", hora: "10:00 AM - 12:00 PM" },
            { dia: "Miércoles", hora: "2:00 PM - 4:00 PM" }
        ],
        "teatro": [
            { dia: "Martes", hora: "9:00 AM - 11:00 AM" },
            { dia: "Jueves", hora: "3:00 PM - 5:00 PM" }
        ],
        "oratoria": [
            { dia: "Viernes", hora: "10:00 AM - 12:00 PM" },
            { dia: "Sábado", hora: "11:00 AM - 1:00 PM" }
        ],
        "danza": [
            { dia: "Lunes", hora: "5:00 PM - 7:00 PM" },
            { dia: "Viernes", hora: "6:00 PM - 8:00 PM" }
        ]
    };

    if (taller && opcionesHorarios[taller]) {
        opcionesHorarios[taller].forEach(function(horario) {
            var option = document.createElement('option');
            option.value = horario.dia + ' ' + horario.hora;
            option.text = horario.dia + ' - ' + horario.hora;
            horarios.appendChild(option);
        });
    }
}