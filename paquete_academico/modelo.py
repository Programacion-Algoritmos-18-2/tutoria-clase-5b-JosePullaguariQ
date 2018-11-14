class Persona(object):#Creamos la clase padre Persona que es una clase Padre
	def __init__(self):
		self.nombre = " "
		self.apellido = " "
		self.pais = Pais()

	#Metodos de agregar y obtener
	def agregar_nombre(self, n):
		self.nombre = n

	def obtener_nombre(self):
		return self.nombre

	def agregar_apellido(self, a):
		self.apellido = a

	def obtener_apellido(self):
		return self.apellido

	def agregar_pais(self, p):
		self.pais = p

	def obtener_pais(self):
		return self.pais
	
	#Metodo para presentar datos
	def presentar_datos(self):
		cadena = "Información:\nNombres Completos: %s-%s\n"%(self.obtener_nombre(),self.obtener_apellido())
		return cadena


class Pais(object):#Creamos la clase padre Pais que es una clase Padre
	def __init__(self):
		self.nombre = " "
		self.capital = " "

	#Metodos de agregar y obtener
	def agregar_nombre(self, n):
		self.nombre = n
	
	def obtener_nombre(self):
		return self.nombre
	
	def agregar_capital(self, capi):
		self.capital = capi
	
	def obtener_capital(self):
		return self.capital

class Estudiante(Persona):#Creamos la clase Estudiante que hereda de la clase Persona
	def __init__(self):
		super(Estudiante, self).__init__()
		self.codigo = 0

	#Metodos de agregar y obtener para atributos de la clase
	def agregar_codigo(self, c):
		self.codigo = c
	
	def obtener_codigo(self):
		return self.codigo

	#Metodo de presentar datos
	def presentar_datos(self):
		cadena = "%s Codigo:  %s\n Procedencia: Pais: %s- Capital: %s"%(super(Estudiante, self).presentar_datos(),self.obtener_codigo(),self.pais.obtener_nombre(), self.pais.obtener_capital())
		return cadena

class Est_Presencial(Estudiante):#Creamos la clase Estudante Presencial que hereda de la clase Estudiante
	def __init__(self):
		super(Est_Presencial,self).__init__()
		self.num_creditos = 0
		self.ciclo = 0
	
	#Metdos de agregar y obtener para los atributos de la clase
	def agregar_num_creditos(self, num):
		self.num_creditos = num
	
	def obtener_num_creditos(self):
		return self.num_creditos
	
	def agregar_ciclo(self, c):
		self.ciclo = c
	
	def obtener_ciclo(self):
		return self.ciclo


class Est_Distancia(Estudiante):#Creamos la clase Est_Distancia que hereda de la clase Estudiante
	def __init__(self):
		super(Est_Distancia,self).__init__()
		self.num_materias = 0
		self.modulo = " "
	
	#Metodos de agregar y obtener para los atributos de la clase
	def agregar_num_materias(self, num_mat):
		self.num_materias = num_mat
	
	def obtener_num_materias(self):
		return self.num_materias
	
	def agregar_modulo(self, m):
		self.modulo = m
	
	def obtener_modulo(self):
		return self.modulo
	
	#Metodo de presentar datos
	def presentar_datos(self):
		cadena = "%s\n Numero de materias: %s\n Modulo: %s"%(super(Est_Distancia,self).presentar_datos(),self.obtener_num_materias(),self.obtener_modulo())
		return cadena