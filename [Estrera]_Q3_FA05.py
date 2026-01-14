ames = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_totals = []

for day in range(len(days)):
    total = 0
    for person in range(len(steps)):
        total += steps[person][day]
    daily_totals.append(total)
    print(days[day], "total steps:", total)

highest_steps = max(daily_totals)
most_active_day = days[daily_totals.index(highest_steps)]

print("Most active day overall:", most_active_day)






