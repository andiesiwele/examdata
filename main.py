import examdata
obj = examdata

menu = "=========================================================" + "\n"
menu = menu + "|                 VIDEO STORE                           |" + "\n"
menu = menu + "=========================================================" + "\n"
menu = menu + "| 1. Generate Toy Math114 Exam Data                                   |" + "\n"
menu = menu + "| 2. Generate Toy CS114 Exam Data                                      |" + "\n"
menu = menu + "=========================================================" + "\n"
menu = menu + "| 3. Generate Frequency Tables                                   |" + "\n"
menu = menu + "| 4. Generate Bar Graphs                                         |" + "\n"
menu = menu + "| 5. Generate Line Graphs                                         |" + "\n"
menu = menu + "| 6. Generate Scatter Plots                                          |" + "\n"
menu = menu + "=========================================================" + "\n"
menu = menu + "| X. Exit                                                |" + "\n"
menu = menu + "=========================================================" + "\n"
menu = menu + "Choice:_"


def main():
    possible_answers = [1, 2, 3, 4, 5]
    answer = input(menu)
    if int(answer) == 1:
        obj.generate_math_exam_data()
    if int(answer) == 2:
        obj.generate_cs_exam_data()
    if int(answer) == 3:
        obj.freq_avg_study_hrs_math114()
        obj.freq_avg_study_hrs_cs114()
        obj.freq_student_ages_math114()
        obj.freq_student_ages_cs114()
        obj.freq_student_marks_math114()
        obj.freq_student_marks_cs114()
    if int(answer) == 4:
        obj.bar_age_group_math114()
        obj.bar_age_group_cs114()
    if int(answer) == 5:
        obj.line_marks_study_hrs_math114()
        obj.line_marks_study_hrs_cs114()
    if int(answer) == 6:
        obj.scatter_marks_time_math114()
        obj.scatter_marks_time_cs114()
        obj.scatter_study_time_age_math114()
main()