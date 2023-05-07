class Registro:
    __dia=''
    __hora=''
    __temperatura=''
    __humedad=''
    __presion=''

    def __init__(self,dia,hora,temp,hum,pres):
        self.__dia = dia
        self.__hora = hora
        self.__temperatura = temp
        self.__humedad = hum
        self.__presion = pres

    def getDia(self):
        return self.__dia

    def getHora(self):
        return self.__hora

    def getTemp(self):
        return self.__temperatura
    
    def getHum(self):
        return self.__humedad

    def getPres(self):
        return self.__presion