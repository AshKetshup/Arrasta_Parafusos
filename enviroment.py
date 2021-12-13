from networkx.classes.graph import Graph
from customException import SimpleException, myself
from objectManager import Objects
from robot import Robot
import networkx as nx

from utils import Utils

class Zone():
    """
    Classe usada para armazenar e manipular dados de Zona.

    Raises:
        `Zone.InvalidBoundariesException`: Excepção usada para declarar Boundaries invalidas.
        `Zone.ZoneNotDefinedException`: Excepção usada para declarar uma zona não definida numa tentativa de obter o tipo 
        de zona.
    """
    
    
    ERROR_INVALID_BOUNDARIES = "A Boundary indicada é invalida:"
    class InvalidBoundariesException(SimpleException):
        """
        Excepção usada para declarar Boundaries invalidas.

        Inherits:
            `SimpleException` (class): Very basic exception
        """
        pass
    
    
    ERROR_ZONE_NOT_DEFINED = "Zona atual não definida."
    class ZoneNotDefinedException(SimpleException):
        """
        Excepção usada para declarar uma zona não definida numa tentativa de obter o tipo de zona.

        Inherits:
            `SimpleException` (class): Very basic exception
        """
        pass
    
    
    ERROR_ZONE_ALREADY_DEFINED = "Zona atual já foi definida."
    class ZoneAlreadyDefinedException(SimpleException):
        """
        Excepção usada para declarar uma zona já previamente definida numa tentativa de configurar o tipo de zona.

        Inherits:
            `SimpleException` (class): Very basic exception
        """
        pass
    
    
    def __init__(self, xRange: tuple[int, int], yRange: tuple[int, int]) -> None:
        """
        Construtor de um objeto Zone.

        Args:
            `xRange` (tuple[int, int]): Alcance de coordenadas no eixo x.
            `yRange` (tuple[int, int]): Alcance de coordenadas no eixo y.

        Raises:
            `Zone.InvalidBoundariesException`: Levantado quando o 1º elemento de um dado tuplo é maior ou igual ao 2º.
        """
        if not xRange[0] < xRange[1] or not yRange[0] < yRange[1]:
            raise Zone.InvalidBoundariesException(f"{Zone.ERROR_INVALID_BOUNDARIES} x -> {xRange} y -> {yRange}", myself())
        
        self._xRange = xRange
        self._yRange = yRange
        self._zoneType = None
        
        
    def isIn(self, coords: tuple[int, int]) -> bool:
        """
        Devolve a resposta à pergunta se um par de coordenadas está incluido dentro do alcançe da Zona.

        Args:
            `coords` (tuple[int, int]): Coordenadas dadas.

        Returns:
            bool: True se estiver incluido; False caso contrario.
        """
        return coords[0] in range(self._xRange[0], self._xRange[1])\
           and coords[1] in range(self._yRange[0], self._yRange[1])
    

    def getType(self) -> str:
        """
        Obtem o tipo da zona.

        Raises:
            `Zone.ZoneNotDefinedException`: Levantado caso o _zoneType ainda não estiver definido.

        Returns:
            str: Tipo da zona atual.
        """
        if not self.zoneType:
            raise Zone.ZoneNotDefinedException(Zone.ERROR_ZONE_NOT_DEFINED, myself())
        return self._zoneType
    

    def setType(self, zoneType: str) -> None:
        """
        Configura o tipo de zona atual.

        Args:
            `zoneType` (str): Tipo de zona atual.
        """
        if self._zoneType:
            raise Zone.ZoneAlreadyDefinedException(Zone.ERROR_ZONE_ALREADY_DEFINED, myself())
        self._zoneType = zoneType

    
    def getXRange(self) -> tuple[int, int]:
        return self._xRange
    
    def getYRange(self) -> tuple[int, int]:
        return self._yRange
        


