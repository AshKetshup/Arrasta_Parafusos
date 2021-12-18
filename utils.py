import inspect
from operator import mul

myself = lambda: inspect.stack()[1][3]

class SimpleException(Exception):
    def __init__(self, errorMsg: str, funName: str = "" ) -> None:
        """
        Construtor da SimpleException.

        Args:
            errorMsg (str): Mensagem enviada como payload.
        """
        self.payload = f"{funName} | {errorMsg}"

    def what(self) -> str:
        """
        Devolve o payload.

        Returns:
            str: Payload da exceção.
        """        
        return self.payload


class Utils():
    class LinearRegression():
        def __init__(self):
            pass
        
        def generate(self, xyList: list[tuple[float, float]]):
            self.x = [i for i, _ in xyList]
            self.y = [j for _, j in xyList]
            
            self.sumX  = sum(self.x)
            self.sumY  = sum(self.y)
            self.sumXY = sum(map(lambda x, y: x*y, self.x, self.y))
            self.sumX2 = sum([x**2 for x in self.x])
            self.n     = len(xyList)
            
            self.m = ((self.n * self.sumXY) - (self.sumX * self.sumY)) / ((self.n * self.sumX2) - (self.sumX**2))
            self.b = (self.sumY - self.m * self.sumX) / self.n
            
            return self
            
        def predictX(self, y: float) -> float:
            return ((y - self.b) / self.m)
            
        def predictY(self, x: float) -> float:
            return (self.m * x + self.b)
        
        def __str__(self) -> str:
            return f"y = ({self.m}) x + ({self.b})"
            
    @staticmethod
    def calcDistance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return ((a[1] - a[0]) ** 2 + (b[1] - b[0]) ** 2) ** 0.5
    
    @staticmethod
    def calcMidPoint(xRange: tuple[int, int], yRange: tuple[int, int]) -> tuple[int, int]:
        return ((xRange[0] + xRange[1]) / 2, (yRange[0] + yRange[1]) / 2)

    @staticmethod
    def timeToStr(t):
        """Formata um dado tempo em segundos e milissegundos."""
        return "{0:3d} segundos e {1:3d} milissegundos".format(int(t), int((t - int(t)) * 1000))    