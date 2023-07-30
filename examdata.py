import numpy as np
#import scipy as sp
#import pandas as pd
import matplotlib.pyplot as plt
import csv
import random

'''
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

'''

# QUESTION 2 Before performing operations on your data, you need to clean your data, remove any zero values and document the process thoroughly in your report.
#create arrays from columns in student_data_math114
# student_num_math114 = np.array([])
# avg_hours_on_campus_math114 = np.array([])
# student_age_math114 = np.array([])
# student_mark_math114 = np.array([])
# #create arrays from columns in student_data_cs114
# student_num_cs114 = np.array([])
# avg_hours_on_campus_cs114 = np.array([])
# student_age_cs114 = np.array([])
# student_mark_cs114 = np.array([])
#
# #fill arrays for math114 exam with loops taking info from csv files
# with open('student_data_math114.csv', mode='r', newline='') as f:
#     f.readline()
#     for i in range(150):
#         line = f.readline()
#         x = line.split(',')
#         np.append(student_num_math114, x[0])
#         np.append(avg_hours_on_campus_math114, x[1])
#         np.append(student_age_math114, x[2])
#         np.append(student_mark_math114, x[3])
# #fill arrays for cs114 exam with loops taking info from csv files
# with open('student_data_math114.csv', mode='r', newline='') as f:
#     f.readline()
#     for i in range(150):
#         line = f.readline()
#         x = line.split(',')
#         np.append(student_num_cs114, x[0])  #can i append numpy arrays like this???
#         np.append(avg_hours_on_campus_cs114, x[1])
#         np.append(student_age_cs114, x[2])
#         np.append(student_mark_cs114, x[3])
#
# '''
# #convert marks into percentages
# student_mark_math114 = (student_mark_math114/130)*100
# student_mark_cs114 = (student_mark_cs114/130)*100
#
# '''
#
# '''
# # 2.1 Create frequency tables for math114 exam and cs114 exam based on the following headings, and using the following criteria:
# • Average hours spent on campus
# • Student age
# • Student mark
# https://www.statology.org/frequency-tables-python/
# '''
#
# '''
# '''
# # 2.2 Using Matplotlib, complete the following:
# # Use a bar chart to show the ages and numbers of students.
# # Your x-axis should represent the age groups used in the previous question.
# age_groups = ['18 - 25', '25 - 35', '35 - 45', 'over 45']
# # count how many student in each age range and put in array
# student_age_num = np.array([])
#
# # count number of students in each age group
# # by creating counters for each age group
# eighteen_twenty_five = 0
# twenty_five_thirty_five = 0
# thirty_five_forty_five = 0
# over_forty_five = 0
# with open('student_data_math114.csv', mode='r', newline='') as f:
#     f.readline()
#     for i in range(150):
#         line = f.readline()
#         line_info = line.split(',')
#         if line_info[1] == '18 - 25':
#             eighteen_twenty_five += 1
#         elif line_info[1] == '25 - 35':
#             twenty_five_thirty_five += 1
#         elif line_info[1] == '35 - 45':
#             thirty_five_forty_five += 1
#         elif line_info[1] == 'over 45':
#             over_forty_five += 1
#
# student_age_num = np.append(student_age_num, eighteen_twenty_five)
# student_age_num = np.append(student_age_num, twenty_five_thirty_five)
# student_age_num = np.append(student_age_num, thirty_five_forty_five)
# student_age_num = np.append(student_age_num, over_forty_five)

'''
#Didnt work, because was using arrays instead of numpy array
plt_bar = plt.bar(age_groups, student_age_num)
plt.bar(age_groups, student_age_num)
'''

# # Putting arrays into numpy array functions, so we can use in matplotlib
# x = np.array(age_groups)
# y = student_age_num

# plt.bar(x, y)
# plt.show()
# labelling x-axis and y-axis
#plt.xlabel('Age Group')
#plt.ylabel('Number of Students')
# displaying the title
#plt.title("Bar Graph showing number of Students per age group")

# REPEAT FOR CS114 change counter names to indicate exam sub

