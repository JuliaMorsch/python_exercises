# Algorithm to calculate the discount on a product

# Receive the product value
value = float(input("Informe o valor do produto que você deseja comprar: "))

# Receive the discount percentage
discount_per = int(input("Informe o percentual de desconto: "))

#  Evaluates if the percentage is valid

if discount_per < 0 or discount_per > 100:
    print("Informe um percentual válido")
else:
    discount = value * (discount_per / 100)

final_value = value - discount

print(f"O valor final do produto é R$ {final_value:.2f}")
