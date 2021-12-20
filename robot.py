from networkx.generators import line
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import time

from objectManager import Objects
from utils import Utils, SimpleException

class Robot():
    """
    Classe de gestão do Robot.

    Raises:
        Robot.NotAvailablePrediction: Levantada quando é requisitado uma previsão 
        em que o mesmo não tem dados suficientes para a concretizar.

    CheckList:
    [X]: Inicializar as variaveis
        * [X] DIR
        * [X] last & curr Position
        * [X] last & curr Battery
        * [X] last & curr Time
        * [X] last & curr Velocity
        * [X] functions
    [X]: Implement manager functions
        * [X] Positions 
            - [X] getPosition()
            - [X] getAdaptedPosition()
            - [X] getDirection()
            - [X] setPosition()
            - [X] isDifferentPosition()
        * [X] Velocity
            - [X] updateVelocity()
        * [X] Battery
            - [X] setBattery()
        * [X] Functions
            - [X] updateFunctions()
            - [X] predictVelocityFromTime()
            - [X] predictVelocityFromBattery()
            - [X] predictTimeFromBattery()
            - [X] predictTimeFromDistance()
    [X]: Implement Robot manager functions
        * [X] updateRobot()
    """
    
    DIR = {
        "STATIC"   : 0,
        "RIGHT"    : 1,
        "LEFT"     : 2,
        "UP"       : 3,
        "DOWN"     : 4,
    }
    
    _lastPosition = (100, 100)
    _currPosition = (100, 100)
    
    _lastBattery = 0
    _currBattery = 0
    
    _timeSince100 = time.time()
    _last100Time  = time.time()
    
    _lastTime = time.time()
    _currTime = time.time()
    
    _currVelocity = 0.0
    _lastVelocity = 0.0
    
    _functions: dict[str, tuple[any, list]] = {
        "VelocityBattery" :    (Utils.LinearRegression(), []),
        "VelocityTime"    :    (Utils.LinearRegression(), []),
        "BatteryTime"     : (Utils.NonLinearRegression(), [])
    }
    
    ERROR_NOT_AVAILABLE_PREDICTION = "Não é possivel efetuar a previsão"
    class NotAvailablePrediction(SimpleException):
        """
        Excepção indicada para quando não é possivel efetuar a previsão.

        Inherits:
            `SimpleException` (class): Very basic exception
        """
        pass
    
    
    @staticmethod
    def isDifferentPos() -> bool:
        """
        Devolve se a posição atual é diferente da posição anterior.

        Returns:
            bool: se são diferentes
        """        
        return Robot._currPosition != Robot._lastPosition
    
    
    @staticmethod
    def getDirection() -> list[int]:
        """
        Calcula as direções que o Robot toma considerando as posição atual e anterior.

        Returns:
            list[int]: Conjunto de direções tomadas pelo robot.
        """        
        (x1, y1), (x0, y0) = Robot._currPosition, Robot._lastPosition 
        
        robotDir = (x1 - x0, y1 - y0)
        
        if robotDir == (0, 0):
            return [Robot.DIR["STATIC"]]
        
        direction = list()
        if robotDir[0] != 0:
            direction.append(Robot.DIR["RIGHT" if robotDir[0] > 0 else "LEFT"])
        
        if robotDir[1] != 0:
            direction.append(Robot.DIR["DOWN" if robotDir[1] > 0 else "UP"])
        
        return direction
    
    
    @staticmethod
    def getPosition() -> tuple[int, int]:
        """
        Devolve a posição atual do Robot.

        Returns:
            tuple[int, int]: Coordenadas atuais do Robot.
        """        
        return Robot._currPosition
    
    
    @staticmethod
    def getAdaptedPosition() -> tuple[int, int]:
        """
        Devolve a posição adaptada, calculada pela direção tomada pelo robot e o tamanho dos objetos.

        Returns:
            tuple[int, int]: Coordenadas do objeto encontrado
        """        
        position = Robot.getPosition()
        direction = Robot.getDirection()
        if Robot.DIR["STATIC"] in direction:
            return position
        
        return (
            position[0] + Objects.SIZE["OBJECT"] if Robot.DIR["RIGHT"] in direction else -Objects.SIZE["OBJECT"],
            position[1] + Objects.SIZE["OBJECT"] if Robot.DIR["DOWN"]  in direction else -Objects.SIZE["OBJECT"]
        )


    @staticmethod
    def getCurrentBattery() -> int:
        """
        Devolve a bateria atual do robot.

        Returns:
            int: Percentagem de bateria do robot
        """        
        return Robot._currBattery


    @staticmethod
    def getCurrentTime() -> float:
        """
        Devolve o tempo atual.

        Returns:
            float: tempo atual
        """        
        return Robot._currTime    
    
    
    @staticmethod
    def setPosition(position: tuple[int, int]) -> None:
        """
        Define a posição do robot através de uma dada coordenada.

        Args:
            position (tuple[int, int]): posição dada
        """        
        Robot._currPosition, Robot._lastPosition = position, Robot._currPosition
        
    
    @staticmethod
    def setBattery(battery: int) -> None:
        """
        Define a bateria atual dada a sua percentagem.

        Args:
            battery (int): Bateria atual
        """        
        Robot._currBattery, Robot._lastBattery = battery, Robot._currBattery


    @staticmethod
    def updateTimeElapsed(battery: int) -> None:
        if battery == 100:
            Robot._last100Time = time.time()
        Robot._timeSince100 = time.time() - Robot._last100Time


    @staticmethod
    def updateVelocity() -> None:
        """
        Atualiza a velocidade instantania do robot baseado na posição atual e na do ultimo frame.
        """        
        if Robot.isDifferentPos():
            Robot._currTime, Robot._lastTime = time.time(), Robot._currTime
            Robot._currVelocity, Robot._lastVelocity = (
                Utils.calcDistance(Robot._lastPosition, Robot._currPosition) / (Robot._currTime - Robot._lastTime), 
                Robot._currVelocity
            )

    # TODO
    @staticmethod
    def updateFunctions() -> None:
        """
        Atualiza as funções de Regressão linear
        """
        # Atualiza as informações
        Robot._functions["VelocityBattery"][1].append((Robot._currVelocity, Robot._currBattery))
        Robot._functions["VelocityTime"][1].append((Robot._timeSince100, Robot._currVelocity))
        Robot._functions["BatteryTime"][1].append((Robot._timeSince100, Robot._currBattery))
    
    
    @staticmethod
    def updateRobot(position: tuple[int, int], battery: int):
        """
        Atualiza o estado completo do Robot tendo em conta sua posição atual e a bateria correspondente.

        Args:
            position (tuple[int, int]): Posição do Robot
            battery (int): Bateria do Robot
        """        
        # """Atualiza o estado completo do robot tendo em conta a posição atual e a bateria restante."""
        # Atualiza a bateria
        Robot.setBattery(battery)
        # Atualiza a posição atual
        Robot.setPosition(position)
        # Atualiza o tempo atual
        Robot.updateTimeElapsed(battery)
        # Atualiza a velociadade atual
        Robot.updateVelocity()
        # Atualiza as linear and nonLinear functions
        Robot.updateFunctions()
        
        
    @staticmethod
    def predictTimeFromBattery(battery: int) -> float:
        """
        Estima através do valor dado de bateria quanto tempo desde os 100% demoraria para o atingir.
        Usa uma Regressão não linear de y = -(x**2) / c + 100

        Args:
            battery (int): Nivel de bateria requesitado

        Returns:
            float: Tempo até ao nivel da bateria ser alcançado.
        """
        if not len(Robot._functions["BatteryTime"][1]) or not battery:
            raise Robot.NotAvailablePrediction(Robot.ERROR_NOT_AVAILABLE_PREDICTION)
        
        
        
        # Inicializar non Linear Regression
        Robot._functions["BatteryTime"][1].sort()
        x: Utils.NonLinearRegression = Robot._functions["BatteryTime"][0]
        
        try:
            x.generate(
                Robot._functions["BatteryTime"][1],
                x.coef, # valor do coeficiente
                100     # valor de B (começa sempre em 100)
            )
        except AttributeError:
            x.generate(
                Robot._functions["BatteryTime"][1],
                250,    # valor do coeficiente
                100     # valor de B (começa sempre em 100)
            )
        
        timeLast = x.predictX(battery, x.coef) - Robot._timeSince100
        
        return timeLast
    
    
    @staticmethod
    def predictVelocityFromBattery(battery: int) -> float:
        """
        Estima através do valor dado de bateria qual a velocidade no ponto.

        Args:
            battery (int): Nivel de bateria requesitado

        Returns:
            float: Velocidade prevista.
        """
        if not len(Robot._functions["VelocityBattery"][1]) or not Robot._currBattery:
            raise Robot.NotAvailablePrediction(Robot.ERROR_NOT_AVAILABLE_PREDICTION)

        value = np.array(battery).reshape(-1, 1)
           
        # Inicializar LinearRegression        
        f = (np.array([i for i, _ in Robot._functions["VelocityBattery"][1]]).reshape(-1, 1),
             np.array([j for _, j in Robot._functions["VelocityBattery"][1]]).reshape(-1, 1))
        
        regression = Robot._functions["VelocityTime"][0].fit(f[0], f[1])
        
        return regression.predict(value)[0][0]
    
    
    @staticmethod
    def predictVelocityFromTime(eTime: int) -> float:
        """
        Estima através do valor dado de Tempo a Velocidade correspondente.

        Args:
            eTime (int): Tempo desde a bateria a 100% pedido

        Returns:
            float: Velocidade prevista.
        """
        if not len(Robot._functions["VelocityTime"][1]) or not Robot._currBattery:
            raise Robot.NotAvailablePrediction(Robot.ERROR_NOT_AVAILABLE_PREDICTION)

        value = np.array(eTime).reshape(-1, 1)
           
        # Inicializar LinearRegression        
        f = (np.array([i for i, _ in Robot._functions["VelocityTime"][1]]).reshape(-1, 1),
             np.array([j for _, j in Robot._functions["VelocityTime"][1]]).reshape(-1, 1))
        
        regression = Robot._functions["VelocityTime"][0].fit(f[0], f[1])
        
        return regression.predict(value)[0][0]
    
    
    @staticmethod
    def predictTimeFromDistance(distance: int) -> float:
        """
        Estima através de uma dada distancia o tempo que lhe levaria a precorrer.

        Args:
            distance (int): distancia dada

        Returns:
            float: Tempo estimado para a percorrer
        """        
        vf = Robot.predictVelocityFromTime(time.time() - Robot._last100Time)
        vi = Robot.predictVelocityFromTime(0)
        
        elapsedTime = 2 * distance / (vf + vi)
        return elapsedTime