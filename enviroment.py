from networkx.classes.graph import Graph
from customException import SimpleException, myself
from objectManager import Objects
import networkx as nx

class Zone():
    ERROR_INVALID_BOUNDARIES = "A Boundary indicada é invalida:"
    class InvalidBoundariesException(SimpleException):
        """
        Excepção usada para declarar Boundaries invalidas.

        Inherits:
            SimpleException (class): Very basic exception
        """        
        pass
    
    ERROR_ZONE_NOT_DEFINED = "Zona atual não definida."
    class ZoneNotDefinedException(SimpleException):
        """
        Excepção usada para declarar uma zona não definida numa tentativa de obter o tipo de zona.

        Inherits:
            SimpleException (class): Very basic exception
        """        
        pass
    
    def __init__(self, xRange: tuple[int, int], yRange: tuple[int, int]) -> None:
        
        if not xRange[0] < xRange[1] or not yRange[0] < yRange[1]:
            raise Zone.InvalidBoundariesException(\
                f"{Zone.ERROR_INVALID_BOUNDARIES} x -> {xRange} y -> {yRange}",\
                myself()\
            )
        
        self.xRange = xRange
        self.yRange = yRange
        self.zoneType = None
        
    def isIn(self, coords: tuple[int, int]) -> bool:
        return coords[0] in range(self.xRange[0], self.xRange[1])\
           and coords[1] in range(self.yRange[0], self.yRange[1])
    
    def getType(self):
        if self.zoneType == None:
            raise Zone.ZoneNotDefinedException(Zone.ERROR_ZONE_NOT_DEFINED, myself())
        else:
            return self.zoneType
    
    def setType(self, zoneType: str) -> None:
        if self.zoneType == None:
            self.zoneType = zoneType


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
        return Enviroment._zoneMap
    
    @staticmethod
    def indexOfLastVisitedZone() -> int:
        return Enviroment._lastVisited
    
    @staticmethod
    def indexOfCurrentZone() -> int:
        return Enviroment._currentZone
    
    @staticmethod
    def updateZoneMap(newRoom: int):
        """TODO: COMENTAR E COMPLETAR"""
        if newRoom:
            if Enviroment._currentRoom != newRoom:
                Enviroment._zoneMap.add_edge(newRoom, Enviroment._currentRoom)
                # Enviroment.updateMap()
    
    
    @staticmethod
    def update(coordinates: tuple[int, int], objects: list[str] = []) -> None:
        for i, zone in enumerate(Enviroment._zones):
            if zone.isIn(coordinates):
                Enviroment.updateZoneMap(i)
                break
        
        if objects:
            for obj in objects:
                obj = tuple(obj.split(Objects.SPLITTER, 1))
                if not Objects.isIn(obj):
                    try:
                        currentObjects = [n[1] for n in Enviroment._zoneMap.nodes[Enviroment._currentZone][obj[0]]]
                        if obj[1] not in currentObjects:
                            Enviroment._zoneMap.nodes[Enviroment._currentZone][obj[0]].append("""TODO: Passar posição """, obj[1])
                    except KeyError:
                        Enviroment._zoneMap.nodes[Enviroment._currentZone][obj[0]] = [(coordinates, obj[1])]
                Enviroment.add(obj)