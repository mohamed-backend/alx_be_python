# daily_reminder.py

# Prompt for user input for the task description, priority, and time-sensitivity
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate the reminder based on task priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = "Invalid priority level. Please choose high, medium, or low."

# Add time-bound message if necessary
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no":
    reminder += ". Consider completing it when you have free time."
else:
    reminder = "Invalid input for time-bound status. Please answer 'yes' or 'no'."

# Print the final reminder
print("\nReminder:", reminder)
