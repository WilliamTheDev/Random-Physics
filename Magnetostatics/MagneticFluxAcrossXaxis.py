import matplotlib.pyplot as mat
import math
import os

# Gobal Variables 
magneticPermeability = 4*math.pi*pow(10, -7)

def MagneticFluxDensity(turns: int, voltage: float, resistance: float, length: float) -> float:
    return magneticPermeability*turns*(voltage/resistance)/length
     
def DensityAcrossXAxis(MagneticFlux: float, length: float, radius: float, x) -> float:
    d1 = (length/2+x)/(math.sqrt(pow(radius, 2)+pow((length/2+x), 2)))
    d2 = (length/2-x)/(math.sqrt(pow(radius, 2)+pow((length/2-x), 2)))
    return MagneticFlux*(d1+d2)

def PointDensity(pointsAcrossXaxis, magneticFlux: float, length: float, radius: float) -> None:
    x = -length/1.2
    outputx = []
    outputy = []
    while x < length/1.2:
        outputx.append(x)
        outputy.append(DensityAcrossXAxis(magneticFlux, length, radius, x))
        x+=length/pointsAcrossXaxis
    mat.plot(outputx, outputy)
    return None

# Interface
print('Finite continuous solenoid Simulation')
print('1. Number of turns of the coil:')
turns = int(input())
os.system('clear')
print("2. Voltage appiled to the coil: (volts)")
voltage = float(input())
os.system('clear')
print("3. Resistance of the coil: (ohms)")
resistance = float(input())
os.system('clear')
print("6. length of the coil: (meters)")
length = float(input())
os.system('clear')
print("5. Outer Radius of the coil: (meters)")
OuterRadius = float(input())
os.system('clear')
print("5. Number of probe points: ")
pointsAcrossXaxis = int(input())
os.system('clear')
print("Processing...")

# Calcuations 
magneticFlux = MagneticFluxDensity(turns, voltage, resistance, length)
PointDensity(pointsAcrossXaxis, magneticFlux, length, OuterRadius)
print("Graph Generated.")

mat.title("Magnetic Flux Vs Distance")
mat.xlabel(f"Distance (m)")
mat.ylabel(f"Magnetic Flux (T)")
mat.show()
