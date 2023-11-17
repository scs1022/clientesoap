from flask import Flask, render_template, request
from zeep import Client

app = Flask(__name__)

wsdl = 'https://servicios-r7yq.onrender.com/?wsdl'
client = Client(wsdl)

def obtener_vehiculos():
    return client.service.obtenerVehiculos()

def obtener_vehiculo(placa):
    request_data = {'placaVehiculo': placa}
    return client.service.obtenerVehiculo(**request_data)

def crear_vehiculo(placa, modelo, precio, soat):
    request_data = {
        'placaVehiculo': placa,
        'modeloVehiculo': int(modelo),
        'precioVehiculo': int(precio),
        'ultimoAnoSOAT': int(soat)
    }
    return client.service.crearVehiculo(**request_data)

def consulta_valor_seguro(placa):
    request_data = {'placaVehiculo': placa}
    return client.service.consultaValorSeguro(**request_data)

def consultar_todo_riesgo(placa):
    request_data = {'placaVehiculo': placa}
    return client.service.consultarTodoRiesgo(**request_data)

def consultar_soat(placa):
    request_data = {'placaVehiculo': placa}
    return client.service.consultarSOAT(**request_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = ''
    
    if request.method == 'POST':
        operation = request.form.get('operation')
        
        placa = request.form.get('placa')
        
        if operation == "obtenerVehiculos":
            resultado = obtener_vehiculos()
        elif operation == "obtenerVehiculo":
            resultado = obtener_vehiculo(placa)
        elif operation == "crearVehiculo":
            modelo = request.form.get('modelo')
            precio = request.form.get('precio')
            soat = request.form.get('soat')
            resultado = crear_vehiculo(placa, modelo, precio, soat)
        elif operation == "consultaValorSeguro":
            resultado = consulta_valor_seguro(placa)
        elif operation == "consultarTodoRiesgo":
            resultado = consultar_todo_riesgo(placa)
        elif operation == "consultarSOAT":
            resultado = consultar_soat(placa)
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
