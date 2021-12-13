from customException import SimpleException
from sklearn.linear_model import LinearRegression
from objectManager import Objects
from utils import Utils
import numpy as np
import time

class Robot():
    """
    [summary]

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
    
    _last100Time = time.time()
    _lastTime = time.time()
    _currTime = time.time()
    
    _currVelocity = 0.0
    _lastVelocity = 0.0
    
    _functions = {
        "VelocityBattery" : (LinearRegression(), []),
        "VelocityTime"    : (LinearRegression(), []),
        "BatteryTime"     : (LinearRegression(), [])
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
    def isDifferentPos():
        return Robot._currPosition != Robot._lastPosition
    
    
    @staticmethod
    def getDirection() -> list[int]:
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
        return Robot._currPosition
        
    @staticmethod
    def getAdaptedPosition() -> tuple[int, int]:
        position = Robot.getPosition()
        direction = Robot.getDirection()
        if Robot.DIR["STATIC"] in direction:
            return position
        
        return (
            position[0] + Objects.SIZE["OBJECT"] if Robot.DIR["RIGHT"] in direction else -Objects.SIZE["OBJECT"],
            position[1] + Objects.SIZE["OBJECT"] if Robot.DIR["DOWN"]  in direction else -Objects.SIZE["OBJECT"]
        )
    
    @staticmethod
    def setBattery(battery: int) -> None:
        Robot._currBattery, Robot._lastBattery = battery, Robot._currBattery
        
    @staticmethod
    def getCurrentBattery() -> int:
        return Robot._currBattery
        
    @staticmethod
    def getCurrentTime() -> int:
        return Robot._currTime    
    
    @staticmethod
    def setPosition(position: tuple[int, int]) -> None:
        Robot._currPosition, Robot._lastPosition = position, Robot._currPosition
    
    
    @staticmethod
    def updateVelocity() -> None:
        if Robot.isDifferentPos():
            Robot._currTime, Robot._lastTime = time.time(), Robot._currTime
            Robot._currVelocity, Robot._lastVelocity = (
                Utils.calcDistance(Robot._lastPosition, Robot._currPosition) / (Robot._currTime - Robot._lastTime), 
                Robot._currVelocity
            )


    @staticmethod
    def updateFunctions() -> None:
        if Robot._currBattery == 100:
            Robot._last100Time = time.time()
        
        # Atualiza as informações
        Robot._functions["VelocityBattery"][1].append((Robot._currVelocity, Robot._currBattery))
        Robot._functions["VelocityTime"][1].append((Robot._currVelocity, Robot._currTime))
        Robot._functions["BatteryTime"][1].append((Robot._currBattery, Robot._currTime))
    
    
    @staticmethod
    def updateRobot(position: tuple[int, int], battery: int):
        """Atualiza o estado completo do robot tendo em conta a posição atual e a bateria restante."""
        # Atualiza a bateria
        Robot.setBattery(battery)
        # Atualiza a posição atual
        Robot.setPosition(position)
        # Atualiza a velociadade atual
        Robot.updateVelocity()
        # Atualiza as linear and nonLinear functions
        Robot.updateFunctions()
        
        
    @staticmethod
    def predictTimeFromBattery(battery: int) -> float:
        """
        Estima através do valor dado de bateria quanto tempo falta em para o atingir.

        Args:
            battery (int): Nivel de bateria requesitado

        Returns:
            float: Tempo até ao nivel da bateria ser alcançado.
        """
        if not len(Robot._functions["BatteryTime"][1]) or not Robot._currBattery:
            raise Robot.NotAvailablePrediction(Robot.ERROR_NOT_AVAILABLE_PREDICTION)

        value = np.array(battery).reshape(-1, 1)
           
        # Inicializar LinearRegression        
        f = (np.array([i for i, _ in Robot._functions["BatteryTime"][1]]).reshape(-1, 1),
             np.array([j for _, j in Robot._functions["BatteryTime"][1]]).reshape(-1, 1))
        
        regression = Robot._functions["BatteryTime"][0].fit(f[0], f[1])
        
        return regression.predict(value)[0][0]
    
    
    @staticmethod
    def predictVelocityFromBattery(battery: int) -> float:
        """
        Estima através do valor dado de bateria qual a velocidade no ponto.

        Args:
            battery (int): Nivel de bateria requesitado

        Returns:
            float: Tempo até ao nivel da bateria ser alcançado.
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
        Estima através do valor dado de bateria quanto tempo falta em para o atingir.

        Args:
            eTime (int): Tempo desde a bateria a 100% pedido

        Returns:
            float: Tempo até ao nivel da bateria ser alcançado.
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
        vf = Robot.predictVelocityFromTime(time.time() - Robot._last100Time)
        vi = Robot.predictVelocityFromTime(0)
        
        elapsedTime = 2 * distance / (vf + vi)
        return elapsedTime