import csv
import numpy as np
import matplotlib.pyplot as plt
# 4.1 Using Python, execute the following requests:
# a. Read the percent-bachelors-degrees-women-usa.csv file as a list of lists. (2 Marks)

# with open("percent-bachelors-degrees-women-usa.csv", "r") as file:
#     BDW = list(csv.reader(file))
# print(BDW)
with open("percent-bachelors-degrees-women-usa.csv", "r") as file:
 # b. Assign the result to the variable BDW. (2 Marks)
 BDW = list(csv.reader(file))

# c. Display the first five rows of BDW separately on different lines. (2 Marks)
for row in BDW[:5]:
    print(row)
# d. Remove the header row (column names) of the dataset and assign the rest of the dataset to BDW1. (2 Marks)
BDW1 = BDW[1:]
# e. Using slicing, display the first, second and third row of BDW1. (2 Marks)
print(BDW1[0])
print(BDW1[1])
print(BDW1[2])


# 4.2 Using for loops in Python, from BDW1, create two dictionaries as instructed below:
# a. A dictionary called “Indexcount_year” where the years are the keys and the values are
# the frequencies of occurrence of each year. (5 Marks)
Indexcount_year = {}
for row in BDW1:
    year = int(row[1])
    if year in Indexcount_year:
        Indexcount_year[year] += 1
    else:
        Indexcount_year[year] = 1
# b. A dictionary called “Indexpercent_year” where the years are the keys and the values
# are the indices of each item in the list. (5 Marks)
Indexpercent_year = {}
for idx, row in enumerate(BDW1):
    year = int(row[1])
    Indexpercent_year[year] = idx
# Note to Student: The index and frequencies should be integers and not strings.

# 4.3 Using for loops in Python, from BDW1, read the following as a list:
# a. The percentages of women who earned a degree per year in the following majors:
# • Math and Statistics. Assign the value to the variable Maths_Stats. (5 Marks)
# • Physical Sciences. Assign the value to the variable Physic_Sci. (5 Marks)
# • Engineering. Assign the value to the variable Engine. (5 Marks)
# • Computer Science. Assign the value to the variable Comp_Sci. (5 Marks)
# Maths_Stats = [float(row[1]) for row in BDW1] #4
# Physic_Sci = [float(row[4]) for row in BDW1] #15
# Engine = [float(row[7]) for row in BDW1] #10
# Comp_Sci = [float(row[11]) for row in BDW1] #8
# # b. The year captured in the dataset as to when these degrees were earned. Assign it to the variable Year. (5 Marks)
# Year = [int(row[0]) for row in BDW1] # 1

Maths_Stats = [float(row[4]) for row in BDW1] #4
Physic_Sci = [float(row[5]) for row in BDW1] #15
Engine = [float(row[10]) for row in BDW1] #10
Comp_Sci = [float(row[8]) for row in BDW1] #8
# b. The year captured in the dataset as to when these degrees were earned. Assign it to the variable Year. (5 Marks)
Year = [int(row[1]) for row in BDW1] # 1

# 4.4 Using the list obtained and its orientation (i.e. I-IV) in 4.3 a:
# a. Create a Numpy array called “Selected4Majors”. Each element in the list must be
# converted to a float before creating the Numpy array. (5 Marks)
Selected4Majors = np.array([Maths_Stats, Physic_Sci, Engine, Comp_Sci], dtype=float)

# b. Create a dictionary called “Majors” where the major is the key and the values are the
# indices of each major, in regards to their orientation. (2 Marks)
Majors = {'Maths_Stats': 0, 'Physic_Sci': 1, 'Engine': 2, 'Comp_Sci': 3}

# 4.5 Write a Python function that will accept two arguments, data and majorlist. Using this
# function, do the following:
# a. With a for loop plot the data in the variable Year, obtained in 4.3 b (x-axis) against the
# data in the variable Selected4Majors (y-axis). This should be done on the same graph. # (5 Marks)

def plot_selected_degrees(Year, Selected4Majors):
    for major in range(Selected4Majors.shape[0]):
        plt.plot(Year, Selected4Majors[major], label=list(Majors.keys())[major])
    # b. Display the legend of the majors for each plot in the upper left corner. (2 Marks)
    plt.legend(loc='upper left')
    # c. Set the title to “Percentage of Selected4Degrees Awarded per Year”, label the x-axis “Year” and the y-axis “Selected4Degrees”. (3 Marks)
    plt.title("Percentage of Selected4Degrees Awarded per Year")
    plt.xlabel("Year")
    plt.ylabel("Selected4Degrees")
    plt.show()

plot_selected_degrees(Year, Selected4Majors)


''''
# 4.6 Based on the plots in 4.5, what can you deduce from the graph?
Based on the graph, we can observe the trends in the percentage of women who earned degrees in different majors 
over the years. Each line represents a different major, and we can see how the percentages have changed over time 
for each of the four majors (Maths & Stats, Physical Sciences, Engineering, and Computer Science).
We can observe if any majors percentage has significantly increased or decreased over the years. Additionally, we can
see if there are any patterns or correlations between the percentages of different majors. Remember that the 
interpretation of the graph may vary depending on the specific trends and data present in the dataset. Further 
statistical analysis and domain knowledge would be needed to draw more concrete conclusions.
'''
