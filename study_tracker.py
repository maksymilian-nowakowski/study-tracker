sessions = []

date = input("Enter date (YYYY-MM-DD):  ")
hours = input("Hours studied today: ")

with open("study_data.txt", "a") as file:
    file.write(f"{date},{hours}\n")

print("Study session saved.")

with open("study_data.txt", "r") as file:
    for line in file:
        date, hours = line.strip().split(",")
        sessions.append((date, float(hours)))

print(sessions)

total_hours = sum(hours for _, hours in sessions)
average = total_hours / len(sessions)

print("Total hours studied:", total_hours)
print("Average per session:", round(average, 2))