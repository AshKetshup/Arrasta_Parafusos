import networkx as nx
from networkx.classes.graph import Graph

from constant import *
from robot import Robot
from zone import Zone
from utils import Utils

class Enviroment():
    """Classe responsavel pelo gerenciamento dos grafos e das zonas."""
    _map = {
        "MIDPOINT": "mid",
        "WEIGHT"  : "weight",
        "ROBOT"   :  "X"
    }
    
    # Zonas com suas coordenadas respetivas
    _zones = [
        Zone(( 30, 135), (165, 435)), # 1 
        Zone((135, 285), (165, 285)), # 2 
        Zone((135, 285), (330, 435)), # 3 
        Zone((285, 435), (165, 435)), # 4 
        Zone((435, 770), (165, 285)), # 5 
        Zone((435, 770), (330, 435)), # 6 
        Zone(( 30, 135), ( 30, 135)), # 7 
        Zone((180, 285), ( 30, 135)), # 8 
        Zone((330, 435), ( 30, 135)), # 9 
        Zone((480, 585), ( 30, 135)), # 10
        Zone((630, 770), ( 30, 135)), # 11
        Zone((630, 770), (435, 570)), # 12
        Zone((480, 585), (435, 570)), # 13
        Zone((330, 435), (435, 570)), # 14
        Zone((180, 285), (435, 570)), # 15
        Zone(( 30, 135), (435, 570))  # 16
    ]
    
    _lastVisited = -1     # Indice da última zona visitada
    _currentZone = -1     # Indice da zona onde o robot se encontra atualmente
    
    _zoneMap = nx.Graph() # Grafo da representação das conexões de zonas
    _infoMap = nx.Graph() # Grafo da representação das informações de zonas
    
    
    @staticmethod
    def getZoneMap() -> Graph:
        """
        Obtem o Grafo do mapa de zonas.

        Returns:
            Graph: zoneMap
        """
        return Enviroment._zoneMap
    
    
    @staticmethod
    def getInfoMap() -> Graph:
        """
        Obtem o Grafo do mapa informação de zonas.

        Returns:
            Graph: infoMap
        """
        return Enviroment._infoMap
    
    
    @staticmethod
    def getCurrentZone() -> Zone:
        """
        Obtem a instancia da zona atual

        Returns:
            Zone: zona
        """        
        return Enviroment._zones[Enviroment._currentZone]
    
    
    @staticmethod
    def indexOfLastVisitedZone() -> int:
        """
        Devolve o indice da ultima Zone visitada.

        Returns:
            int: Indice da ultima zona visitada
        """
        return Enviroment._lastVisited
    
    
    @staticmethod
    def indexOfCurrentZone() -> int:
        """
        Devolve o indice da Zone atual.

        Returns:
            int: Indice da zona atual
        """
        return Enviroment._currentZone
    
    
    @staticmethod
    def zoneToString(index: int) -> str:
        """
        Gera a string representante de uma zona

        Args:
            index (int): index da zona

        Returns:
            str: zona em string
        """        
        return f"Z{index+1:02d}"
    
    
    @staticmethod
    def entryToString(zFrom: int, zTo: int) -> str:
        """
        Gera a string representante de uma entrada

        Args:
            zFrom (int): zona origem
            zTo (int): zona chegada

        Returns:
            str: entrada em string
        """        
        return f"E{min(zFrom+1, zTo+1):02d}{max(zFrom+1, zTo+1):02d}"
    
    
    @staticmethod
    def getEdgeBetweenZoneAndEntry(zFrom: int, zTo: int) -> tuple[str, str]:
        """
        Obtem a areste por entre a zona e a entrada.

        Args:
            zFrom (int): zona origem
            zTo (int): zona chegada

        Returns:
            tuple[str, str]: zona em string, entrada em string
        """        
        return (Enviroment.zoneToString(zFrom), Enviroment.entryToString(zFrom, zTo))
    
    
    @staticmethod
    def getEdgeBetweenEntryAndEntry(z1: int, z2: int, z3: int) -> tuple[str, str]:
        """
        Obtem as arestas por entre as entradas das zonas.

        Args:
            z1 (int): index de zona 1
            z2 (int): index de zona 2
            z3 (int): index de zona 3

        Returns:
            tuple[str, str]: Arestas em string
        """        
        return (Enviroment.entryToString(z1, z2), Enviroment.entryToString(z2, z3))
    
    
    @staticmethod
    def getMidPoint(zone: Zone) -> tuple[int, int]:
        """
        Obtem o ponto medio da zona em questão.

        Args:
            zone (Zone): Zona

        Returns:
            tuple[int, int]: Coordenadas do ponto medio
        """        
        return Utils.calcMidPoint(zone.getXRange(), zone.getYRange())
    
    
    @staticmethod
    def generateEntryPaths() -> None:
        """Gera o caminho para a entrada de uma zona."""        
        # Para cada zona no grafo:
        for zone in Enviroment._infoMap.nodes():
            zones = sorted(nx.all_neighbors(Enviroment._infoMap, zone))
            # Primeira entrada
            for i in range(len(zones) - 1):
                # Segunda entrada
                for j in range(i + 1, len(zones)):
                    # Se não houver já uma aresta associada às 2 entradas:
                    edge = Enviroment.getEdgeBetweenEntryAndEntry(zone, zones[i], zones[j])
                    if not Enviroment._zoneMap.has_edge(*edge):
                        # Vamos buscar as coordenadas das entradas
                        entryI = Enviroment._zoneMap\
                            .nodes[Enviroment.entryToString(zone, zones[i])][Enviroment._map["MIDPOINT"]]
                        entryJ = Enviroment._zoneMap\
                            .nodes[Enviroment.entryToString(zone, zones[j])][Enviroment._map["MIDPOINT"]]
                        
                        # Calculamos a distancia entre as entradas
                        distance = Utils.calcDistance(entryI, entryJ)
                        
                        # Adicionamos com o peso
                        Enviroment._zoneMap.add_edges_from(
                            [edge], 
                            weight = distance
                        )


    @staticmethod
    def findNode(foo) -> tuple:
        """
        Encontra um nodo no grafo infoMap supondo uma condição.

        Args:
            foo (function): condição booleana de paragem.

        Raises:
            nx.NodeNotFound: levantado ao não encontrar o nodo

        Returns:
            tuple: nodo encontrado
        """
        resNode = None
        for node in list(Enviroment._infoMap.nodes(data = True)):
            try:
                if foo(node):
                    resNode = node
                    break
            except Zone.ZoneNotDefinedException as e:
                continue
        
        if not resNode:
            raise nx.NodeNotFound()
        
        return resNode


    @staticmethod
    def updateMap() -> None:
        """Atualiza o zoneMap."""        
        robotPos = Robot.getPosition()
        
        # Entrada 1 para MidPoint
        midPoint = Enviroment.getMidPoint(Enviroment._zones[Enviroment._currentZone])
        distance = Utils.calcDistance(midPoint, robotPos)
        Enviroment._zoneMap.add_edges_from(
            [Enviroment.getEdgeBetweenZoneAndEntry(Enviroment._currentZone, Enviroment._lastVisited)], 
            weight = distance
        )
        Enviroment._zoneMap.nodes[Enviroment.zoneToString(Enviroment._currentZone)][Enviroment._map["MIDPOINT"]] = midPoint
        
        # Entrada 2 para MidPoint
        midPoint = Enviroment.getMidPoint(Enviroment._zones[Enviroment._lastVisited])
        distance = Utils.calcDistance(midPoint, robotPos)
        Enviroment._zoneMap.add_edges_from(
            [Enviroment.getEdgeBetweenZoneAndEntry(Enviroment._lastVisited, Enviroment._currentZone)],
            weight = distance   
        )
        Enviroment._zoneMap.nodes[Enviroment.zoneToString(Enviroment._lastVisited)][Enviroment._map["MIDPOINT"]] = robotPos
        
        # Entrada para Entrada
        Enviroment._zoneMap.nodes[Enviroment.entryToString(Enviroment._currentZone, Enviroment._lastVisited)][Enviroment._map["MIDPOINT"]] = robotPos
        
        Enviroment.generateEntryPaths()
   
            
    @staticmethod
    def updateInfoMap(newZone: int) -> None:
        """
        Atualiza o infoMap.

        Args:
            newZone (int): index da nova zona.
        """
        # Se a nova zona não for o valor default (-1):
        if newZone != -1:
            # Se entrarmos numa zona diferente à atual:
            if Enviroment._currentZone != newZone:
                # Atualizamos a zona
                Enviroment._currentZone, Enviroment._lastVisited = newZone, Enviroment._currentZone
                # Adicionamos a aresta entre a zona atual e a nova
                Enviroment._infoMap.add_edge(newZone, Enviroment._currentZone)
                # Atualizamos o zoneMap
                Enviroment.updateMap()
    
    
    @staticmethod
    def update(coordinates: tuple[int, int], objects: list[str] = []) -> None:
        """
        Atualiza os dados e grafos utilizados na execução dos problemas.

        Args:
            coordinates (tuple[int, int]): Coordenadas do atuais do robot.
            objects (list[str], optional): Lista de objetos avistados atualmente. Por padrão [].
        """        
        from objectManager import Objects
        
        adapted_pos = Robot.getAdaptedPosition()
        # Para cada zona:
        for i, zone in enumerate(Enviroment._zones):
            # Verificamos se estamos atualmente nela.
            if zone.isIn(adapted_pos):
                # Atualizamos o mapa de informação
                Enviroment.updateInfoMap(i)
                # Saimos do for loop
                break
        
        curr = Enviroment.getCurrentZone()
        
        # Se existirem objetos
        if objects:
            # Para cada objeto
            for obj in objects:
                # Vamos criar o objeto (Separando num tuplo pelo tipo e nome)
                obj = tuple(obj.split(SPLITTER, 1))
                
                # Se o objeto não estiver já guardado.
                if not Objects.isIn(obj):
                    # Tentamos:
                    try:
                        # Obtemos os objetos atuais
                        currentObjects = [n[1] for n in Enviroment._infoMap.nodes[Enviroment._currentZone][obj[0]]]
                        
                        # Se o nome do objeto não estiver nos objetos atuais:
                        if obj[1] not in currentObjects:
                            # Vamos ao grafo  
                            #     no node da zona atual (dicionario), No indice do tipo de objeto
                            #     damos append nesse indice a posição adaptada do objeto e respetivo nome.
                            Enviroment._infoMap\
                                .nodes[Enviroment._currentZone][obj[0]]\
                                .append((adapted_pos, obj[1]))
                    
                    # Ao levantar KeyError (Não foi encontrado a chave `obj[0]` no dicionario)
                    except KeyError:
                        # Atribuimos ao node da zona atual, no obj[0] atribuimos as coordenadas e o nome do objeto.
                        Enviroment._infoMap.nodes[Enviroment._currentZone][obj[0]] = [(adapted_pos, obj[1])]
                
                # Adcionamos o objeto caso seja novo
                Objects.add(obj, curr)
                
        try:
            curr.getType()
        except Exception:
            if Enviroment._lastVisited == -1:
                curr.setStart()

                
    @staticmethod
    def getTypeOfZone(zone: int) -> str:
        """
        Indica qual o tipo da zona pelo index da mesma.

        Args:
            zone (int): index da zona

        Returns:
            str: tipo de zona
        """        
        return Enviroment._zones[zone].getType()
    

    @staticmethod
    def addRobotToGraph() -> None:
        """Adiciona ao grafo um nodo representante da presença do Robot."""        
        # Criamos o nó correspondente ao Robot        
        Enviroment._zoneMap.add_node(Enviroment._map["ROBOT"])
        # Recolhemos todos os vizinhos da zona em que o Robot está atualmente
        edges = nx.all_neighbors(Enviroment._zoneMap, Enviroment.zoneToString(Enviroment._currentZone))
        # Para cada aresta:
        for edge in edges:
            # Calculamos a distancia entre o Robot e o midPoint
            distance = Utils.calcDistance(
                Enviroment._zoneMap.nodes[edge][Enviroment._map["MIDPOINT"]], 
                Robot.getPosition()
            )
            # E adicionamos a aresta ao Robot com a distancia correspondente como peso.
            Enviroment._zoneMap.add_edge(Enviroment._map["ROBOT"], edge, weight = distance)


    @staticmethod
    def delRobotFromGraph() -> None:
        """Apaga o nodo dedicado à presença do Robot"""
        try:
            # Remover o robot do grafo
            Enviroment._zoneMap.remove_node(Enviroment._map["ROBOT"])
        except:
            # Já foi previamente removido
            pass

    
    @staticmethod
    def getProbabilityOfAdultInZoneIfThereIsChildButNoShopcar() -> float:
        ''''Determina a probabilidade de encontrar um adulto na zona, 
        sabedo que está lá uma criança, mas nao um carrinho'''

        #Contabiliza as zonas encontradas, as zonas que contêm adulto, criança mas não carrinho
        # e as zonas que têm criança mas não têm carrinho
        total_zones                               = 0
        zones_with_adult_and_child_but_no_shopcar = 0
        zones_with_child_but_no_shopcar           = 0

        # Efetuar ciclo para verificar zona no grafo e incrementar as variaveis acima
        for node in list(Enviroment._infoMap.nodes(data = True)):
            if OBJ["ADULT"] in node[1] and OBJ["CHILD"] in node[1] and not OBJ["CART"] in node[1]:
                zones_with_adult_and_child_but_no_shopcar += 1
            if OBJ["CHILD"] in node[1] and OBJ["CART"] not in node[1]:
                zones_with_child_but_no_shopcar += 1
            total_zones += 1        
        
        #Probabilidade de existir zona com adulto,criança mas nao carrinho
        prob_zones_with_adult_and_child_but_no_shopcar = zones_with_adult_and_child_but_no_shopcar / total_zones

        #Probabilidade de existir zona com criança mas nao carrinho
        prob_zones_with_child_but_no_shopcar = zones_with_child_but_no_shopcar / total_zones

        #Probabilidade Condicionada
        return prob_zones_with_adult_and_child_but_no_shopcar / prob_zones_with_child_but_no_shopcar                


    @staticmethod
    def getProbabilityOfNextPersonBeAChild() -> float:
        """
        Determina a probabilidade de a proxima pessoa ser uma criança
        Contabiliza os "objetos" agrupando-os de forma individual
        
          A: Adult
          B: Shopcar
          C: Child
          n: NOT
        
          'and' usado para simular o seguinte: P(B,C)
        Exemplo: ABnC = Adult and Shopcar and NOT Child

        Returns:
            float: probabilidade de a proxima pessoa avistada ser uma criança
        """
        # Contadores
        countA = 0
        countB = 0
        countC = 0

        # A probabilidade que estamos a calcular pode-se tradizir da seguinte forma.
        # P(C) = P(C,B) / P(B)
        # Assim sendo, o robo só precisa de recolher as probabilidades de A e B
        # A nossa linha de raciocinio esta devidamente clarificada no pdf do relatorio

        # Efetuar ciclo para verificar zona no grafo e incrementar as variaveis acima
        
        for node in list(Enviroment._infoMap.nodes(data = True)):
            if OBJ["ADULT"] in node[1]:
                countA += len(node[1][OBJ["ADULT"]])
            if OBJ["CART"] in node[1]:
                countB += len(node[1][OBJ["CART"]])
            if OBJ["CHILD"] in node[1]:
                countC += len(node[1][OBJ["CHILD"]])
                
        # Contabiliza os "objectos" encontrados (crianças, adultos e carrinhos)
        total_objects = countA + countB + countC
        
        # Calculo das probabilidades
        pA = countA / total_objects
        pB = countB / total_objects

        # 0.8 e o 0.1 são valores provenienetes da tabela dada no enunciadoe são respetivamente
        # prob_C_knowing_AB = 0.8 e prob_C_knowing_nAB = 0.1  
        pBAC = (pA * pB * 0.8)
        pBnAC = ((1 - pA) * pB * 0.1)
        pCandB = pBAC + pBnAC

        # Probabilidade pretendida
        return pCandB / pB
   