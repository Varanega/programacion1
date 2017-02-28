r# Ajax
![ajax](img/ajax.gif)

## GET
```javascript
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
	document.querySelector('#resultado').innerHTML = this.responseText;
}
};
xhttp.open('GET', 'dominio.com', true);
xhttp.send();
```

## POST
```javascript
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
if (this.readyState == 4 && this.status == 200) {
	document.querySelector('#resultado').innerHTML = this.responseText;
}
};
info = "fecha_nacimiento=" + encodeURIComponent(fecha.value) +
         "&codigo_postal=" + encodeURIComponent(cp.value) +
         "&telefono=" + encodeURIComponent(telefono.value) +
         "&nocache=" + Math.random();

xhttp.open('POST', '/datos', true);
xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhttp.send(info);
```

## JSON

### Python
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    list = [
        {'param': 'foo', 'val': 2},
        {'param': 'bar', 'val': 10}
    ]
    return jsonify(list)

if __name__ == '__main__':
    app.run()
```
### Javascript
```javascript
aJSON = JSON.parse(xhttp.responseText);
let nombre_jefe = 'Nombre de Jefe: ' + aJSON.responsable.nombre;
```
