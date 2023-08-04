import numpy as np
#import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import csv
import random

# QUESTION 1 Create two datasets in csv files, one for each examination, with 150 rows each.
# Writing data to CSV exam files
csv_headers = ['Student Number', 'Age', 'Average Hours Studying On Campus', 'Student Mark', 'Time Taken on Exam']

def generate_student_data():
    student_number = random.randint(1000, 9999)
    age_group = random.randint(18, 60)
    hours_studying = random.uniform(1, 5)
    student_mark = random.randint(0, 130)
    time_taken_on_exam = random.randint(0, 180)
    return [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]

def generate_math_exam_data():
    # Generating 150 rows of data for math114 exam file
    data_one = []
    for _ in range(150):
        data_one.append(generate_student_data())

    with open('student_data_math114.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
        writer.writerows(data_one)
    print("CSV file 'student_data_math114.csv' with 150 rows has been created.")
def generate_cs_exam_data():
    # Generating 150 rows of data for cs114 exam file
    data_two = []
    for _ in range(150):
        data_two.append(generate_student_data())

    with open('student_data_cs114.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)
        writer.writerows(data_two)
    print("CSV file 'student_data_cs114.csv' with 150 rows has been created.")
