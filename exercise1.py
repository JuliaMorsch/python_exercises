# Create a code that receives a person's age and indicates the movie they can watch according to their age

# Bem-vindo à Máquina de Venda Automática de Ingressos de Cinema!

# Solicita a idade do cliente
age = int(input(" Digite a sua idade:"))

# Verifica a idade para sugerir os filmes
if age < 12:
    print("Você pode assistir ao filme Lilo & Stich")
elif age >= 12 and age < 18:
    print("Você pode assitir ao filme Super Mario Bros")
else:
    print("Você pode assistir ao filme Invocação do Mal 4")

# Tickets for movies:

#Verifica a disponibilidade de ingressos
qtd_tickets = 10
if qtd_tickets > 0:
    print("Você pode comprar um ingresso para assistir ao seu filme")
elif qtd_tickets == 0:
    print("Não há mais ingressos disponíveis para o seu filme")