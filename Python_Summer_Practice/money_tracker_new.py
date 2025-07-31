import os
import csv

file_path = "C:/Users/jcbed/Desktop/jobs.csv"


# def view_jobs():
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)

# def add_job():
    # new_entry = []
    # new_entry.append(input("What was the job you did? "))
    # new_entry.append(float(input("How many hours did you work? ")))
    # new_entry.append(float(input("How much were you paid per hour? ")))

    # with open(file_path, "a", newline="") as file:
    #     writer = csv.writer(file)
    #     writer.writerow(new_entry)
    #     print(f"Your job {new_entry} was added to jobs.csv\n")

def edit_job():
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        jobs = list(reader)
    print("Here are your past jobs:")
    index = 0
    for job in jobs:
        if index == 0:
            print(job)
        else:
            print(index, job)
        index +=1
    
    try:
        choice = int(input("Which job would you like to edit? (1, 2, 3, etc.): ")) - 1
        if 0 <= choice < len(jobs):
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

    print("Job updated successfully!")

edit_job()

# def remove_job():
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)

# def save_to_file():
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)

# def calculate_earnings():
#     with open(file_path, "r") as file:

# def new_task():

# def main():
#     task = input("Hello, welcome to Money Tracker 2.0! What do you wish to do today? You can:\n 1. View completed jobs \n 2. Add a job \n 3. Edit a past job \n 4. Remove a past job \n 5. Save to file \n 6. Calculate earnings \n 7. Quit \n(1, 2, 3, 4, 5, 6, 7) "):
#     while task != 7 or "q" or "Q":
#         match task
#             case 1:
#                 view_jobs()
#             case 2:
#                 add_job()
#             case 3:
#                 edit_job()
#             case 4:
#                 remove_job()
#             case 5:
#                 save_to_file()
#             case 6:
#                 calculate_earnings()
        
# main()