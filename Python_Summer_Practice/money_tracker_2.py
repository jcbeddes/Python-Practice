import os
import csv

file_path = "C:/Users/jcbed/Desktop/jobs.csv"

def view_jobs():
    with open(file_path, "r") as file:
        content = file.read()
        print(f"\n{content}")

def add_job():
    new_entry = []
    new_entry.append(input("What was the job you did? "))
    new_entry.append(float(input("How many hours did you work? ")))
    new_entry.append(float(input("How much were you paid per hour? ")))

    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(new_entry)
        print(f"Your job {new_entry} was added to jobs.csv\n")

def edit_job():
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        jobs = list(reader)
    print("\nHere are your past jobs:")
    index = 0
    for job in jobs:
        if index == 0:
            print(job)
        else:
            print(index, job)
        index +=1
    
    try:
        choice = int(input("Which job would you like to edit? (1, 2, 3, etc.): "))
        if 1 <= choice < len(jobs):
            new_job = input("New job name: ")
            new_hours = float(input("New number of hours: "))
            new_rate = float(input("New hourly rate: "))
            jobs[choice] = [new_job, new_hours, new_rate]
        else:
            print("Invalid job number.")
            return
    except ValueError:
        print("Invalid input.")
        return

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(jobs)

    print("Job updated successfully!\n")

def remove_job():
    # Step 1: Read the jobs from the file
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        jobs = list(reader)

    # Step 2: Show jobs to the user
    print("\nHere are your past jobs:\n")
    index = 0
    for job in jobs:
        if index == 0:
            print(job)
        else:
            print(index, job)
        index +=1

    # Step 3: Get user's choice and remove job
    try:
        choice = int(input("Which job would you like to remove? (1, 2, 3, etc.): "))
        if 1 <= choice < len(jobs):
            removed = jobs.pop(choice)
            print(f"\nDeleted: {removed}\n")

            # Step 4: Write updated list back to file
            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(jobs)  # ✅ writes list of rows
        else:
            print("Invalid job number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def calculate_earnings():
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        jobs = list(reader)
    item = 0
    earnings = 0
    for job in jobs:
        if item != 0:
            earnings += float(job[1])*float(job[2])
        item +=1

    print(f"\nYou have earned ${earnings}\n")

def main():

    task = 0

    try:
        task = int(input("Hello, welcome to Money Tracker 2.0! What do you wish to do today? You can:\n 1. View completed jobs \n 2. Add a job \n 3. Edit a past job \n 4. Remove a past job\n 5. Calculate earnings \n 6. Quit \n(1, 2, 3, 4, 5, 6) "))
        while task < 1 or task > 6:
            task = int(input("Enter a real number idiot...\n"))     
    except ValueError:
        print("\nEnter a real number, idiot...\n")

    while task != 6:
        if task == 1:
            view_jobs()
        elif task == 2:
            add_job()
        elif task == 3:
            edit_job()
        elif task == 4:
            remove_job()
        elif task == 5:
            calculate_earnings()
        try:
            task = int(input("Do you wish to perform another operation? You can:\n 1. View completed jobs \n 2. Add a job \n 3. Edit a past job \n 4. Remove a past job\n 5. Calculate earnings \n 6. Quit \n(1, 2, 3, 4, 5, 6) "))
            while task < 1 or task > 6:
                task = int(input("Enter a real number idiot...\n"))     
        except ValueError:
            try:
                while task < 1 or task > 6:
                    task = int(input("\nEnter a real number, idiot...\n"))
            except ValueError
    print("Goodbye.\n")
    


main()