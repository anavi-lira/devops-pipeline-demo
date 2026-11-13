def calcular_total(preco, quantidade):
    return preco * quantidade


if __name__ == "__main__":
    total = calcular_total(50, 3)
    print(f"Total da compra: R$ {total:.2f}")