from objectManager import Objects
from utils import Utils
import time

class Robot():
    """
    [summary]

    TODO:
    [ ]: Inicializar as variaveis
        * [X] DIR
        * [X] last & curr Position
        * [X] last & curr Battery
        * [X] last & curr Time
        * [X] last & curr Velocity
        * [ ] functions
    [ ]: Implement manager functions
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
        * [ ] Functions
            - [X] refreshFunctions()
            - [ ] predictTimeFromDistance()
            - [ ] predictTimeFromBattery()
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
    
    _lastTime = time.time()
    _currTime = time.time()
    
    _currVelocity = 0.0
    _lastVelocity = 0.0
    
    # _functions = {
    #     "VelocityBatery": Utils.LinearFunction(),
    #     "VelocityTime"  : Utils.LinearFunction(),
    #     "BateryTime"    : Utils.LinearFunction()
    # }
    
    
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
    def getAdaptedPosition() -> tuple[int, int]:
        position = Robot.getCurrentPosition()
        direction = Robot.getDirection()
        if Robot.DIR["STATIC"] in direction:
            return position
        
        return (
            position[0] + Objects.SIZE["OBJECT"] if Robot.DIR["RIGHT"] in direction else -Objects.SIZE["OBJECT"],
            position[1] + Objects.SIZE["OBJECT"] if Robot.DIR["DOWN"]  in direction else -Objects.SIZE["OBJECT"]
        )
    
    
    @staticmethod
    def getPosition() -> tuple[int, int]:
        return Robot._currPosition
    
    @staticmethod
    def setBattery(battery: int) -> None:
        Robot._currBattery, Robot._lastBattery = battery, Robot._currBattery
        
        
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
        if Robot._currBattery > Robot._lastBattery:
            map(lambda x: x.reset(), Robot._functions)

    
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
        # Robot.updateFunctions() 

    # TODO: 
    # * REWRITE THE LINEAR FUNCTIONS INTO A LINEAR REGRESSION (using `from sklearn.linear_model import LinearRegression`)
    # * CONTINUE