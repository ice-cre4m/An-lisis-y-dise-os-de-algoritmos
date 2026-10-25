def main():
    t = int(input()) # test cases
    for _ in range(t):
        arr = []
        N = int(input()) # number of elements
        for _ in range(N):
            arr.append(int(input()))
        acumuladoMaxIzqInmediata = 0
        acumuladoMaxAnterior = 0
        acumuladoMaximo = 0
        if len(arr) == 0:
            print(0)
            continue
        if len(arr) == 1:
            print(arr[0])
            continue
        acumuladoMaxIzqInmediata = arr[0]
        for i in range(1, len(arr)):
            #hay un acumulado para dos casillas anteiroes, uno para la casilla actual
            #si estoy en el dos [1,2,31,23,1,2,3,4,3,24,3]
            # debo comparar lo que tenia hace dos iteraciones y lo que tengo en esta iteracion sumando mi elemetno
            if acumuladoMaxAnterior + arr[i] > acumuladoMaxIzqInmediata:
                acumuladoMaximo = acumuladoMaxAnterior + arr[i]
                acumuladoMaxAnterior = acumuladoMaxIzqInmediata
                acumuladoMaxIzqInmediata = acumuladoMaximo
            else:
                acumuladoMaximo = acumuladoMaxIzqInmediata
                acumuladoMaxAnterior = acumuladoMaxIzqInmediata

        print(acumuladoMaximo)









        

        
        



if __name__ == "__main__":
    main()


"""
El jugador puede tomar o saltar una casilla
se debe maximizar el acumulado
tomar si ya se tomo antes resta el valor a la izquierda que se tomo

"""