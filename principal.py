#Importamos el paquete donde este el modelo.py
from paquete_academico.modelo import * 

#Creamos el objeto 1
p = Pais()
p.agregar_nombre("Ecudaor")
p.agregar_capital("Quito")

#Creamos el objeto 2
est1 = Est_Distancia()
est1.agregar_nombre("José")
est1.agregar_apellido("Diaz")
est1.agregar_codigo("11012")
est1.agregar_num_materias(5)
est1.agregar_modulo("Noveno")
est1.agregar_pais(p)

#Presentamos datos
print(est1.presentar_datos())