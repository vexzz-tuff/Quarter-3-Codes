cities = ["City A", "City B"]

temperatures = [
    [30, 31, 29, 32, 33],
    [28, 27, 29, 30, 31]
]

print(temperatures[1][2])

temperatures[0][0] = 31

print(sum(temperatures[0]) / 5)

#I chose this dataset because weather changes every day and is easy to track. 
#A 2D array helps organize the temperatures by city and day.
#Each row shows one city, and each column shows a day. 
#This makes the data easy to read and calculate.