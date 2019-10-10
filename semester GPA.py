# Semester GPA Calculation

def convertGrade(grade):
    if grade == 'F':
        return 0
    else:
        return 4 - (ord(grade) - ord('A'))

def getGrades():
    semester_info = []
    more_grades = True
    empty_str = ''

    while more_grades:
        course_grade = input('Enter grade (hit Enter if done): ')
        while course_grade not in ('A','B','C','D','F',empty_str):
            course_grade = input('Enter letter grade received: ')

        if course_grade == empty_str:
            more_grades = False
        else:
            num_credits = int(input('Enter number of credits: '))
            semester_info.append([num_credits, course_grade])

    return semester_info
        
def calculateGPA(sem_grades_info, cumulative_gpa_info):
    sem_quality_pts = 0
    sem_credits = 0
    current_cumulative_gpa, total_credits = cumulative_gpa_info

    for k in range(len(sem_grades_info)):
        num_credits, letter_grade = sem_grades_info[k]
        
        sem_quality_pts = sem_quality_pts + \
                          num_credits * convertGrade(letter_grade)
        
        sem_credits = sem_credits + num_credits

    sem_gpa = sem_quality_pts / sem_credits
    new_cumulative_gpa = (current_cumulative_gpa * total_credits +\
             sem_gpa * sem_credits) / (total_credits + sem_credits)
                   
    return (sem_gpa, new_cumulative_gpa)

# ---- main

# program greeting
print('This program calculates semester and cumulative GPAs\n')

# get current GPA info
total_credits = int(input('Enter total number of earned credits: '))
cumulative_gpa = float(input('Enter your current cumulative GPA: '))
cumulative_gpa_info = (cumulative_gpa, total_credits)

# get current semester grade info
print()
semester_grades = getGrades()

# calculate semester gpa and new cumulative gpa
semester_gpa, cumulative_gpa = calculateGPA(semester_grades, \
                               cumulative_gpa_info)

# display semester gpa and new cumulative gpa
print('\nYour semester GPA is', format(semester_gpa, '.2f'))
print('Your new cumulative GPA is', format(cumulative_gpa, '.2f'))
print(convertGrade('E'))

print(convertGrade('E'))

print(convertGrade('E'))

print(convertGrade('E'))

print(convertGrade('E'))








