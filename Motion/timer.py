import matplotlib.pyplot as mat 
from tabulate import tabulate
import math 

# Gobal Variables 
magneticPermeability = 4*math.pi*pow(10, -7)

def MagneticFluxDensity(turns: int, voltage: float, resistance: float, length: float) -> float:
    return magneticPermeability*turns*(voltage/resistance)/length

def MagneticForce(MagneticFlux: float, ProjectileLength: float, current: float) -> float:
    return MagneticFlux*current*ProjectileLength

turns  = 160
voltage = 20.50
coilResistance = 0.2
coilLength = 0.05
distance = 0.07
projectileLength = 0.07

Density = MagneticFluxDensity(turns, voltage, coilResistance, coilLength)
Force = MagneticForce(Density, projectileLength, (voltage/coilResistance))
accelation = Force/0.01

x = []
y = []
time = 0
intialVelocity = 0
stages = []
for i in range(0, 10):
    velocity = (math.sqrt(pow(intialVelocity,2)+2*accelation*distance))
    time = (velocity-intialVelocity)/accelation
    resistance = (time/(1.1*(1*pow(10, -5))))
    x.append(i)
    y.append(time*1000)
    stages.append([i+1, velocity, time*1000, resistance])
    intialVelocity = velocity

print(tabulate(stages, headers=['Stage', 'Velocity (m/s)', 'Time (ms)', 'Resistance (ohms)']))

# Matlab 
mat.plot(x, y)
mat.title("Stages Vs Time")
mat.xlabel("Stages")
mat.ylabel("Time (ms)")
mat.show()

