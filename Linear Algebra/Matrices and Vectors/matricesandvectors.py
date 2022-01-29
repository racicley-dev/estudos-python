from numpy import *

def criar_matriz():
    r = int(input('Número de linhas. Digite um número.\n'))
    c = int(input('Número of colunas. Digite um número.\n'))
    Matrix = zeros((r,c)) 
    for linha in range(int(r)):
        for coluna in range(int(c)):
            Matrix[linha, coluna] = input('Insira o elemento a['+str(linha)+','+str(coluna)+'] = ')
        
    return Matrix


def criar_vetor():
    vz = int(input('Insira o tamanho do vetor.\n'))
    Vector = zeros((vz))

    for e in range(int(vz)):
        Vector[e] = input('Insira o elemento a['+ str(e) +'] = ')

    return Vector

def monta():
    tipo = input('Insira M para Matriz ou V para Vetor:\n')
    if tipo == 'M':
        return (criar_matriz(),'M')
    else:
        return (criar_vetor(),'V')


def main():
    matriz_vetor = monta()

    print(matriz_vetor[0])

    #vectors
    #v = array([1.,2.,3.])

    # two vectors with three components
    #v1 = array([1., 2., 3.])
    #v2 = array([2, 0, 1.])

    # scalar multiplications/divisions
    #2*v1 # array([2., 4., 6.])
    #v1/2 # array([0.5, 1., 1.5])

    #print(v,v1,v2)

if __name__ == "__main__":
    main()