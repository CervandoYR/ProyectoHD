
    // Ocultar mensajes de error tras 5 segundos
    document.addEventListener("DOMContentLoaded", function() {
        setTimeout(function() {
            const errorMessages = document.querySelectorAll('.error-message');
            errorMessages.forEach(function(msg) {
                msg.style.display = 'none';
            });
        }, 3000); // 3 segundos
    });

