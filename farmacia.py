from collections import deque
'''
Usamos deque que es una clase del módulo collections
en Python que proporciona una implementación eficiente 
de una cola de doble extremo, ideal para agregar o quitar 
elementos de ambos lados.
'''
class Cliente:
    def __init__(self, nombre, cedula, numero_turno=None):
        self.nombre = nombre
        self.cedula = cedula
        self.numero_turno = numero_turno
        self.medicamentos = []  # Lista que actúa como pila para los medicamentos
    '''
    Constructor de la clase Cliente que inicializa los datos del cliente 
    (nombre, cédula y su turno). Además, se inicializa una lista vacía 
    que actuará como pila para almacenar los medicamentos del cliente.
    '''

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)  # Agrega un medicamento al final de la lista (pila)
    '''
    Método que permite agregar un medicamento al cliente, 
    agregando el medicamento al final de la lista de medicamentos.
    '''

    def deshacer_medicamento(self):
        if self.medicamentos:
            return self.medicamentos.pop()  # Usamos pop() para eliminar el último medicamento de la lista
        return None  # Si no hay medicamentos, retornamos None
    '''
    Método para deshacer el último medicamento agregado. Usamos pop() para
    remover el último medicamento agregado a la pila de medicamentos. Si no
    hay medicamentos, retorna None.
    '''

    def __str__(self):
        return f'Turno {self.numero_turno} - {self.nombre} - {self.cedula}'
    '''
    Método especial que define cómo se representará el cliente como 
    cadena de texto, mostrando el turno, nombre y cédula.
    '''

class Medicamento:
    def __init__(self, nombre, numero_turno):
        self.nombre = nombre
        self.numero_turno = numero_turno
    '''
    Constructor de la clase Medicamento que inicializa el nombre del medicamento
    y el número de turno al que está asociado.
    '''

    def __str__(self):
        return f'{self.nombre} (Turno {self.numero_turno})'
    '''
    Método especial que define cómo se representará un medicamento como cadena
    de texto, mostrando su nombre y el turno al que está asociado.
    '''

class Farmacia:
    def __init__(self):
        self.turnos = deque()  # Cola para los turnos
        self.entregas = []  # Lista general de todas las entregas realizadas
        self.numero_turno = 1  # Número de turno inicial
    '''
    Constructor de la clase Farmacia que inicializa una cola (deque) para manejar los turnos,
    una lista para registrar todas las entregas y un contador para los turnos, comenzando desde 1.
    '''

    def asignar_turno(self, cliente):
        cliente.numero_turno = self.numero_turno  # Asigna el turno actual al cliente
        self.turnos.append(cliente)  # Añade el cliente a la cola de turnos
        self.numero_turno += 1  # Incrementa el número de turno para el siguiente cliente
    '''
    Método que asigna un número de turno a un cliente y lo agrega a la cola de turnos.
    Luego, incrementa el número de turno para futuros clientes.
    '''

    def entregar_medicamentos(self, numero_turno, medicamentos):
        cliente = next((c for c in self.turnos if c.numero_turno == numero_turno), None)
        if cliente:
            for medicamento in medicamentos:
                medicamento_obj = Medicamento(medicamento, numero_turno)
                cliente.agregar_medicamento(medicamento_obj)  # Se agrega a la lista del cliente
                self.entregas.append(medicamento_obj)  # Se agrega a la lista general de entregas
            self.turnos.remove(cliente)  # Remueve al cliente de la cola de turnos una vez entregados los medicamentos
    '''
    Método para entregar medicamentos a un cliente. Recorre los medicamentos
    agregándolos a la lista de medicamentos del cliente y registrando las entregas
    en la lista general. Luego remueve al cliente de la cola de turnos.
    '''

    def deshacer_ultimo_medicamento(self, numero_turno):
        cliente = next((c for c in self.turnos if c.numero_turno == numero_turno), None)
        if cliente:
            ultimo_medicamento = cliente.deshacer_medicamento()  # Usamos pop() para deshacer el último medicamento
            if ultimo_medicamento:
                self.entregas.remove(ultimo_medicamento)  # Remueve de la lista general de entregas
    '''
    Método para deshacer el último medicamento entregado a un cliente.
    Usamos pop() para quitar el último medicamento de la lista de medicamentos del cliente,
    y si existe, también lo quitamos de la lista general de entregas.
    '''

    def mostrar_turnos(self):
        return list(self.turnos)  # Devuelve una lista de los turnos actuales
    '''
    Método que devuelve la lista de los turnos en la cola.
    '''

    def mostrar_entregas(self):
        return list(self.entregas)  # Devuelve una lista de las entregas actuales
    '''
    Método que devuelve la lista general de todas las entregas realizadas.
    '''
