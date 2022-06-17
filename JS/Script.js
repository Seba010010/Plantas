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

function validarFormSub(){
    let emailSubInput  = document.getElementById("emailSub");
    let emailSub = emailSubInput.value;

    if(!emailSub){
      alert(`El campo email no puede estar vacio`);
    }

}

function validarFormLogin(){
  let nombreInput = document.getElementById("nombreUsuario");
  let passInput   = document.getElementById("usuarioPass");

  console.log(nombreInput.value);

  let nombre = nombreInput.value;
  let pass   = passInput.value;

  if(!nombre){
    alert("El nombre no puede estar vacio")
  }

  if(!pass){
    alert("La contraseña no puede estar vacia")
  }

}

function validarFormRegistro(){

  
  let nombreInput   = document.getElementById("nombres");
  let apellidoInput = document.getElementById("apellidos");
  let correoInput   = document.getElementById("correo");
  let passwordInput = document.getElementById("password");

  let nombre = nombreInput.value;
  let apellido = apellidoInput.value;
  let correo = correoInput.value;
  let password = passwordInput.value;

  console.log(`${nombre} ${apellido} ${correo} ${password}`)


  if(!nombre){
    alert("El nombre no puede estar vacio")
  }
  
  if(!apellido){
    alert("El apellido no puede estar vacio")
  }

  if(!correo){
    alert("El correo  no puede estar vacio")
  }

  if(!password){
    alert("La contraseña no puede estar vacia")
  }


}
//:::::::::::::::Consumo de API Openweathermap::::::::::::::://

window.addEventListener('load', ()=> {
  let lon
  let lat

  let temperaturaValor = document.getElementById('temperatura-valor')  
  let temperaturaDescripcion = document.getElementById('temperatura-descripcion')  
  
  let ubicacion = document.getElementById('ubicacion')  
  let iconoAnimado = document.getElementById('icono-animado') 

  let vientoVelocidad = document.getElementById('viento-velocidad') 


  if(navigator.geolocation){
     navigator.geolocation.getCurrentPosition( posicion => {
         //console.log(posicion.coords.latitude)
         lon = posicion.coords.longitude
         lat = posicion.coords.latitude
          //ubicación actual    
         //const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=$d92580f775301ffa57fa15570bc4dd69`

         //ubicación por ciudad
         const url = 'https://api.openweathermap.org/data/2.5/weather?q=Santiago&APPID=d92580f775301ffa57fa15570bc4dd69'

         fetch(url)
          .then( response => { return response.json()})
          .then( data => {
              //console.log(data)
              
              let temp = Math.round(data.main.temp)
              //console.log(temp)
              temperaturaValor.textContent = `${temp} ° C`

              //console.log(data.weather[0].description)
              let desc = data.weather[0].description
              temperaturaDescripcion.textContent = desc.toUpperCase()
              ubicacion.textContent = data.name
              
              vientoVelocidad.textContent = `${data.wind.speed} m/s`
              
              //iconos dinámicos
              console.log(data.weather[0].main)
              switch (data.weather[0].main) {
                  case 'Thunderstorm':
                    iconoAnimado.src='img/thunder.svg'
                    console.log('TORMENTA');
                    break;
                  case 'Drizzle':
                    iconoAnimado.src='img/rainy-2.svg'
                    console.log('LLOVIZNA');
                    break;
                  case 'Rain':
                    iconoAnimado.src='img/rainy-7.svg'
                    console.log('LLUVIA');
                    break;
                  case 'Snow':
                    iconoAnimado.src='img/snowy-6.svg'
                      console.log('NIEVE');
                    break;                        
                  case 'Clear':
                      iconoAnimado.src='img/day.svg'
                      console.log('LIMPIO');
                    break;
                  case 'Atmosphere':
                    iconoAnimado.src='img/weather.svg'
                      console.log('ATMOSFERA');
                      break;  
                  case 'Clouds':
                      iconoAnimado.src='img/cloudy-day-1.svg'
                      console.log('NUBES');
                      break;  
                  default:
                    iconoAnimado.src='img/cloudy-day-1.svg'
                    console.log('por defecto');
                }

          })
          .catch( error => {
              console.log(error)
          })
     })
        
  }
})
