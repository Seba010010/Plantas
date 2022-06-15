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
         //const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${AQUI_VIENE_TU_API_KEY}`

         //ubicación por ciudad
         const url = 'https://api.openweathermap.org/data/2.5/weather?q=Santiago&units=metric&lang=es&APPID=d92580f775301ffa57fa15570bc4dd69'

         //console.log(url)

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
              
              //para iconos estáticos
              //const urlIcon = `http://openweathermap.org/img/wn/${iconCode}.png`                     
              //icono.src = urlIcon
              //console.log(data.weather[0].icon)

              //para iconos dinámicos
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
