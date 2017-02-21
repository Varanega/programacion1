# Arrays

```javascript

// Vectores (array de una dimensión)
var semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'];

var meses = [];
meses[0] = 'Enero';
meses[1] = 'Febrero';

// Leer
console.log(meses[1]);

// Longitud
console.log(meses.length);

// Añadir
meses.push('Marzo');

// Eliminar un elemento -> Quito Marzo
aDias.splice(2, 1);

// Matrices (array de dos dimensiones)
let agenda = [][];
agenda[2017] = ['Enero', 'Febrero', 'Marzo'];
agenda[2018] = ['Enero', 'Febrero', 'Marzo'];
agenda[2019] = ['Enero', 'Febrero', 'Marzo'];

// Modificar
agenda[2017]['Febrero'] = 'Hablar con Manolin';

// Añadir
agenda[2020].push(['Enero', 'Febrero', 'Marzo']);

// Set (Conjuntos)
let setPelis = new Set(); // No permite repeticiones
setPelis.add('Lo que el viento se llevó')
setPelis.add('Lo que el viento se llevó')
setPelis.add('La gran evasion')

console.log('SET: Tiene la Gran evasion? ' + setPelis.has('La gran evasion'))
console.log('SET: ' + setPelis.size)

// Maps
let mapPrecios = new Map();
mapPrecios.set("Martini", 12);
mapPrecios.set(setPelis, 34);
console.log('MAPS: Precio de Martini ' + mapPrecios.get('Martini'))

// Weak Maps
var wm = new WeakMap();
wm.set(setPelis, { extra: 42 });
wm.size === undefined

// Weak Sets
var ws = new WeakSet();
ws.add({ data: 42 });


```
