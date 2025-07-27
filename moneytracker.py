import os

expenditures = []

if os.path.exists("jobs.txt"):
    with open("jobs.txt", "r") as file:
        for line in file:
            # Split line: "Job name ... 10.0 hours"
            if "..." in line:
                parts = line.strip().split("...")
                jobname = parts[0].strip()
                hours_str = parts[1].strip().split(" ")[0]  # Just the number part
                try:
                    hours = float(hours_str)
                    expenditures.append({"job": jobname, "hours": hours})
                except ValueError:
                    pass

def addjob():
    jobname = input("What was the job? ")
    hoursworked = float(input("How many hours did you work? "))
    expenditures.append ({"job": jobname, "hours": hoursworked})

def printjob():
    print()
    for job in expenditures:
        print(f"You spent {job['hours']} hours working on {job['job']}.")
    print()

def calculateearnings():
    earnings = 0
    for hours in expenditures:
        earnings += hours["hours"]
    earnings = earnings * 20
    print(f"\nYou have earned ${earnings}\n")

def savetofile():
    with open("jobs.txt", "w") as file:
        for job in expenditures:
            file.write(f"{job['job']} ... {job['hours']} hours\n")
    print("\nJobs save to jobs.txt\n")

def readfile():
    print("\nPreviously saved jobs:")
    with open("jobs.txt", "r") as file:
        contents = file.read()
        print(contents)

def performtask():
    task = int(input("What task do you wish to perform? \nAdd job:1 \nPrint job:2 \nCalculate earnings:3 \nSave to file: 4 \nView past jobs: 5 \nQuit 6 \n"))
    while task != 6:
        if task == 1:
            addjob()
            task = int(input("\nWhat other task do you wish to perform? \nAdd job:1 \nPrint job:2 \nCalculate earnings:3 \nSave to file: 4 \nView past jobs: 5 \nQuit 6 \n"))
        elif task == 2:
            printjob()
            task = int(input("\nWhat other task do you wish to perform? \nAdd job:1 \nPrint job:2 \nCalculate earnings:3 \nSave to file: 4 \nView past jobs: 5 \nQuit 6 \n"))
        elif task == 3:
            calculateearnings()
            task = int(input("\nWhat other task do you wish to perform? \nAdd job:1 \nPrint job:2 \nCalculate earnings:3 \nSave to file: 4 \nView past jobs: 5 \nQuit 6 \n"))
        elif task == 4:
            savetofile()
            task = int(input("\nWhat other task do you wish to perform? \nAdd job:1 \nPrint job:2 \nCalculate earnings:3 \nSave to file: 4 \nView past jobs: 5 \nQuit 6 \n"))
        elif task == 5:
            readfile()
            task = int(input("\nWhat other task do you wish to perform? \nAdd job:1 \nPrint job:2 \nCalculate earnings:3 \nSave to file: 4 \nView past jobs: 5 \nQuit 6 \n"))
        else:
            task = int(input("\nPlease select a number 1-6: "))

def main():
    print("\nHello, welcome to Money Tracker!\n")
    performtask()
                         
main()