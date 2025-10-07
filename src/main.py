
print("=-"*30)
print(f"{"CONVERSOR DE MOEDAS":^60}")
print("=-"*30)

def main():
    ops = ["DÓLAR", "REAL", "EURO"]
    print("-="*20)
    moeda_sem_conversao = float(input("Digite o valor que possue para converter: "))
    for n, op in enumerate(ops):
        print(f"[{n + 1}] {op}")
    moeda_atual = input("Qual sua moeda atual: ").upper()

    moeda_para_converter = int(input("Agora digite para qual moeda deseja converter: "))
    match moeda_para_converter:
        case 1:#converte para dólar
            # breakpoint()
            if moeda_atual == ops[1] or moeda_atual == '2': #se a moeda atual for real
                result = moeda_sem_conversao / 5
                print(result)
            elif moeda_atual == ops[2] or moeda_atual == '3': #se a moeda atual for euro
                result = moeda_sem_conversao * 1.17
                print(result)
        case 2:#converte para real
                result = moeda_sem_conversao * 5
                print(result)
        case 3:#converte para euro
            ...
    print("Penis")
if __name__ =="__main__":
    main()