from flask import Flask, render_template, request, redirect, url_for
from farmacia import Farmacia, Cliente
'''
Importamos Flask para manejar las rutas y las solicitudes HTTP,
además importamos las clases `Farmacia` y `Cliente` desde el archivo 
`farmacia.py`, que contienen la lógica de negocio.
'''

app = Flask(__name__)  # Inicializamos la aplicación Flask
farmacia = Farmacia()  # Creamos una instancia de la clase `Farmacia`
'''
Creamos la instancia de la aplicación Flask y la llamamos `app`.
También inicializamos una instancia de la clase `Farmacia` para gestionar
toda la lógica de la farmacia.
'''

@app.route('/')
def index():
    turnos = farmacia.mostrar_turnos()  # Obtenemos los turnos actuales
    entregas = farmacia.mostrar_entregas()  # Obtenemos las entregas actuales
    return render_template('index.html', turns=turnos, deliveries=entregas)
'''
Ruta principal que renderiza la página de inicio ('/').

- Se obtienen los turnos actuales mediante el método `mostrar_turnos()`
  de la instancia `farmacia`.
- También se obtienen las entregas realizadas con `mostrar_entregas()`.
- Finalmente, se renderiza la plantilla HTML `index.html`, pasando los turnos
  y entregas como contexto para ser mostrados en la página.
'''

@app.route('/assign_turn', methods=['POST'])
def assign_turn():
    nombre = request.form.get('customer_name')  # Obtiene el nombre del formulario
    cedula = request.form.get('customer_id')  # Obtiene la cédula del formulario
    cliente = Cliente(nombre, cedula)  # Crea una instancia de Cliente
    farmacia.asignar_turno(cliente)  # Asigna un turno al cliente
    return redirect(url_for('index'))
'''
Ruta para asignar turnos a los clientes.

- Recibe una solicitud POST desde un formulario, donde obtiene el `nombre`
  y la `cédula` del cliente.
- Crea un nuevo objeto `Cliente` con esos datos.
- Llama al método `asignar_turno()` de la clase `Farmacia` para asignar un
  turno al cliente y añadirlo a la cola.
- Luego redirige de nuevo a la página principal (`index`) usando `redirect()`.
'''

@app.route('/deliver_medications', methods=['POST'])
def deliver_medications():
    numero_turno = int(request.form.get('turn_number'))  # Obtiene el número de turno
    medicamentos = request.form.getlist('medications')  # Obtiene la lista de medicamentos
    farmacia.entregar_medicamentos(numero_turno, medicamentos)  # Entrega los medicamentos al cliente correspondiente
    return redirect(url_for('index'))
'''
Ruta para entregar medicamentos a un cliente.

- Recibe una solicitud POST desde un formulario que contiene el `numero_turno`
  y una lista de `medicamentos` (obtenida con `getlist()`).
- Llama al método `entregar_medicamentos()` de la clase `Farmacia`, pasando
  el número de turno y los medicamentos.
- Luego redirige de nuevo a la página principal (`index`) usando `redirect()`.
'''

if __name__ == '__main__':
    app.run(debug=True)
'''
Inicia la aplicación Flask en modo de depuración (`debug=True`), lo que significa que
la aplicación se reinicia automáticamente si se detectan cambios en el código. Esto es útil
durante el desarrollo.
'''
