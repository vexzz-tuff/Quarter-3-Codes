steps = [
    [4500, 5200, 4800, 5000, 5300],  # Person 1
    [4000, 4100, 3900, 4200, 4600],  # Person 2
    [6000, 5800, 5900, 6100, 6200]   # Person 3
]

print("Steps Record:\n")

all_steps = []

for i in range(len(steps)):
    total = sum(steps[i])
    average = total / len(steps[i])

    print("Person", i + 1, "steps:", steps[i])
    print("Total steps:", total)
    print("Average steps:", average)
    print()

    all_steps.extend(steps[i])

print("Highest step count:", max(all_steps))
print("Lowest step count:", min(all_steps))