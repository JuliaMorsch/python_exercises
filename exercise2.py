# Program that lists movies and receives ratings.

movie = ["filme1", "filme2", "filme3", "filme4", "filme5"]

for mov in movie:
    print(mov)
    rating = int(input("Digite a sua avaliação de 1 a 5 (6 para sair):"))
    if rating == 6:
        print("Obrigada por participar!")
        break

