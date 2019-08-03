import math
import os
import random
import re
import sys


def gradingStudents(grades, gradesrem):
    result = []
    for i in range(len(grades)):

        if grades[i] >= 38:
            if gradesrem[i] >= 3:
                result.append(grades[i]+(5 - gradesrem[i]))

            else:
                    result.append(grades[i])
        else:
            result.append(grades[i])
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    gradesrem = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
        gradesrem.append(int(grades[_]%5))
    result = gradingStudents(grades, gradesrem)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

