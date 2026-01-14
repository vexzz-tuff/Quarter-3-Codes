cities = ["City A", "City B"]

temperatures = [
    [30, 31, 29, 32, 33],
    [28, 27, 29, 30, 31]
]

for i in range(len(temperatures)):
    print(cities[i], temperatures[i])
    print("Total:", sum(temperatures[i]))
    print("Average:", sum(temperatures[i]) / len(temperatures[i]))

print("Highest temperature:", max(max(row) for row in temperatures))

#Using a 2D array made the data easy to organize by city and day. 
#It was easy to find the total and average because each city’s data was in one row. 
#Finding the highest temperature was a little harder but still manageable.