import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import csv
import random

# QUESTION 1 Create two datasets in csv files, one for each examination, with 150 rows each.
def generate_age_group():
    age_groups = ['18 - 25', '25 - 35', '35 - 45', 'over 45']
    return random.choice(age_groups)

def generate_study_hours():
    study_hours = ['1 - 2', '2 - 3', '4 - 5']
    return random.choice(study_hours)

def generate_student_data():
    student_number = random.randint(1000, 9999)
    age_group = generate_age_group()
    hours_studying = generate_study_hours()
    student_mark = random.randint(0, 130)
    time_taken_on_exam = random.randint(0, 180) # should i
    return [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]

# Generating 150 rows of data for math114 exam file
data_one = []
for _ in range(150):
    data_one.append(generate_student_data())
# Generating 150 rows of data for cs114 exam file
data_two = []
for _ in range(150):
    data_two.append(generate_student_data())

# Writing data to CSV exam files
csv_headers = ['Student Number', 'Age Group', 'Average Hours Studying On Campus', 'Student Mark', 'Time Taken on Exam']

with open('student_data_math114.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)
    writer.writerows(data_one)
print("CSV file 'student_data_math114.csv' with 150 rows has been created.")
  
with open('student_data_cs114.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)
    writer.writerows(data_two)
print("CSV file 'student_data_cs114.csv' with 150 rows has been created.")


# QUESTION 2 Before performing operations on your data, you need to clean your data, remove any zero values and document the process thoroughly in your report.
#create arrays from columns in student_data_math114
student_num_math114 = np.array([])
avg_hours_on_campus_math114 = np.array([])
student_age_math114 = np.array([])
student_mark_math114 = np.array([])
#create arrays from columns in student_data_cs114
student_num_cs114 = np.array([])
avg_hours_on_campus_cs114 = np.array([])
student_age_cs114 = np.array([])
student_mark_cs114 = np.array([])

#fill arrays for math114 exam with loops taking info from csv files
with open(student_data_math114.csv,'r') as f: 
    f.readline()
    for i in range(150): 
        line = f.readline()
        x = line.split(',')
        np.append(student_num_math114, x[0])
        np.append(avg_hours_on_campus_math114, x[1])
        np.append(student_age_math114, x[2])
        np.append(student_mark_math114, x[3])       
#fill arrays for cs114 exam with loops taking info from csv files
with open(student_data_cs114.csv,'r') as f:
    f.readline()
    for i in range(150): 
        line = f.readline()
        x = line.split(',')
        np.append(student_num_cs114, x[0])
        np.append(avg_hours_on_campus_cs114, x[1])
        np.append(student_age_cs114, x[2])
        np.append(student_mark_cs114, x[3])
    
'''
#convert marks into percentages
student_mark_math114 = (student_mark_math114/130)*100 
student_mark_cs114 = (student_mark_cs114/130)*100 

'''

'''
# 2.1 Create frequency tables for math114 exam and cs114 exam based on the following headings, and using the following criteria:
• Average hours spent on campus
• Student age
• Student mark
https://www.statology.org/frequency-tables-python/
'''

'''
'''
# 2.2 Using Matplotlib, complete the following:
age_groups = ['18 - 25', '25 - 35', '35 - 45', 'over 45']

#Use a bar chart to show the ages and numbers of students. Your x-axis should represent the age groups used in the previous question.
age_groups = ['18 - 25', '25 - 35', '35 - 45', 'over 45']
student_age_num = np.array() #count how many student in each age range and put in array

#count numebr of students in each age group
#counters for age ranges
eighteen_twenty_five = 0
twenty_five_thirty_five = 0
thirt_five_forty_five = 0
over_forty_five = 0
with open(student_data_math114.csv,'r') as f:
    f.readline()
    for i in range(151):
        line = f.readline()
        line_info = line.split(',')
        if line_info[1] == '18 - 25':
            eighteen_twenty_five += 1
        elif line_info[1] == '25 - 35':
            twenty_five_thirty_five += 1
        elif line_info[1] == '35 - 45':
            thirt_five_forty_five += 1
        elif line_info[1] == 'over 45':
            over_forty_five += 1

student_age_num = np.append(eighteen_twenty_five)
student_age_num = np.append(twenty_five_thirty_five)
student_age_num = np.append(thirt_five_forty_five)
student_age_num = np.append(over_forty_five)

plt.bar(age_groups,student_age_num)
plt.show()

'''
with open(student_data_cs114.csv,'r') as f:
    f.readline()
'''
#Use a line graph to show if there is a correlation between higher marks(y) and more time spent on campus(x).
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'solid')
plt.show()

'''
• Use a scatter chart to plot each student’s mark(y) and the time(x) taken on the examination, in minutes.
• Use a scatter chart to plot the relationship between time spent on campus(y) and the student’s age(x).
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
plt.show()
'''

