"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
41266, Diogo Simões
43464, Cristiano Santos

"""
from math import floor
from objectManager import Objects
from enviroment import Enviroment
from robot import Robot
from zone import Zone


def work(posicao, bateria, objetos) -> None:
    """
    Esta função é invocada em cada ciclo de clock e pode servir para armazenar 
    informação recolhida pelo agente

    Podem achar o tempo atual usando, p.ex. `time.time()`
    
    Args:
        posicao (list of int): A posição atual do agente, uma lista [X,Y]
        bateria (int): Valor de energia na bateria, um número inteiro >= 0
        objetos (list of string): Nome do(s) objeto(s) próximos do agente, uma string
    """
    posicao = tuple(posicao)
    # Se a bateria for 0 o robot para de recolher dados
    if bateria:
        Robot.updateRobot(posicao, bateria)
        Enviroment.update(posicao, objetos)

	
def resp1():
    """Qual foi a penúltima pessoa do sexo feminino que viste?"""
    try:
        print(Objects.getPenultSawFemale())
    except Objects.NotEnoughFemalesException as e:
        print(e.what())

def resp2():
    """Em que tipo de zona estás agora?"""
    try:
        print(Enviroment.getCurrentZone().getType())
    except Zone.ZoneNotDefinedException as e:
        print(e.what())
    

def resp3():
    """Qual o caminho para a papelaria?"""
    pass


def resp4():
    """Qual a distância até ao talho?"""
    pass


def resp5():
    """Quanto tempo achas que demoras a ir de onde estás até à caixa?"""
    try:
        # 1o: TODO: calcular distancia
        distancia = 0
        
        # 2o: calcular o tempo previsto usando a distancia
        timeP = Robot.predictTimeFromDistance(distancia)
        
        print(f"O robot prevê a possibilidade de demorar-mos ao precorrer {distancia} de distancia em {timeP}s\n")
    except Robot.NotAvailablePrediction as e:
        print(e.what())


def resp6():
    """
    Quanto tempo achas que falta até ficares com metade da bateria que tens 
    agora?
    """
    # TODO FIND FUCKING BUG
    try:
        halfBattery = floor(Robot.getCurrentBattery()/2)
        pTime = Robot.predictTimeFromBattery(halfBattery)
        
        print(f"O robot prevê a possibilidade de chegarmos ao nivel de bateria '{halfBattery}' daqui a {pTime:04f}s\n")
    except Robot.NotAvailablePrediction as e:
        print(e.what())

    
    

def resp7():
    """Qual é a probabilidade da próxima pessoa a encontrares ser uma criança?"""
    pass

def resp8():
    """
    Qual é a probabilidade de encontrar um adulto numa zona se estiver lá uma
    criança mas não estiver lá um carrinho?
    """
    pass