#Use a line graph to show if there is a correlation between higher marks(y) and more time spent on campus(x).

# variables to store num of student in each time category
# num_students_one_two = 0
# num_students_two_three = 0
# num_students_four_five = 0
# study_hours = ['1 - 2', '2 - 3', '4 - 5']
# x = np.array(study_hours)
# sum_grades_one_two = 0
# sum_grades_two_three = 0
# sum_grades_four_five = 0
#
# y = np.array([])
# # get average study hours for each group
# with open('student_data_math114.csv', mode='r', newline='') as f:
#     f.readline()
#     for i in range(150):
#         line = f.readline()
#         line_info = line.split(',')
#         if line_info[2] == '1 - 2':
#             #get percentage of each student's mark, then add it to grades_students_one_two and
#             sum_grades_one_two = sum_grades_one_two + (int(line_info[3])/130) *100
#             num_students_one_two += 1
#         elif line_info[2] == '2 - 3':
#             sum_grades_two_three = sum_grades_two_three + (int(line_info[3])/130) *100
#             num_students_two_three += 1
#         elif line_info[2] == '4 - 5':
#             sum_grades_four_five = sum_grades_four_five + (int(line_info[3])/130) *100
#             num_students_four_five += 1
#
# avg_one_two = sum_grades_one_two/num_students_one_two
# avg_two_three = sum_grades_two_three/num_students_two_three
# avg_four_five = sum_grades_four_five/num_students_four_five
# average = np.array([avg_one_two, avg_two_three, avg_four_five])
# y = np.append(y, num_students_one_two)
# y = np.append(y, num_students_two_three)
# y = np.append(y, num_students_four_five)
#
# plt.plot(x, y)
# # labelling x-axis and y-axis
# plt.xlabel('time spent on campus')
# plt.ylabel('Student Mark')
# # displaying the title
# plt.title('line graph showing correlation between marks and time spent on campus')
# plt.show()

#Use a scatter chart to plot each student’s mark(y) and the time(x) taken on the examination, in minutes.
# def sort_array(array):
#     # bubble sort
#     for first_idx, first_item in enumerate(array):
#         for second_idx, second_item in enumerate(array):
#             if int(array[first_idx][4]) < int(array[second_idx][4]):
#                 # TODO: make sort make sense
#                 smaller = array[second_idx]
#                 bigger = array[first_idx]
#                 array[first_idx] = smaller
#                 array[second_idx] = bigger
#     return array
#
# x = np.array([]) #time taken
# y = np.array([]) #student mark
#
# new_array = []
# with open('student_data_math114.csv', mode='r', newline='') as file:
#     file.readline()
#     for line in file:
#         stripped_line = line.rstrip('\r\n')
#         line_items = stripped_line.split(',')
#         new_array.append(line_items)
#     # sort array of lines in ascending order by time which is index 4 of each line
#
# sorted_array = sort_array(new_array)
# for sorted_item in sorted_array:
#     # [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]
#     y = np.append(y, (int(sorted_item[3])/130) *100)
#     x = np.append(x, int(sorted_item[4]))
# plt.scatter(x, y)
#
# # labelling x-axis and y-axis
# plt.xlabel('Time Spent On Exam')
# plt.ylabel('Student Mark')
# # # displaying the title
# plt.title('Scatter Chart of Student Marks and Time spent on Math114 Exam')
# plt.show()

# TODO: Complete the below!!!!!!!!!!!!!!!!!!
# # Use a scatter chart to plot the relationship between time spent on campus(y) and the student’s age(x).
# x = np.array([])
# y = np.array([])
# with open('student_data_math114.csv', mode='r', newline='') as f:
#     f.readline()
#     for i in range(150):
#         line = f.readline()
#         line_info = line.split(',')
#         np.append(y, line_info[1])
#         np.append(x, line_info[2])
# plt.scatter(x, y)

# labelling x-axis and y-axis
# plt.xlabel('time spent on campus')
# plt.ylabel('marks')
# # displaying the title
# plt.title('line graph showing correlation between marks and time spent on campus')

# plt.show()
#
