names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []

for i in range(len(steps)):
    total_steps = sum(steps[i])
    totals.append(total_steps)
    print(names[i], "total steps:", total_steps)

highest_steps = max(totals)
lowest_steps = min(totals)

highest_index = totals.index(highest_steps)
highest_person = names[highest_index]

print("\nPerson with the highest total steps:", highest_person)
print("Difference between highest and lowest steps:", highest_steps - lowest_steps)