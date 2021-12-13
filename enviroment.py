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
    
    _lastVisited = None    # Indice da última zona visitada
    _currentZone = None    # Indice da zona onde o robot se encontra atualmente
    
    _zoneMap = nx.Graph()
    
    @staticmethod
    def getZoneMap() -> Graph:
        """
        Obtem o Grafo do mapa de zonas.

        Returns:
            Graph: zoneMap
        """
        return Enviroment._zoneMap
    
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
    def getEdgeBetweenRoomAndDoor(zFrom: Zone, zTo: Zone):
        pass #TODO: DO THIS
    
    @staticmethod
    def getMidPoint(zone: Zone) -> tuple[int, int]:
        return Utils.calcMidPoint(zone.getXRange(), zone.getYRange())
    
    @staticmethod
    def updateMap() -> None:
        # TODO: FIND THE BUG
        robotPos = Robot.getPosition()
        
        midPoint = Enviroment.getMidPoint(Enviroment._zones[Enviroment._currentZone])
        distance = Utils.calcDistance(midPoint, robotPos)
        Enviroment._zoneMap.add_edges_from(Enviroment.getEdgeBetweenRoomAndDoor(Enviroment._currentZone, Enviroment._lastVisited)) #KEEP
    
    @staticmethod
    def updateZoneMap(newZone: int):
        if newZone:
            if Enviroment._currentZone != newZone:
                Enviroment._currentZone, Enviroment._lastVisited = newZone, Enviroment._currentZone
                Enviroment._zoneMap.add_edge(newZone, Enviroment._currentZone)
                Enviroment.updateMap()
    
    
    @staticmethod
    def update(coordinates: tuple[int, int], objects: list[str] = []) -> None:
        # Para cada zona
        for i, zone in enumerate(Enviroment._zones):
            # Verificamos se estamos atualmente nela.
            if zone.isIn(coordinates):
                Enviroment.updateZoneMap(i)
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
                        currentObjects = [n[1] for n in Enviroment._zoneMap.nodes[Enviroment._currentZone][obj[0]]]
                        
                        # Se o nome do objeto não estiver nos objetos atuais:
                        if obj[1] not in currentObjects:
                            # Vamos ao grafo  
                            #     no node da zona atual (dicionario), No indice do tipo de objeto
                            #     damos append nesse indice a posição adaptada do objeto e respetivo nome.
                            Enviroment._zoneMap\
                                .nodes[Enviroment._currentZone][obj[0]]\
                                .append(Robot.getAdaptedPosition(), obj[1])
                    
                    # Ao levantar KeyError (Não foi encontrado a chave `obj[0]` no dicionario)
                    except KeyError:
                        # Atribuimos ao node da zona atual, no obj[0] atribuimos as coordenadas e o nome do objeto.
                        Enviroment._zoneMap.nodes[Enviroment._currentZone][obj[0]] = [(coordinates, obj[1])]
                
                # Adcionamos o objeto caso seja novo
                Objects.add(obj)