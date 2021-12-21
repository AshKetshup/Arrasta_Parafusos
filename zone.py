from utils import SimpleException, myself

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
        if not self._zoneType:
            raise Zone.ZoneNotDefinedException(Zone.ERROR_ZONE_NOT_DEFINED)
        
        return self._zoneType
    

    def setType(self, zoneType: str) -> None:
        """
        Configura o tipo de zona atual.

        Args:
            `zoneType` (str): Tipo de zona atual.
        """
        if self._zoneType:
            print(Zone.ERROR_ZONE_ALREADY_DEFINED)
            raise Zone.ZoneAlreadyDefinedException(Zone.ERROR_ZONE_ALREADY_DEFINED, myself())
        
        self._zoneType = zoneType

    
    def getXRange(self) -> tuple[int, int]:
        return self._xRange
    
    def getYRange(self) -> tuple[int, int]:
        return self._yRange
