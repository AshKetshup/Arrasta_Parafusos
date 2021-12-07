"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
41266, Diogo Simões
43464, Cristiano Santos

"""
from objectManager import Objects
from enviroment import Enviroment
import time


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
    Enviroment.update(posicao, objetos)    
    pass

	
def resp1():
    """Qual foi a penúltima pessoa do sexo feminino que viste?"""
    try:
        print(Objects.getPenultSawFemale())
    except Objects.NotEnoughFemalesException as e:
        print(e.what())

def resp2():
    """Em que tipo de zona estás agora?"""
    pass


def resp3():
    """Qual o caminho para a papelaria?"""
    pass


def resp4():
    """Qual a distância até ao talho?"""
    pass


def resp5():
    """Quanto tempo achas que demoras a ir de onde estás até à caixa?"""    
    pass


def resp6():
    """
    Quanto tempo achas que falta até ficares com metade da bateria que tens 
    agora?
    """    
    pass


def resp7():
    """Qual é a probabilidade da próxima pessoa a encontrares ser uma criança?"""
    pass

def resp8():
    """
    Qual é a probabilidade de encontrar um adulto numa zona se estiver lá uma
    criança mas não estiver lá um carrinho?
    """
    pass
