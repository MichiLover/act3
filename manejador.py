from registro import Registro

class listaRegistro:
    __lista = []

    def __init__(self):

        self.__lista=[]

    def cargaRegistro(self,dia,hora,temp,hum,pres):

        newRegistro=Registro(dia,hora,temp,hum,pres)
        self.__lista.append(newRegistro)

    def listaBi(self):
        lista_bidimensional = [[None]*5 for _ in range(2)]
        # Llenar lista bidimensional con registros
        for Datos in self.__lista:
            dia = Datos.getDia() - 1  # Restar 1 para que el índice empiece en 0
            hora = Datos.getHora() - 1  # Restar 1 para que el índice empiece en 0
            lista_bidimensional[dia][hora] = Datos

             # Imprimir lista bidimensional
        for i in range(2):
            for j in range(5):
                Datos = lista_bidimensional[i][j]
                if Datos is None:
                    print("No hay registro para el día {} y hora {}".format(i+1, j+1))
                else:
                    print("Registro para el día {} y hora {}: temperatura={}, humedad={}, presión={}".format(
                        i+1, j+1, Datos.getTemp(), Datos.getHum(), Datos.getPres()))  

    def temperatura(self):
        # Variables para almacenar los valores máximos y mínimos
        max_temp = 0
        min_temp = 0
        max_temp_dia = ''
        max_temp_hora = ''
        min_temp_dia = ''
        min_temp_hora = ''

        # Recorrer la lista de registros
        for registro in self.__lista:

            # Obtener el valor de temperatura del registro actual
            temp_actual = registro.getTemp()

            # Actualizar valores máximos y mínimos si corresponde
            if temp_actual > max_temp:
                max_temp = temp_actual
                max_temp_dia = registro.getDia()
                max_temp_hora = registro.getHora()
            if temp_actual < min_temp or min_temp == 0:
                min_temp = temp_actual
                min_temp_dia = registro.getDia()
                min_temp_hora = registro.getHora()

        # Mostrar los resultados
        print('Temperatura máxima:', max_temp, '°C, día:', max_temp_dia, ', hora:', max_temp_hora)
        print('Temperatura mínima:', min_temp, '°C, día:', min_temp_dia, ', hora:', min_temp_hora)

    def humedad(self):
        # Variables para almacenar los valores máximos y mínimos
        max_hum = 0
        min_hum = 0
        max_hum_dia = ''
        max_hum_hora = ''
        min_hum_dia = ''
        min_hum_hora = ''

        # Recorrer la lista de registros
        for registro in self.__lista:

            # Obtener el valor de humedad del registro actual
            hum_actual = registro.getHum()

            # Actualizar valores máximos y mínimos si corresponde
            if hum_actual > max_hum:
                max_hum = hum_actual
                max_hum_dia = registro.getDia()
                max_hum_hora = registro.getHora()
            if hum_actual < min_hum or min_hum == 0:
                min_hum = hum_actual
                min_hum_dia = registro.getDia()
                min_hum_hora = registro.getHora()

        # Mostrar los resultados
        print('Humedad máxima:', max_hum, '°C, día:', max_hum_dia, ', hora:', max_hum_hora)
        print('Humedad mínima:', min_hum, '°C, día:', min_hum_dia, ', hora:', min_hum_hora)

    def presion(self):
        # Variables para almacenar los valores máximos y mínimos
        max_pres = 0
        min_pres = 0
        max_pres_dia = ''
        max_pres_hora = ''
        min_pres_dia = ''
        min_pres_hora = ''

        # Recorrer la lista de registros
        for registro in self.__lista:

            # Obtener el valor de presion del registro actual
            pres_actual = registro.getPres()

            # Actualizar valores máximos y mínimos si corresponde
            if pres_actual > max_pres:
                max_pres = pres_actual
                max_pres_dia = registro.getDia()
                max_pres_hora = registro.getHora()
            if pres_actual < min_pres or min_pres == 0:
                min_pres = pres_actual
                min_pres_dia = registro.getDia()
                min_pres_hora = registro.getHora()

        # Mostrar los resultados
        print('Presion máxima:', max_pres, '°C, día:', max_pres_dia, ', hora:', max_pres_hora)
        print('Presion mínima:', min_pres, '°C, día:', min_pres_dia, ', hora:', min_pres_hora)


    #Esto se usa para buscar las temperaturas por cada hora
    def agregar(self, registro):
        self.__lista.append(registro)

    def promedio_mensual_por_hora(self):
            # Crear una lista de 5 listas (una por cada hora del día)
            temp_por_hora = [[] for _ in range(5)]

            # Recorrer la lista de registros y agregar la temperatura a la lista correspondiente
            for registro in self.__lista:
                hora = registro.getHora()
                temp = registro.getTemp()
                temp_por_hora[hora-1].append(temp)

            # Calcular la temperatura promedio para cada hora
            # se crea un enumerado que va a comenzar en 1, y el for recorre cada hora y su lista correspondiente de temperaturas
            #start es un parámetro opcional que se utiliza para especificar el índice inicial del enumerado.

            for hora, temp_list in enumerate(temp_por_hora, start=1):
                if temp_list:
                    promedio = sum(temp_list) / len(temp_list)
                    print(f"Promedio de temperatura para la hora {hora}: {promedio}")
                else:
                    print(f"No hay registros para la hora {hora}")

    def listar_valores_por_dia(self, dia):
            for registro in self.__lista:
                if registro.getDia() == dia:
                    print(f"Hora: {registro.getHora()}, Temperatura: {registro.getTemp()}, Humedad: {registro.getHum()}")    


