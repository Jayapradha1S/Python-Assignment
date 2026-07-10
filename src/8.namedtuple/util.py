from collections import namedtuple

def calculate_average(n, column):
    Student = namedtuple("Student", column)

    sum = 0

    for i in range(n):
        ls = input().split()
        st = Student(*ls)
        sum += int(st.MARKS)

    avg = sum / n
    return avg