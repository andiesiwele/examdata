import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# QUESTION 2 Before performing operations on your data, you need to clean your data, remove any zero values and document the process thoroughly in your report.
# 2.1 Create frequency tables for math114 and cs114 exams based on the following headings, and using the following criteria:

# 2.1.1 a) Create frequency table showing average hours Math114 students spent studying on campus
def freq_avg_study_hrs_math114():
    data = {}
    # count number of students in each category of hours using the following counters
    one_two_hours_math114counter = 0
    two_three_hours_math114counter = 0
    three_four_hours_math114counter = 0
    four_five_hours_math114counter = 0
    with open('student_data_math114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if float(y[2]) < 2:
                one_two_hours_math114counter += 1
            elif float(y[2]) < 3:
                two_three_hours_math114counter += 1
            elif float(y[2]) < 4:
                three_four_hours_math114counter += 1
            elif float(y[2]) <= 5:
                four_five_hours_math114counter += 1

    data['Average Hours Studying'] = ['1 - 2', '2 - 3', '3 - 4', '4 - 5']
    data['Frequency'] = [one_two_hours_math114counter, two_three_hours_math114counter, three_four_hours_math114counter, four_five_hours_math114counter]
    # Creating a DataFrame from the frequency table data
    frequency_table_df = pd.DataFrame(data)
    heading = "Average Hours Spent on Campus by Math114 Students"
    print(heading)
    print(frequency_table_df.to_string(index=False))

# 2.1.1 b) Create frequency table showing average hours CS114 students spent studying on campus
def freq_avg_study_hrs_cs114():
    data = {}
    # count number of students in each category of hours using the following counters
    one_two_hours_cs114counter = 0
    two_three_hours_cs114counter = 0
    three_four_hours_cs114counter = 0
    four_five_hours_cs114counter = 0
    with open('student_data_cs114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if float(y[2]) < 2:
                one_two_hours_cs114counter += 1
            elif float(y[2]) < 3:
                two_three_hours_cs114counter += 1
            elif float(y[2]) < 4:
                three_four_hours_cs114counter += 1
            elif float(y[2]) <= 5:
                four_five_hours_cs114counter += 1

    data['Average Hours Studying'] = ['1 - 2', '2 - 3', '3 - 4', '4 - 5']
    data['Frequency'] = [one_two_hours_cs114counter, two_three_hours_cs114counter, three_four_hours_cs114counter, four_five_hours_cs114counter]
    # Creating a DataFrame from the frequency table data
    frequency_table_df = pd.DataFrame(data)
    heading = "Average Hours Spent on Campus by CS114 Students"
    print(heading)
    print(frequency_table_df.to_string(index=False))

# 2.1.2 a) Create frequency table showing student ages of Math114 Students
def freq_student_ages_math114():
    data = {}
    eighteen_twenty_five_age_math114counter = 0
    twenty_five_thirty_five_age_math114counter = 0
    thirty_five_forty_five_age_math114counter = 0
    over_forty_five_age_math114counter = 0
    with open('student_data_math114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if int(y[1]) <= 25:
                eighteen_twenty_five_age_math114counter += 1
            elif int(y[1]) <= 35:
                twenty_five_thirty_five_age_math114counter += 1
            elif int(y[1]) <= 45:
                thirty_five_forty_five_age_math114counter += 1
            elif int(y[1]) > 45:
                over_forty_five_age_math114counter += 1

    data['Age Group'] = ['18 - 25', '25 - 35', '35 - 45', 'over 45']
    data['Frequency'] = [eighteen_twenty_five_age_math114counter, twenty_five_thirty_five_age_math114counter, thirty_five_forty_five_age_math114counter, over_forty_five_age_math114counter]
    # Creating a DataFrame from the frequency table data
    frequency_table_df = pd.DataFrame(data)
    heading = "Math114 Student Age "
    print(heading)
    print(frequency_table_df.to_string(index=False))

# 2.1.2 b) Create frequency table showing student ages of CS114 Students
def freq_student_ages_cs114():
    data = {}
    eighteen_twenty_five_age_cs114counter = 0
    twenty_five_thirty_five_age_cs114counter = 0
    thirty_five_forty_five_age_cs114counter = 0
    over_forty_five_age_cs114counter = 0
    with open('student_data_cs114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if int(y[1]) <= 25:
                eighteen_twenty_five_age_cs114counter += 1
            elif int(y[1]) <= 35:
                twenty_five_thirty_five_age_cs114counter += 1
            elif int(y[1]) <= 45:
                thirty_five_forty_five_age_cs114counter += 1
            elif int(y[1]) > 45:
                over_forty_five_age_cs114counter += 1

    data['Age Group'] = ['18 - 25', '25 - 35', '35 - 45', 'over 45']
    data['Frequency'] = [eighteen_twenty_five_age_cs114counter, twenty_five_thirty_five_age_cs114counter, thirty_five_forty_five_age_cs114counter, over_forty_five_age_cs114counter]
    # Creating a DataFrame from the frequency table data
    frequency_table_df = pd.DataFrame(data)
    heading = "CS114 Students Age "
    print(heading)
    print(frequency_table_df.to_string(index=False))

# 2.1.3 a) Create frequency table showing Student marks of Math114 Students
def freq_student_marks_math114():
    data = {}
    under_forty_five_math114 = 0
    forty_five_forty_nine_math114 = 0
    fifty_fifty_nine_math114 = 0
    sixty_sixty_nine_math114 = 0
    seventy_seventy_nine_math114 = 0
    over_eighty_math114 = 0

    with open('student_data_math114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if ((float(y[3]))/130)*100 < 45:
                under_forty_five_math114 += 1
            elif ((float(y[3]))/130)*100 < 50:
                forty_five_forty_nine_math114 += 1
            elif ((float(y[3]))/130)*100 < 60:
                fifty_fifty_nine_math114 += 1
            elif ((float(y[3]))/130)*100 < 70:
                sixty_sixty_nine_math114 += 1
            elif ((float(y[3]))/130)*100 < 80:
                seventy_seventy_nine_math114 += 1
            elif ((float(y[3]))/130)*100 >= 80:
                over_eighty_math114 += 1

    data['Mark'] = ['under 45', '45 - 49', '50 - 59', '60 - 69', '70 - 79', 'over 80']
    data['Frequency'] = [under_forty_five_math114, forty_five_forty_nine_math114, fifty_fifty_nine_math114, sixty_sixty_nine_math114, seventy_seventy_nine_math114, over_eighty_math114]
    # Creating a DataFrame from the frequency table data
    frequency_table_df = pd.DataFrame(data)
    heading = "Math114 Student Marks "
    print(heading)
    print(frequency_table_df.to_string(index=False))

# 2.1.3 b) Create frequency table showing Student marks of CS114 Students
def freq_student_marks_cs114():
    data = {}
    under_forty_five_cs114 = 0
    forty_five_forty_nine_cs114 = 0
    fifty_fifty_nine_cs114 = 0
    sixty_sixty_nine_cs114 = 0
    seventy_seventy_nine_cs114 = 0
    over_eighty_cs114 = 0

    with open('student_data_cs114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if ((float(y[3]))/130)*100 < 45:
                under_forty_five_cs114 += 1
            elif ((float(y[3]))/130)*100 < 50:
                forty_five_forty_nine_cs114 += 1
            elif ((float(y[3]))/130)*100 < 60:
                fifty_fifty_nine_cs114 += 1
            elif ((float(y[3]))/130)*100 < 70:
                sixty_sixty_nine_cs114 += 1
            elif ((float(y[3]))/130)*100 < 80:
                seventy_seventy_nine_cs114 += 1
            elif ((float(y[3]))/130)*100 >= 80:
                over_eighty_cs114 += 1

    data['Mark'] = ['under 45','45 - 49','50 - 59','60 - 69','70 - 79','over 80']
    data['Frequency'] = [under_forty_five_cs114, forty_five_forty_nine_cs114, fifty_fifty_nine_cs114, sixty_sixty_nine_cs114, seventy_seventy_nine_cs114, over_eighty_cs114]
    # Creating a DataFrame from the frequency table data
    frequency_table_df = pd.DataFrame(data)
    heading = "CS114 Student Marks "
    print(heading)
    print(frequency_table_df.to_string(index=False))


# 2.2 Using Matplotlib, complete the following:
# 2.2.1 a) Use a bar chart to show the age groups (x) and numbers of Math114 students
def bar_age_group_math114():
    # count how many student in each age range and put in array
    student_age_num = np.array([])
    # counters for number of students in each age group
    eighteen_twenty_five_age_math114counter = 0
    twenty_five_thirty_five_age_math114counter = 0
    thirty_five_forty_five_age_math114counter = 0
    over_forty_five_age_math114counter = 0
    with open('student_data_math114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            line_info = line.split(',')
            if 18 <= int(line_info[1]) < 25:
                eighteen_twenty_five_age_math114counter += 1
            elif 25 <= int(line_info[1]) < 35:
                twenty_five_thirty_five_age_math114counter += 1
            elif 35 <= int(line_info[1]) < 45:
                thirty_five_forty_five_age_math114counter += 1
            elif int(line_info[1]) > 45:
                over_forty_five_age_math114counter += 1

    student_age_num = np.append(student_age_num, eighteen_twenty_five_age_math114counter)
    student_age_num = np.append(student_age_num, twenty_five_thirty_five_age_math114counter)
    student_age_num = np.append(student_age_num, thirty_five_forty_five_age_math114counter)
    student_age_num = np.append(student_age_num, over_forty_five_age_math114counter)

    x = np.array(['18 - 25', '25 - 35', '35 - 45', 'over 45'])
    y = student_age_num

    # labelling x-axis and y-axis
    plt.xlabel('Age Group')
    plt.ylabel('Number of Students')
    # displaying the title
    plt.title("Number of Math114 Students Per Age Group")
    plt.bar(x, y)
    plt.show()

# 2.2.1 b) Use a bar chart to show the age groups (x) and numbers of CS114 students
def bar_age_group_cs114():
    # count how many student in each age range and put in array
    student_age_num = np.array([])
    # counters for number of students in each age group
    eighteen_twenty_five_age_cs114counter = 0
    twenty_five_thirty_five_age_cs114counter = 0
    thirty_five_forty_five_age_cs114counter = 0
    over_forty_five_age_cs114counter = 0
    with open('student_data_cs114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            line_info = line.split(',')
            if 18 <= int(line_info[1]) < 25:
                eighteen_twenty_five_age_cs114counter += 1
            elif 25 <= int(line_info[1]) < 35:
                twenty_five_thirty_five_age_cs114counter += 1
            elif 35 <= int(line_info[1]) < 45:
                thirty_five_forty_five_age_cs114counter += 1
            elif int(line_info[1]) > 45:
                over_forty_five_age_cs114counter += 1

    student_age_num = np.append(student_age_num, eighteen_twenty_five_age_cs114counter)
    student_age_num = np.append(student_age_num, twenty_five_thirty_five_age_cs114counter)
    student_age_num = np.append(student_age_num, thirty_five_forty_five_age_cs114counter)
    student_age_num = np.append(student_age_num, over_forty_five_age_cs114counter)

    x = np.array(['18 - 25', '25 - 35', '35 - 45', 'over 45'])
    y = student_age_num

    # labelling x-axis and y-axis
    plt.xlabel('Age Group')
    plt.ylabel('Number of Students')
    # displaying the title
    plt.title("Number of CS114 Students Per Age Group")
    plt.bar(x, y)
    plt.show()



# 2.2.2 a) Use a line graph to show if there is a correlation between higher Math114 marks(y) and more time spent on campus studying(x).
# variables to store num of student in each time category
def line_marks_study_hrs_math114():
    num_students_one_math114 = 0
    num_students_two_math114 = 0
    num_students_three_math114 = 0
    num_students_four_math114 = 0

    sum_grades_one_math114 = 0
    sum_grades_two_math114 = 0
    sum_grades_three_math114 = 0
    sum_grades_four_math114 = 0

    # get average study hours for each group
    with open('student_data_math114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if float(y[2]) < 2:
                # get percentage of each student's mark, then add it to grades_students_one_two_math114
                sum_grades_one_math114 = sum_grades_one_math114 + (int(y[3]) / 130) * 100
                num_students_one_math114 += 1
            elif float(y[2]) < 3:
                sum_grades_two_math114 = sum_grades_two_math114 + (int(y[3]) / 130) * 100
                num_students_two_math114 += 1
            elif float(y[2]) < 4:
                sum_grades_three_math114 = sum_grades_three_math114 + (int(y[3]) / 130) * 100
                num_students_three_math114 += 1
            elif float(y[2]) <= 5:
                sum_grades_four_math114 = sum_grades_four_math114 + (int(y[3]) / 130) * 100
                num_students_four_math114 += 1

    avg_one_math114 = sum_grades_one_math114 / num_students_one_math114
    avg_two_math114 = sum_grades_two_math114 / num_students_two_math114
    avg_three_math114 = sum_grades_three_math114 / num_students_three_math114
    avg_four_math114 = sum_grades_four_math114 / num_students_four_math114

    x = np.array(['1 - 2', '2 - 3', '3 - 4', '4 - 5'])
    y = np.array([avg_one_math114, avg_two_math114, avg_three_math114, avg_four_math114])

    plt.plot(x, y)
    # labelling x-axis and y-axis
    plt.xlabel('Time Spent on Campus Studying')
    plt.ylabel('Student Marks')
    # displaying the title
    plt.title('Math114 Student Marks and Time Spent on Campus Studying')
    plt.show()

#2.2.2 b) Use a line graph to show if there is a correlation between higher CS114 marks(y) and more time spent on campus(x).
def line_marks_study_hrs_cs114():
    num_students_one_cs114 = 0
    num_students_two_cs114 = 0
    num_students_three_cs114 = 0
    num_students_four_cs114 = 0

    sum_grades_one_cs114 = 0
    sum_grades_two_cs114 = 0
    sum_grades_three_cs114 = 0
    sum_grades_four_cs114 = 0

    # get average study hours for each group
    with open('student_data_cs114.csv', mode='r', newline='') as f:
        f.readline()
        for i in range(150):
            line = f.readline()
            y = line.split(',')
            if float(y[2]) < 2:
                # get percentage of each student's mark, then add it to grades_students_one_two_math114
                sum_grades_one_cs114 = sum_grades_one_cs114 + (float(y[3]) / 130) * 100
                num_students_one_cs114 += 1
            elif float(y[2]) < 3:
                sum_grades_two_cs114 = sum_grades_two_cs114 + (float(y[3]) / 130) * 100
                num_students_two_cs114 += 1
            elif float(y[2]) < 4:
                sum_grades_three_cs114 = sum_grades_three_cs114 + (float(y[3]) / 130) * 100
                num_students_three_cs114 += 1
            elif float(y[2]) < 5:
                sum_grades_four_cs114 = sum_grades_four_cs114 + (float(y[3]) / 130) * 100
                num_students_four_cs114 += 1

# get percentage of each student's mark, then add it to grades_students_one_two_math114
    avg_one_cs114 = sum_grades_one_cs114 / num_students_one_cs114
    avg_two_cs114 = sum_grades_two_cs114 / num_students_two_cs114
    avg_three_cs114 = sum_grades_three_cs114 / num_students_three_cs114
    avg_four_cs114 = sum_grades_four_cs114 / num_students_four_cs114

    x = np.array(['1 - 2', '2 - 3', '3 - 4', '4 - 5'])
    y = np.array([avg_one_cs114, avg_two_cs114, avg_three_cs114, avg_four_cs114])

    plt.plot(x, y)
    # labelling x-axis and y-axis
    plt.xlabel('Time Spent on Campus Studying')
    plt.ylabel('Student Mark')
    # displaying the title
    plt.title('CS114 Student Marks and Time Spent on Campus Studying')
    plt.show()


# 2.2.3 a) Use a scatter chart to plot each student’s mark(y) and the time(x) taken on the Math114 examination, in minutes.
'''
Sort csv file lines asc via bubble sort function
populate x and y numpy arrays 
plot scatter plot 
'''
# sort array by time taken on exam
def sort_array(array):
    # bubble sort
    for first_idx, first_item in enumerate(array):
        for second_idx, second_item in enumerate(array):
            if int(array[first_idx][4]) < int(array[second_idx][4]):
                # TODO: make sort make sense
                smaller = array[second_idx]
                bigger = array[first_idx]
                array[first_idx] = smaller
                array[second_idx] = bigger
    return array
# sort by hours spent on campus studying
def sort_array_by_study_time(array):
    # bubble sort
    for first_idx, first_item in enumerate(array):
        for second_idx, second_item in enumerate(array):
            if float(array[first_idx][2]) < float(array[second_idx][2]):
                # TODO: make sort make sense
                smaller = array[second_idx]
                bigger = array[first_idx]
                array[first_idx] = smaller
                array[second_idx] = bigger
    return array
def scatter_marks_time_math114():
    x = np.array([])  # time taken
    y = np.array([])  # student mark
    new_array = []
    with open('student_data_math114.csv', mode='r', newline='') as file:
        file.readline()
        for line in file:
            stripped_line = line.rstrip('\r\n')
            line_items = stripped_line.split(',')
            new_array.append(line_items)

    # sort array of lines in ascending order by time which is index 4 of each line
    sorted_array = sort_array(new_array)
    for sorted_item in sorted_array:
        # [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]
        x = np.append(x, int(sorted_item[4]))
        y = np.append(y, (float(sorted_item[3])/130) * 100)

    plt.scatter(x, y)
    # labelling x-axis and y-axis
    plt.xlabel('Time Spent On Exam')
    plt.ylabel('Student Mark')
    # # displaying the title
    plt.title('Student Marks and Time spent on Math114 Exam')
    plt.show()

# 2.2.3 b) Use a scatter chart to plot each student’s mark(y) and the time(x) taken on the CS114 examination, in minutes.
def scatter_marks_time_cs114():
    x = np.array([])  # time taken
    y = np.array([])  # student mark
    new_array = []
    with open('student_data_cs114.csv', mode='r', newline='') as file:
        file.readline()
        for line in file:
            stripped_line = line.rstrip('\r\n')
            line_items = stripped_line.split(',')
            new_array.append(line_items)

    # sort array of lines in ascending order by time which is index 4 of each line
    sorted_array = sort_array(new_array)
    for sorted_item in sorted_array:
        # [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]
        x = np.append(x, int(sorted_item[4]))
        y = np.append(y, (float(sorted_item[3]) / 130) * 100)

    plt.scatter(x, y)
    # labelling x-axis and y-axis
    plt.xlabel('Time Spent On Exam')
    plt.ylabel('Student Mark')
    # # displaying the title
    plt.title('Student Marks and Time spent on CS114 Exam')
    plt.show()

#2.2.4 a)  Use a scatter chart to plot the relationship between time spent on campus(y)and age of Math114 students.
def scatter_study_time_age_math114():
    x = np.array([])
    y = np.array([])
    new_array = []
    with open('student_data_math114.csv', mode='r', newline='') as f:
        f.readline()
        for line in f:
            stripped_line = line.rstrip('\r\n')
            line_items = stripped_line.split(',')
            new_array.append(line_items)

            # sort array of lines in ascending order by time which is index 2 of each line
            sorted_array = sort_array_by_study_time(new_array)
            for sorted_item in sorted_array:
                # [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]
                x = np.append(x, float(sorted_item[1]))
                y = np.append(y, float(sorted_item[2]))

    plt.scatter(x, y)
    #labelling x-axis and y-axis
    plt.xlabel('Student Age')
    plt.ylabel('Time Spent Studying on Campus')
    # displaying the title
    plt.title('Time Spent on Studying on Campus and Ages of Math114 students')
    plt.show()

# 2.2.4 b)  Use a scatter chart to plot the relationship between time spent on campus(y)and age of CS114 students.
def scatter_study_time_age_cs114():
    x = np.array([])  # time spent
    y = np.array([])
    new_array = []
    with open('student_data_cs114.csv', mode='r', newline='') as f:
        f.readline()
        for line in f:
            stripped_line = line.rstrip('\r\n')
            line_items = stripped_line.split(',')
            new_array.append(line_items)

            # sort array of lines in ascending order by time which is index 2 of each line
            sorted_array = sort_array_by_study_time(new_array)
            for sorted_item in sorted_array:
                # [student_number, age_group, hours_studying, student_mark, time_taken_on_exam]
                x = np.append(x, float(sorted_item[1]))
                y = np.append(y, float(sorted_item[2]))

    plt.scatter(x, y)
    #labeling x-axis and y-axis
    plt.xlabel('Student Age')
    plt.ylabel('Time Spent Studying on Campus')
    # displaying the title
    plt.title('Time Spent on Studying on Campus and Ages of CS114 students')
    plt.show()