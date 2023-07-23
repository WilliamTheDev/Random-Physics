import matplotlib.pyplot as mat 

ramplength = 1.9 # Meters

# Each data point is 0.022s apart, if all dots are recorded
# if every 5 data point are recorded the value should be changed to 0.1.
timeBetween = 0.022 # Seconds

# Dot distance between in mm 
data = [0, 2,2,3,4,5,6,6,6,7,7,8,8,8,9,10,
        10,11,11,11,11,11,11,11,12,12,12,
        13,13,14,14,15,15,15,15,16,16,16,
        16,16,16,17,17,17,17,17,18,18,18,
        19,19,19,20,20,20,21,21,21,21,22,
        22,22,22,23,23,23,24,24,24,25,25,
        25,25,26,26,26,26,27,27,27,28,28,
        28,29,29,29,30,30,30,30,31,31,32,
        32,32,32,32,33,33,34,36,36,36,36,
        37,37,37,37,38,38,38,38,38,39,39,
        39,39]

datalength = len(data)
time = [timeBetween*i for i in range(0, datalength)]
velocity = [data[i]/timeBetween/1000 for i in range(0, datalength)]

totalTime = (datalength*timeBetween)
averageVelocity = ramplength/totalTime
print(f'Total Time: {totalTime}s')
print(f'Average Velocity: {averageVelocity}m/s')

mat.plot(time, velocity)
mat.title("Velocity Vs Time")
mat.xlabel("Time (s)")
mat.ylabel("Velocity (m/s)")
mat.show()
