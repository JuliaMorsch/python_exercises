# Algorithm to calculate the media of grades for a student

grades = [7.5, 6.0, 8.0, 9.5, 5.0]

def calculate_avg(grades):
    sum_grades = sum(grades)
    avg = sum_grades / len(grades)
    return avg

# Lambda function that round the avarage to two decimal places

round_avg = lambda media: round(media, 2)

# Calaculate media of grades and print the result

media = calculate_avg(grades)
media_avg = round_avg(media)

# Check the students' situation

situation = "Aprovado" if media_avg >= 7 else "Reprovado"
