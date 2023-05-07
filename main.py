import csv
from registro import Registro
from manejador import listaRegistro

if __name__=='__main__':
    archivo=open('registro.csv')
    newRegistro=listaRegistro()
    reader=csv.reader(archivo,delimiter=",")
    bandera=True
    for fila in reader:
        if bandera:
            bandera=False
        else:
            dia= int(fila[0])
            hora= int(fila[1])
            temp= int(fila[2])
            hum= int(fila[3])
            pres= int(fila[4])

            newRegistro.cargaRegistro(dia,hora,temp,hum,pres)
            print("\n")
    archivo.close()
    newRegistro.listaBi()
    print("\n")
    print("Mostrar para cada variable el día y hora de menor y mayor valor.")
    print("\n")
    newRegistro.temperatura()
    print("\n")
    newRegistro.humedad()
    print("\n")
    newRegistro.presion()
    print("\n")
    print("Indicar la temperatura promedio mensual por cada hora.")
    print("\n")
    newRegistro.promedio_mensual_por_hora()
    print("\n")
    newRegistro.listar_valores_por_dia(1)