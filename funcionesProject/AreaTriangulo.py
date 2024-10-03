# Ejemplo para calcular el area del triangulo

#Variables de entrada
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return area
#Invocar
resultado = calcularAreaTriangulo(base,altura)

#salida
print(f"El area del tringulo cuya base {base} y altura {altura} es: {resultado} " )

# Funcion con argumentos predeterminado
def my_function(country = "Colombia"):
    print("I am from " +country)

#Invocar la funcion
my_function()
my_function("Sweden")

#Argumentos arbitrarios
def mostrarEstudiante(*args):
    print("El estudiante : "+args[2])

#Invocamos la funcion
mostrarEstudiante("Emil","Tobias","Linus")

def mostrarCarros(carro1, carro2, carro3):
    print("El carro es: "+carro2)

mostrarCarros(carro1="BMW",carro3="Ferrari",carro2="Ford")

def mostrarCliente(**kwargs):
    print("Su apellido es: " + kwargs["apellido"])

mostrarCliente(nombre = "Tobias", apellido="refesnes")

def miFuncion():
    pass

x = min(5, 10, 15)
y = max(5,10,15)
print(x)
print(y)

num1 = pow(7, 4)

print(num1)
import math

num2 = math.sqrt(34)

print(num2)

num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3)
print(num4)