import os.path
import datetime
import json
# HABIT TRACKER

# Streaks

#Why is this habit tracker any different

#How do we make the user actually enjoy doing this, maybe set up reward systems ect ect

#Maybe daily notifcations and check ups like "How are you doing" and more, and be able to turn off these in settings incase 2 annoying

# Run in the background

# Notfication system, maybe on discord? or maybe we send it 2 the users device

# Encourage users to improve habits, with making addicting ways, such as visualizers made playfully, 

# Also have an todo list built in, where u can also assign habits, e.g Brush teeth, Habit:Stretch, etc ect

def start():
    habits_file = "habits.json"
    goals_file = "goals.json"

    habits_exist = os.path.isfile(habits_file)
    goals_exist = os.path.isfile(goals_file)

    if not habits_exist:
        print("Let's set up your habits!")
        userhabitsask = input("What habits do you want to grow? (comma separated) :) ")
        habits = [habit.strip() for habit in userhabitsask.split(",")]
        with open(habits_file, 'w') as f:
            json.dump(habits, f, indent=4)
        print(f"Habits saved to {habits_file}")
    else:
        print("Habits file found, skipping setup.")

    if not goals_exist:
        print("Let's set up your goals!")
        usergoalsask = input("What goals do you want to achieve? (comma separated) :) ")
        goals = [goal.strip() for goal in usergoalsask.split(",")]
        with open(goals_file, 'w') as f:
            json.dump(goals, f, indent=4)
        print(f"Goals saved to {goals_file}")
    else:
        print("Goals file found, skipping setup.")

def todolist():
    while True:
        print("TODO List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Back to Main Menu")
        
        choice = int(input("Please choose an option: "))

        if choice == 1:
            task = input("Enter the task you want to add: ")
            with open('todo.json', 'a') as f:
                f.write(task + '\n')
            print(f"Task '{task}' added to your TODO list.")
        elif choice == 2:
            try:
                with open('todo.json', 'r') as f:
                    tasks = f.readlines()
                if tasks:
                    print("Your TODO List:")
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task.strip()}")
                else:
                    print("Your TODO list is empty.")
            except FileNotFoundError:
                print("No TODO list found.")
        elif choice == 3:
            try:
                with open('todo.json', 'r') as f:
                    tasks = f.readlines()
                if tasks:
                    for i, task in enumerate(tasks, 1):
                        print(f"{i}. {task.strip()}")
                    task_num = int(input("Enter the task number you want to remove: "))
                    if 0 < task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        with open('todo.json', 'w') as f:
                            f.writelines(tasks)
                        print(f"Task '{removed_task.strip()}' removed from your TODO list.")
                    else:
                        print("Invalid task number.")
                else:
                    print("Your TODO list is empty.")
            except FileNotFoundError:
                print("No TODO list found.")
        elif choice == 4:
            return
        else:
            print("Invalid choice, please try again.")

def track_habits():
    habits_file = "habits.json"
    goals_file = "goals.json"
    streak_file = "streak.json"
    today = datetime.date.today()

    if not os.path.isfile(habits_file):
        print("No habits found. Please set up your habits first.")
        start()
        return

    if not os.path.isfile(goals_file):
        print("No goals found. Please set up your goals first.")
        start()
        return

    with open(habits_file, 'r') as f:
        habits = json.load(f)
    with open(goals_file, 'r') as f:
        goals = json.load(f)

    try:
        with open(streak_file, 'r') as f:
            streak_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        streak_data = {}

    for habit in habits:
        if habit not in streak_data:
            streak_data[habit] = {"last_date": None, "streak": 0}

    print("\nYour Habits:")
    for habit in habits:
        print(f"- {habit}")

    print("\nYour Goals:")
    for goal in goals:
        print(f"- {goal}")

    print("\nLet's track your streaks!")
    for habit in habits:
        print(f"Did you complete '{habit}' today? (y/n)")
        done = input("> ").strip().lower()
        last_date = streak_data[habit]["last_date"]
        streak = streak_data[habit]["streak"]

        if done == 'y':
            if last_date != str(today):
                if last_date == str(today - datetime.timedelta(days=1)):
                    streak += 1
                else:
                    streak = 1
                streak_data[habit]["last_date"] = str(today)
                streak_data[habit]["streak"] = streak
            else:
                print(f"You've already tracked '{habit}' today.")
        else:
            print(f"'{habit}' not completed today. Streak reset.")
            streak_data[habit]["streak"] = 0
            streak_data[habit]["last_date"] = str(today)

    with open(streak_file, 'w') as f:
        json.dump(streak_data, f, indent=4)

    print("\nCurrent Streaks:")
    for habit in habits:
        print(f"'{habit}': {streak_data[habit]['streak']} day(s)")

def remindertype():
    print("WIP")

def notif_frequency():
    print("WIP")

def settings():
    print("Welcome to settings"
          "\n1. Notifications"
          "\n2. Back to Main Menu")
    while True:
        choice = int(input("Please choose an option: "))
        
        if choice == 1:
            print("Welcome to the Notfication settings" \
            "\n 1. Type of reminder output (Discord/System)" \
            "\n 2. frequency of notifcations (Hours, e.g every 6 hours) ")
            notif_choice = int(input("Please choose an option: "))
            if notif_choice == 1:
                remindertype()
            elif notif_choice == 2:
                notif_frequency()
            else:
                print("Invalid choice, please try again :3")
        elif choice == 2:
            return        
        else:
            print("Invalid choice, please try again.")
def mainmenu():
    while True:
        print("Welcome to the Habit Tracker!" 
        "\n1. Start/Track Habits" 
        "\n2. TODO List" 
        "\n3. Settings" 
        "\n4. Exit")
        choice = int(input("Please choose an option: "))

        if choice == 1:
            start()
            track_habits()
        elif choice == 2:
            todolist()
        elif choice == 3:
            settings()
        elif choice == 4:
            print("Exiting the Habit Tracker. Goodbye!")
            exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    start()
    mainmenu()
