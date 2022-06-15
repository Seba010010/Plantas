function validarFormContacto(){
    
    let nombreInput = document.getElementById("nombreContacto");
    let emailInput  = document.getElementById("emailContacto");
    let mensajeContactoInput = document.getElementById("mensajeContacto");

    let nombre = nombreInput.value;
    let email = emailInput.value;
    let mensaje = mensajeContactoInput.value;

    if(!nombre){
        alert(`El campo nombre no puede estar vacio`);    
    }
    if(!email){
        alert(`El campo email no puede estar vacio`);
    }
    if(!mensaje){
        alert("El campo mensaje no puede estar vacio")
    }
}