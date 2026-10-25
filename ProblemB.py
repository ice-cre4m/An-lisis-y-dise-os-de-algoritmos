def main():
    C = int(input()) #casos de prueba
    for _ in range(C):
        listNumbers = list(map(int, input().split()))
        N = listNumbers.pop(0)
        listNumbers = [0] + listNumbers
        if N == 1:
            print(listNumbers[0])
            continue
        if N == 0:
            print(0)
            continue
        maximaGananciaPulgada = [0] * N
        minimaGananciaPulgada = [float('inf')] * N
        maximaGananciaPulgada[0] = listNumbers[0]
        minimaGananciaPulgada[0] = listNumbers[0]
        for pulgada in range(1, N-1):
            sumaHastaI = 0
            for j in range(1, pulgada):
                sumaHastaI += listNumbers[j]
                
            if sumaHastaI > listNumbers[pulgada]:
                maximaGananciaPulgada[pulgada] = sumaHastaI
                minimaGananciaPulgada[pulgada] = listNumbers[pulgada]

            else:
                maximaGananciaPulgada[pulgada] = listNumbers[pulgada]
                minimaGananciaPulgada[pulgada] = sumaHastaI

        print(min(minimaGananciaPulgada), max(maximaGananciaPulgada))






if __name__ == "__main__":
    main()