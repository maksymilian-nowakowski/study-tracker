date = input("Enter date (YYYY-MM-DD):  ")
hours = input("Hours studied today: ")

with open("study_data.txt", "a") as file:
    file.write(f"{date},{hours}\n")

print("Study session saved.")