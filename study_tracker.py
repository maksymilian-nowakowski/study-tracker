def log_study():
    date = input("Enter date (YYYY-MM-DD): ")
    hours = input("Hours studied today: ")

    with open("study_data.txt", "a") as file:
        file.write(f"{date},{hours}\n")

    print("Study session saved.")

def load_sessions():
    sessions = []
    try:
        with open("study_data.txt", "r") as file:
            for line in file:
                date, hours = line.strip().split(",")
                sessions.append((date, float(hours)))
        return sessions
    except FileNotFoundError:
        print("No study data found yet.")

def print_summary(sessions):
    if not sessions:
        print("No study sessions recorded yet.")
        return
    
    total_hours = sum(hours for _, hours in sessions)
    average = total_hours / len(sessions)

    print("Total hours studied:", total_hours)
    print("Average per session:", round(average, 2))

def main():
    log_study()
    sessions = load_sessions()
    print_summary(sessions)

main()
