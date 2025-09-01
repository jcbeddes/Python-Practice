import csv
import os

file_path = "C:/Users/jcbed/Desktop/jobs.csv"

def csv_to_list_of_lists(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        return list(reader)

my_list = csv_to_list_of_lists(file_path)
print(my_list)