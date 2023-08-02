import Question1
import Question2

obj = Question2
generate_data = Question1

menu = "==============================================================" + "\n"
menu = menu + "|                 Exam Data                                   |" + "\n"
menu = menu + "==============================================================" + "\n"
menu = menu + "| 1. Generate Toy Data for Math114 Exam                       |" + "\n"
menu = menu + "| 2. Generate Toy Data for CS114 Exam                         |" + "\n"
menu = menu + "==============================================================" + "\n"
menu = menu + "| 3. Generate Statistical Visualisations for Math114 Exam Data|" + "\n"
menu = menu + "| 4. Generate Statistical Visualisations for CS114 Exam Data  |" + "\n"
menu = menu + "==============================================================" + "\n"
menu = menu + "| X. Exit                                                     |" + "\n"
menu = menu + "==============================================================" + "\n"
menu = menu + "Choice:_"

math_menu = "=========================================================" + "\n"
math_menu = math_menu + "|       Visualisations for Math 114 Exam Data            |" + "\n"
math_menu = math_menu + "=========================================================" + "\n"
math_menu = math_menu + "| 1. Generate Frequency Tables for Math 114 Exam Data    |" + "\n"
math_menu = math_menu + "| 2. Generate Bar Graphs for Math 114 Exam Data          |" + "\n"
math_menu = math_menu + "| 3. Generate Line Graphs for Math 114 Exam Data         |" + "\n"
math_menu = math_menu + "| 4. Generate Scatter Plots for Math 114 Exam Data       |" + "\n"
math_menu = math_menu + "=========================================================" + "\n"
math_menu = math_menu + "| B. Back                                                |" + "\n"
math_menu = math_menu + "| X. Exit                                                |" + "\n"
math_menu = math_menu + "=========================================================" + "\n"
math_menu = math_menu + "Choice:_"

cs_menu = "=========================================================" + "\n"
cs_menu = cs_menu + "|        Visualisations for Computer Science 114 Exam Data         |" + "\n"
cs_menu = cs_menu + "=========================================================" + "\n"
cs_menu = cs_menu + "| 1. Generate Frequency Tables for CS 114 Exam Data     |" + "\n"
cs_menu = cs_menu + "| 2. Generate Bar Graphs for CS 114 Exam Data           |" + "\n"
cs_menu = cs_menu + "| 3. Generate Line Graphs for CS 114 Exam Data          |" + "\n"
cs_menu = cs_menu + "| 4. Generate Scatter Plots for CS 114 Exam Data        |" + "\n"
cs_menu = cs_menu + "=========================================================" + "\n"
cs_menu = cs_menu + "| B. Back                                                |" + "\n"
cs_menu = cs_menu + "| X. Exit                                                |" + "\n"
cs_menu = cs_menu + "=========================================================" + "\n"
cs_menu = cs_menu + "Choice:_"


def main():
    sub_menu = ""
    possible_answers = [1, 2, 3, 4, 5, "X", "x"]
    answer = input(menu)
    if int(answer) == 1:
        genarate_data.generate_math_exam_data()
    elif int(answer) == 2:
        genarate_data.generate_cs_exam_data()
    elif int(answer) == 3:
        sub_menu = input(math_menu)
        # all math114 visualisations
        if answer == "A" or answer == "a":
            obj.freq_student_marks_math114()
            obj.freq_student_ages_math114()
            obj.freq_avg_study_hrs_math114()
            obj.bar_age_group_math114()
            obj.line_marks_study_hrs_math114()
            obj.scatter_marks_time_math114()
            obj.scatter_study_time_age_math114()
        # math114 freq tables
        elif int(sub_menu) == 1:
            obj.freq_student_marks_math114()
            obj.freq_student_ages_math114()
            obj.freq_avg_study_hrs_math114()
        # math114 bar graphs
        elif int(sub_menu) == 2:
            obj.bar_age_group_math114()
        # math114 line graphs
        elif int(sub_menu) == 3:
            obj.line_marks_study_hrs_math114()
        # math114 scatter plots
        elif int(sub_menu) == 4:
            obj.scatter_marks_time_math114()
            obj.scatter_study_time_age_math114()
        # math114 back to main menu
        elif answer == "B" or "b":
            main()
        # terminate program
        elif answer == "X" or "x":
            exit()
        else:
            main()
    if int(answer) == 4:
       sub_menu = input(cs_menu)
       # all math114 visualisations
       if answer == "A" or answer == "a":
           obj.freq_student_marks_cs114()
           obj.freq_student_ages_cs114()
           obj.freq_avg_study_hrs_cs114()
           obj.bar_age_group_cs114()
           obj.line_marks_study_hrs_cs114()
           obj.scatter_marks_time_cs114()
           obj.scatter_study_time_age_cs114()
       # cs114 freq tables
       elif int(sub_menu) == 1:
           obj.freq_student_marks_cs114()
           obj.freq_student_ages_cs114()
           obj.freq_avg_study_hrs_cs114()
       # cs114 bar graphs
       elif int(sub_menu) == 2:
           obj.bar_age_group_cs114()
       # cs114 line graphs
       elif int(sub_menu) == 3:
           obj.line_marks_study_hrs_cs114()
       # cs114 scatter plots
       elif int(sub_menu) == 4:
           obj.scatter_marks_time_cs114()
           obj.scatter_study_time_age_cs114()
       # back to main menu
       elif answer == "B" or "b":
           main()
       # terminate program
       elif answer == "X" or "x":
           exit()
       else:
            main()
    if answer == "X" or "x":
        exit()
    else:
        main()
main()