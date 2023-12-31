from pylab import *
# Definición de constantes
N=1000           # Número de pasos
x0=0.0           # Posición inicial
v0=0.0           # Velocidad inicial
tau=3.0          # Tiempo en segundos de la simulación
h=tau/float(N-1)   # Paso del tiempo
gravedad=9.8      # Aceleración 9.8 m/s**2
k=3.5             # Constante elástica del resorte 
m=0.2             # Masa de la partícula

# Generamos un arreglo de Nx2 para almacenar posición y velocidad
y=zeros([N,2])
# tomamos los valores del estado inicial
y[0,0]=x0
y[0,1]=v0

# Generamos tiempos igualmente espaciados
tiempo=linspace(0,tau,N)

# Definimos nuestra ecuación diferencial
def EDO(estado,tiempo):
    f0=estado[1]
    f1=-(k/m)*estado[0]-gravedad
    return array([f0,f1])

# Método de Euler para  resolver numéricamente la EDO 
def Euler(y,t,h,f): 
    y_p=y+h*f(y,t)  # Calculamos el valor siguiente de y
    y_c=y+h*(f(y,t)+f(y_p,t+h))/2.0
    return y_c

# Ahora calculamos!
for j in range(N-1):
    y[j+1]=Euler(y[j],tiempo[j],h,EDO)

# Ahora graficamos
xdatos=[y[j,0] for j in range(N)]
vdatos=[y[j,1] for j in range(N)]

plot(tiempo,xdatos,'-r')
plot(tiempo,vdatos,'-b')
xlabel('Tiempo')
ylabel('Posición y velocidad')
show()