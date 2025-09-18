# Algorithm to calculate the media of grades for a student

grades = [7.5, 6.0, 8.0, 9.5, 5.0]

def calculate_avg(grades):
    sum_grades = sum(grades)
    avg = sum_grades / len(grades)
    return avg

