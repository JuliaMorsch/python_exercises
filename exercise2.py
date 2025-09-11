# Program that lists movies and receives ratings.

# Wellcome message
print("Bem-vindo à classificação de filmes!")
print("Você tem 5 filmes para avaqliar.")
print("Digite 0 a qualquer momento para sair.")

movie = ["filme1", "filme2", "filme3", "filme4", "filme5"]

for mov in movie:
    print(mov)
    rating = int(input(f"Como você avaliaria o {mov} de 1 a 5?:"))
    if rating == 0:
        print("Obrigada por participar!")
        break

