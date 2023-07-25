import matplotlib.pyplot as plt

# Affect of mass on the accelation of a trolley
# trolley mass:
trolley = 500
pullyweight = 1000  
weights = [0, 250, 500, 750]
Time = [[0.62, 0.34], # 0g 
        [0.58, 0.87], # 250g
        [0.62, 0.75], # 500g
        [0.86, 0.59]] # 750

AverageTime = [(Time[i][0]+Time[i][1])/2 for i in range(0, len(Time))]
AverageAccelation = [2/(AverageTime[i]*AverageTime[i]) for i in range(0, len(AverageTime))]
print(f'Gravity Force: {(pullyweight/1000)*9.8}N')

for A in range(0, len(AverageAccelation)):
    print(f'{weights[A]}g: {AverageTime[A]}s | {AverageAccelation[A]}m/s^2')
    x = []
    y = []
    for T in range(0, 1000):
        x.append(T/1000)
        y.append(T/1000*AverageAccelation[A])
    plt.plot(x, y)

plt.title("Velocity Vs Time")
plt.xlabel(f"Time (s)")
plt.ylabel(f"Velocity (m/s)")
plt.show()