"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
41266, Diogo Simões
43464, Cristiano Santos

"""
import networkx as nx
from math import floor

from constant import *
from objectManager import Objects
from enviroment import Enviroment
from robot import Robot
from utils import Utils
from zone import Zone
import networkx as nx
import matplotlib.pyplot as plt


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
        nx.draw_random(Enviroment._zoneMap, with_labels=True)
        plt.savefig("map2.png")
        plt.clf()
        nx.draw_random(Enviroment._infoMap, with_labels=True)
        plt.savefig("map4.png")
        plt.clf()
        nx.draw_circular(Enviroment._zoneMap, with_labels=True)
        plt.savefig("map3.png")
        plt.clf()

    except Objects.NotEnoughFemalesException as e:
        print(e.what())


def resp2():
    """Em que tipo de zona estás agora?"""
    try:
        print(Enviroment.getCurrentZone().getType())
    except Zone.ZoneNotDefinedException as e:
        print("Corredor" if Enviroment.indexOfCurrentZone() in range(6) else e.what())


def resp3():
    """Qual o caminho para a papelaria?"""
    #Atençao ---- MOfificar a funçao pathDescription
    '''Determina se a papelaria ja foi encontrada até ao momento '''
    try:
        # Adicionamos o robo ao grafo
        Enviroment.addRobotToGraph()
        
        bixo = None
        for node in list(Enviroment._infoMap.nodes(data = True)):
            try:
                if "papelaria" == Enviroment.getTypeOfZone(node[0]):
                    bixo = node
            except Zone.ZoneNotDefinedException as e:
                continue
        
        if not bixo:
            raise nx.NodeNotFound()
        
        
        path = nx.astar_path(
            Enviroment._zoneMap,
            Enviroment._map["ROBOT"], 
            Enviroment.zoneToString(bixo[0])
        )
        
        if Enviroment.getCurrentZone() == node[0]:
            path = Enviroment.zoneToString(bixo[0])
            print("Já se encontra na papelaria")

        # Eliminamos o robo do grafo
        Enviroment.delRobotFromGraph()
        print(f"Resposta: O caminho até a papelaria é : {Utils.pathDescription(path)}\n")
    except nx.NodeNotFound as e:
        print("Ainda não foi encontrado o objetivo")
    pass

    pass


def resp4():
    """Qual a distância até ao talho?"""
    try:
        # Adicionamos o robo ao grafo
        Enviroment.addRobotToGraph()
        
        bixo = None
        for node in list(Enviroment._infoMap.nodes(data = True)):
            try:
                if "talho" == Enviroment.getTypeOfZone(node[0]):
                    bixo = node
            except Zone.ZoneNotDefinedException as e:
                continue
        
        if not bixo:
            raise nx.NodeNotFound()
        
        print(
            nx.astar_path(
                Enviroment._zoneMap, 
                Enviroment._map["ROBOT"], 
                Enviroment.zoneToString(bixo[0])
            )
        )
        
        weight = nx.astar_path_length(
            Enviroment._zoneMap,
            Enviroment._map["ROBOT"], 
            Enviroment.zoneToString(bixo[0])
        )
        
        if Enviroment.getCurrentZone() == node[0]:
            weight = 0
        
        # Eliminamos o robo do grafo
        Enviroment.delRobotFromGraph()
        print(f"Resposta: Distancia até ao talho = {weight}\n")
    except nx.NodeNotFound:
        print("Ainda não foi encontrado o objetivo")


def resp5():
    """Quanto tempo achas que demoras a ir de onde estás até à caixa?"""
    try:
        # Adicionamos o robo ao grafo
        Enviroment.addRobotToGraph()
        
        bixo = None
        nodeInfo = list(Enviroment._infoMap.nodes(data = True))
        for node in nodeInfo:
            if OBJ["CASHIER"] in node[1]:
                bixo = node
        
        if not bixo:
            raise nx.NodeNotFound()
        
        
        weight = nx.astar_path_length(
            Enviroment._zoneMap,
            Enviroment._map["ROBOT"], 
            Enviroment.zoneToString(bixo[0])
        )
        
        # Eliminamos o robo do grafo
        Enviroment.delRobotFromGraph
        print(f"Resposta: {Utils.timeToStr(Robot.predictTimeFromDistance(weight))}\n")
    except Robot.NotAvailablePrediction as e:
        print(e.what())
    except nx.NodeNotFound as e:
        print("Ainda não foi encontrado o objetivo")

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
    try:
        print(Enviroment.getProbabilityOfNextPersonBeAChild())
    except ZeroDivisionError:
        print("Ainda não foram encontrados elementos consideraveis suficientes para a estatistica.")


def resp8():
    """
    Qual é a probabilidade de encontrar um adulto numa zona se estiver lá uma
    criança mas não estiver lá um carrinho?
    """
    try:
        print(Enviroment.getProbabilityOfAdultInZoneIfThereIsChildButNoShopcar())
    except ZeroDivisionError:
        print("Ainda não foi encontrado nenhum elemento consideravel na estatistica.")
