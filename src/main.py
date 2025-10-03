
print("=-"*30)
print(f"{"CONVERSOR DE MOEDAS":^60}")
print("=-"*30)

def main():
    ops = ["Dólar", "Real", "Euro"]
    print("-="*20)
    moeda_sem_conversao = float(input("Digite a moeda do valor que deseja converter: "))
    for n, op in enumerate(ops):
        print(f"[{n + 1}] {op}")
    moeda_atual = input("Agora digite em qual moeda está o valor: ")
    moeda_para_converter = int(input("Agora digite para qual moeda que deseja converter: "))
    breakpoint()
    match moeda_para_converter:
        case 1:#converte para dólar
            if moeda_atual == ops[1] or 2: #converte do real
                result = moeda_sem_conversao / 5
                print(result)
            if moeda_atual == ops[2] or 3: #converte do euro
                result = moeda_sem_conversao * 1.17
                print(result)
        case 2:#converte para real
                result = moeda_sem_conversao * 5
                print(result)
        case 3:#converte para euro
            ...

if __name__ =="__main__":
    main()