class Enviroment():
    _map = {
        "MIDPOINT": "mid",
        "WEIGHT"  : "weight",
        "ROBOT"   :  "X"
    }
    
    _zones = [
        Zone(( 30, 135), (165, 435)),
        Zone((135, 285), (165, 285)),
        Zone((135, 285), (285, 330)),
        Zone((285, 435), (165, 435)),
        Zone((435, 770), (165, 285)),
        Zone((435, 770), (285, 330)),
        Zone((180, 285), ( 30, 135)),
        Zone(( 30, 135), ( 30, 135)),
        Zone((330, 435), ( 30, 135)),
        Zone((480, 585), ( 30, 135)),
        Zone((630, 770), ( 30, 135)),
        Zone((630, 770), (435, 570)),
        Zone((480, 585), (435, 570)),
        Zone((330, 435), (435, 570)),
        Zone((180, 285), (435, 570)),
        Zone(( 30, 135), (435, 570))
    ]
    
    _lastVisited = -1    # Indice da última zona visitada
    _currentZone = -1    # Indice da zona onde o robot se encontra atualmente
    
    _zoneMap = nx.Graph()
    _infoMap = nx.Graph()
    
    
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
        return f"Z{index:02d}"
    
    
    @staticmethod
    def entryToString(zFrom: int, zTo: int) -> str:
        return f"E{min(zFrom, zTo):02d}{max(zFrom, zTo):02d}"
    
    
    @staticmethod
    def getEdgeBetweenZoneAndEntry(zFrom: int, zTo: int):
        return (Enviroment.zoneToString(zFrom), Enviroment.entryToString(zFrom, zTo))
    
    
    @staticmethod
    def getEdgeBetweenEntryAndEntry(z1: int, z2: int, z3: int) -> tuple[str, str]:
        return (Enviroment.entryToString(z1, z2), Enviroment.entryToString(z2, z3))
    
    
    @staticmethod
    def getMidPoint(zone: Zone) -> tuple[int, int]:
        return Utils.calcMidPoint(zone.getXRange(), zone.getYRange())
    
    
    @staticmethod
    def generateEntryPaths() -> None:
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
    def updateMap() -> None:
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
    def updateInfoMap(newZone: int):
        if newZone != -1:
            if Enviroment._currentZone != newZone:
                Enviroment._currentZone, Enviroment._lastVisited = newZone, Enviroment._currentZone
                Enviroment._infoMap.add_edge(newZone, Enviroment._currentZone)
                Enviroment.updateMap()
    
    
    @staticmethod
    def update(coordinates: tuple[int, int], objects: list[str] = []) -> None:
        # Para cada zona
        for i, zone in enumerate(Enviroment._zones):
            # Verificamos se estamos atualmente nela.
            if zone.isIn(coordinates):
                Enviroment.updateInfoMap(i)
                break
        
        # Se verificarmos existirem objetos
        if objects:
            # Para cada objeto
            for obj in objects:
                # Vamos criar o objeto (Separando num tuplo pelo tipo e nome)
                obj = tuple(obj.split(Objects.SPLITTER, 1))
                
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
                                .append((Robot.getAdaptedPosition(), obj[1]))
                    
                    # Ao levantar KeyError (Não foi encontrado a chave `obj[0]` no dicionario)
                    except KeyError:
                        # Atribuimos ao node da zona atual, no obj[0] atribuimos as coordenadas e o nome do objeto.
                        Enviroment._infoMap.nodes[Enviroment._currentZone][obj[0]] = [(coordinates, obj[1])]
                
                # Adcionamos o objeto caso seja novo
                Objects.add(obj)
                
                
    @staticmethod
    def getTypeOfZone(zone: int) -> str:
        return Enviroment._zones[zone].getType()
    
    
    @staticmethod
    def addRobotToGraph() -> None:
        # Criamos o nó correspondente ao Robot        
        Enviroment._zoneMap.add_node(Enviroment._map["ROBOT"])
        # Recolhemos todos os vizinhos da zona em que o Robot está atualmente
        edges = nx.all_neighbors(Enviroment._zoneMap, Enviroment.zoneToString(Enviroment._currentZone))
        # Para cada aresta:
        for edge in edges:
            # Calculamos a distancia entre o Robot e o midPoint
            distance = Utils.calcDistance(
                Enviroment._zoneMap[edge][Enviroment._map["MIDPOINT"]], 
                Robot.getPosition()
            )
            # E adicionamos a aresta ao Robot com a distancia correspondente como peso.
            Enviroment._zoneMap.add_edge(Enviroment._map["ROBOT"], edge, weight = distance)
            
    @staticmethod
    def delRobotFromGraph() -> None:
        try:
            # Remover o robot do grafo
            Enviroment._zoneMap.remove_node(Enviroment._map["ROBOT"])
        except:
            # Já foi previamente removido
            pass