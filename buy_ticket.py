VALOR_KM = 3.50

# Cidades
cidades = {
    1: "Buzios",
    2: "Cabo Frio",
    3: "Arraial do Cabo"
}

# Distâncias entre as cidades
distancias = {
    ("Buzios", "Cabo Frio"): 30,
    ("Cabo Frio", "Buzios"): 30,
    ("Buzios", "Arraial do Cabo"): 40,
    ("Arraial do Cabo", "Buzios"): 40,
    ("Cabo Frio", "Arraial do Cabo"): 10,
    ("Arraial do Cabo", "Cabo Frio"): 10
}

# 40 assentos por rota
rotas = {}

for rota in distancias:
    rotas[rota] = list(range(1, 41))

total_vendas = 0


# Funções

def mostrar_cidades():
    print("\n===== CIDADES DISPONÍVEIS =====")
    for codigo, cidade in cidades.items():
        print(f"{codigo} - {cidade}")


def comprar_passagem():
    global total_vendas

    mostrar_cidades()

    try:
        origem = int(input("\nCidade de origem: "))
        destino = int(input("Cidade de destino: "))
    except ValueError:
        print("\nDigite apenas números!")
        return

    if origem not in cidades or destino not in cidades:
        print("\nCidade inválida!")
        return

    origem = cidades[origem]
    destino = cidades[destino]

    if origem == destino:
        print("\nOrigem e destino não podem ser iguais.")
        return

    rota = (origem, destino)

    if len(rotas[rota]) == 0:
        print("\nNão há mais assentos disponíveis nessa rota.")
        return

    distancia = distancias[rota]
    valor = distancia * VALOR_KM

    print("\n==============================")
    print("       DADOS DA VIAGEM")
    print("==============================")
    print(f"Origem: {origem}")
    print(f"Destino: {destino}")
    print(f"Distância: {distancia} km")
    print(f"Valor da passagem: R$ {valor:.2f}")

    print("\nAssentos disponíveis:")
    print(rotas[rota])

    try:
        assento = int(input("\nEscolha o número do assento: "))
    except ValueError:
        print("\nDigite um número válido.")
        return

    if assento not in rotas[rota]:
        print("\nEsse assento já foi vendido ou não existe.")
        return

    # Reservar o assento
    rotas[rota].remove(assento)

    total_vendas += valor

    print("\n==============================")
    print("   PASSAGEM VENDIDA!")
    print("==============================")
    print(f"Origem: {origem}")
    print(f"Destino: {destino}")
    print(f"Assento: {assento}")
    print(f"Valor pago: R$ {valor:.2f}")
    print(f"Assentos restantes: {len(rotas[rota])}")


def consultar_vendas():
    print("\n==============================")
    print(" TOTAL DE VENDAS")
    print("==============================")
    print(f"Valor arrecadado: R$ {total_vendas:.2f}")


def consultar_assentos():
    print("\n==============================")
    print(" ASSENTOS DISPONÍVEIS")
    print("==============================")

    for rota, lista_assentos in rotas.items():
        print(f"\n{rota[0]} ➜ {rota[1]}")
        print(f"Assentos livres: {len(lista_assentos)}")

        if len(lista_assentos) > 0:
            print(lista_assentos)
        else:
            print("Ônibus lotado!")


# Menu

while True:

    print("\n===================================")
    print("BEM-VINDO!")
    print("===================================")
    print("1 - Comprar passagem")
    print("2 - Consultar vendas")
    print("3 - Consultar assentos")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        comprar_passagem()

    elif opcao == "2":
        consultar_vendas()

    elif opcao == "3":
        consultar_assentos()

    elif opcao == "4":
        print("\nObrigado por viajar conosco!")
        break

    else:
        print("\nOpção inválida!")