import matplotlib.pyplot as mat 
import math 
from tabulate import tabulate

# Gobal Variables 
magneticPermeability = 4*math.pi*pow(10, -7)

# Magnetic Feild Strength
def MagneticFluxDensity(turns: int, length: float, current: float) -> float:
    return magneticPermeability*turns*current/length

# Force acting upon the projectile
def MagneticForce(MagneticFlux: float, ProjectileLength: float, current: float) -> float:
    return MagneticFlux*current*ProjectileLength

def Accelation(Force: float, Mass: float) -> float:
    return Force/Mass

# 555 timer ic required resistance to meet time period. 
def TimeResistance(Time: float, Capactance: float) -> float: 
    return Time/(1.1*Capactance)

##Vairables 
# Source 
voltage = 20.50
voltageCo = 0.1

# Launcher
turns  = 160
coilResistance = 0.2
resistanceCo = 0.03 + 0.009
coilLength = 0.05
distance = 0.07
coils = 10
eff = 58.517555267/100 

# Projectile
projectileLength = 0.1
projectileMass = 0.01

intialVelocity = 0
stageout = []
velocityout = []
timeout = []
stages = []

for x in range(0, 10):
    current = (voltage-voltageCo*x)/(resistanceCo*x+coilResistance)
    density = MagneticFluxDensity(turns, coilLength, current)
    force = MagneticForce(density, projectileLength, current)
    accelation = Accelation(force, projectileMass)
    velocity = math.sqrt(pow(intialVelocity, 2)+2*accelation*distance)
    time = (velocity-intialVelocity)/accelation
    resistance = TimeResistance(time, (1*pow(10, -5)))
    stageout.append(x+1)
    velocityout.append(velocity*eff)
    kenticEnergy = 1/2*projectileMass*pow(velocity,2)
    timeout.append(time*1000)
    stages.append([x+1, round(current,2), round(ResistanceCo*x+coilResistance,2), round(velocity*eff,2), round(kenticEnergy, 2), round(time*1000,2), round(resistance)])
    intialVelocity = velocity

print(tabulate(stages, headers=['Stage', 'Current (Amps)', 'CResistance (ohms)', 'Velocity (m/s)', 'Kentic Energy (J)', 'Time (ms)', 'TResistance (ohms)']))

totaltime = 0
for i in range(0, len(stageout)):
    totaltime = totaltime + timeout[i]

print(f'Total Time: {round(totaltime,2)} ms')
print(f'Speed: {round(velocityout[len(stageout)-1]*3.6,2)} kph')
print(f'Eff: {eff*100}%')
# Matlab 
mat.plot(stageout, velocityout)
mat.plot(stageout, timeout)
mat.title("Stages Vs Time & Velocity")
mat.xlabel("Stages")
mat.ylabel("Time (ms) & Velocity (M/s)")
mat.show()
