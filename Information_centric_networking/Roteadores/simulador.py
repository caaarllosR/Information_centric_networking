import heapq as hq
import random as rdm
from datetime import datetime

# Comeco da inicializacao do Simulador

# Fila de Eventos
evento = []
filaEventos = []
rdm.seed(datetime.now())
temporizador_simulador = 0

# Parametros
lambdaRoteador = 1/2
maxPulosRandomWalk = 3
probEncontrarConteudoRoteador = 0.7
numPulosRandomWalk = 0
numEventos = 5

# Inicializacao da fila de eventos

for i in range(0,numEventos) :
    hq.heappush(filaEventos, [rdm.expovariate(lambdaRoteador),'Chegada ao Roteador', numPulosRandomWalk, 'requisicaoConteudo'+str(i+1)])



# Termino da inicializacao do Simulador

while(len(filaEventos)>0) :
    filaEventos.sort()
    print('\n-----------------------------------------------------------\nfilaEventos: ', filaEventos, '\n')  # Log para teste

    evento = hq.heappop(filaEventos)

    print(evento[3]) #Log para teste

    if evento[2]>maxPulosRandomWalk :
        print('Chegada ao Servidor')
        print('Tempo da total da', evento[3], ': ', evento[0])  # Log para teste

    else :
        print('Pulo ',evento[2]) #Log para teste

        print(evento[1])
        temporizador_simulador += evento[0]

        if rdm.random() <= probEncontrarConteudoRoteador :
            print('Conteudo encontrado no Roteador')
            print('Tempo da total da',evento[3], ': ', evento[0])  # Log para teste

        else:
            evento[2]+= 1
            evento[0] += rdm.expovariate(lambdaRoteador)
            print('Conteudo nao encontrado no Roteador')
            print('Tempo da nova requisicao  ', evento[0])  # Log para teste
            hq.heappush(filaEventos,evento)
else:
    print('\n',"O loop while foi encerrado com sucesso!")
