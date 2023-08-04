import matplotlib.pyplot as mat
from tabulate import tabulate
import math
import os

# Gobal Variables 
magneticPermeability = 4*math.pi*pow(10, -7)
coefficientVoltage = 0.4

def MagneticFluxDensity(turns: int, current: float, length: float) -> float:
    return magneticPermeability*turns*current/length

def MagneticForce(MagneticFlux: float, ProjectileLength: float, current: float) -> float:
    return MagneticFlux*current*ProjectileLength

def VelocityStages(coils: int, turns: int, mass: float, length: float, 
                   projectileLength: float, voltage: float, resistance: float) -> None:
    velocity = 0
    x = 0
    outputx = []
    outputy = []
    stages = []
    while x < coils:
        current = (voltage-coefficientVoltage*x)/(resistance+(resistanceCo*x))
        force = MagneticForce(MagneticFluxDensity(turns, current, length), projectileLength, current)
        acceleration = force/mass
        velocity = math.sqrt((velocity*velocity)+2*acceleration*(length))
        outputy.append(velocity)
        outputx.append(x)
        stages.append([x+1, current, velocity])
        x+=1
    mat.plot(outputx, outputy)
    print(tabulate(stages, headers=['Stage', 'Ampre (A)', 'Velocity (m/s)']))
    print(f'{round(velocity*3.6)}kph')

# Interface
os.system('clear')
print('Electromagnetic Coil Gun Simulation')
print('-- single coil parameters --')
print("1. Number of turns of the coil: ")
turns = float(input())
print("2. Voltage applied to the coil: (volts)")
voltage = float(input())
print("3. Resistance of the coil: (ohms)")
resistance = float(input())
print("4. Length of the coil: (meters)")
length = float(input())
os.system('clear')
print("-- Projectile Parameters")
print("5. Projectile length: (meters) ")
projectileLength = float(input())
os.system('clear')
print("6. Projectile mass: (kg) ")
projectileMass = float(input())
os.system('clear')
print('7. Number of coils: ')
coils = int(input())
os.system('clear')

print("Processing...")
# Calcuations 
VelocityStages(coils, turns, projectileMass, length, projectileLength, voltage, resistance)
print("Graph Generated.")

mat.title("Velocity Vs Stages")
mat.xlabel(f"Stages (meters)")
mat.ylabel("Velocity (meters/second)")
mat.show()
            
            
