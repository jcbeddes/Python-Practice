expenditures = [
    {"job": "pressure washing", "hours": 10},
    {"job": "bathroom floor", "hours": 15},
    {"job": "pressure washing for Larry", "hours": 10},
    {"job": "shed door", "hours": 15}
]

addjob = input("Hello, do you have earnings to report? Y/N ").strip().upper()
while addjob == "Y":
    jobname = input("What was the job? ")
    hoursworked = int(input("How many hours did you work? "))
    expenditures.append ({"job": jobname, "hours": hoursworked})
    addjob = input("Do you have other earnings to report? Y/N ")


for job in expenditures:
    print(f"You spent {job['hours']} hours working on {job['job']}.")

earnings = 0

for hours in expenditures:
    earnings += hours["hours"]
earnings = earnings * 20
print(f"\nYou have earned ${earnings}")

savetofile = input("\nDo you want to save this report to a file? (Y/N) " ).strip().upper()
if savetofile == "Y":
    with open("jobs.txt", "w") as file:
        for job in expenditures:
            file.write(f"{job['job']} ... {job['hours']} hours\n")
    print("Jobs save to jobs.txt")

readfile = input("Do you want to see your saves jobs? (Y/N) ").strip().upper()
if readfile == "Y":
    print("\nPreviously saved jobs:")
    with open("jobs.txt", "r") as file:
        contents = file.read()
        print(contents)