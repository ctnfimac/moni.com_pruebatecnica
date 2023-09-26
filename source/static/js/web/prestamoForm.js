window.onload = function () {
    const registroForm = document.getElementById('prestamo__formulario')
    const mensajePrestamo = document.getElementById('prestamo_mensaje')

    registroForm.addEventListener('submit', (event) => {
        event.preventDefault()

        fetch(registroForm.action,{
            method: 'POST',
            body: new FormData(registroForm),
            headers:{
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': registroForm.elements.csrfmiddlewaretoken.value,
            }
        })
        .then( response => response.json())
        .then( data => {
            
            if(data.errors){
                if(data.errors.monto){
                    mensajePrestamo.innerHTML = data.errors.monto[0];
                    mensajePrestamo.style.display = 'block';
                    mensajePrestamo.style.backgroundColor = '#e74c3c';
                    limpiaMensajeDeError()
                    
                }else{
                    mensajePrestamo.innerHTML = 'Error en su solicitud, intente luego';
                    mensajePrestamo.style.display = 'block';
                    mensajePrestamo.style.backgroundColor = '#e74c3c';
                    limpiaMensajeDeError()
                }               
            }else{
                mensajePrestamo.innerHTML = data.msg;
                mensajePrestamo.style.display = 'block';
                mensajePrestamo.style.backgroundColor = '#1abc9c';
                limpiaFormulario()
            }
        
        })
        .catch( error => {
            mensajePrestamo.innerHTML = 'Error en el sistema, intente luego';
            mensajePrestamo.style.display = 'block';
            mensajePrestamo.style.backgroundColor = '#e74c3c';
            limpiaMensajeDeError()
        })


    })

    function limpiaFormulario(){
        setTimeout(function(){
            registroForm.reset();
            mensajePrestamo.style.display = 'none';
        }, 5000);
    }

    function limpiaMensajeDeError(){
        setTimeout(function(){
            mensajePrestamo.style.display = 'none';
        }, 5000);
    }

}