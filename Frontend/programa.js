//Frontend mínimo
let url="http://127.0.0.1:8000/sumar"

let myAPI= url + "?a=5&b=45";

async function crearPetición() {
    let response = await fetch(myAPI);
    let datos = response.json();
}