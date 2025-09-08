# Create a code that receives a person's age and indicates the movie they can watch according to their age

age = int(input(" Digite a sua idade:"))

if age < 12:
    print("Você pode assistir ao filme Lilo & Stich")
elif age >= 12 and age < 18:
    print("Você pode assitir ao filme Super Mario Bros")
else:
    print("Você pode assistir ao filme Invocação do Mal 4")

# Tickets for movies:
qtd_tickets = 0
if qtd_tickets > 0:
    print("Você pode comprar um ingresso para assistir ao seu filme")
elif qtd_tickets == 0:
    ("Não há mais ingressos disponíveis para o seu filme")