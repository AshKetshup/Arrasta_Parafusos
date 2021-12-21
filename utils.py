import inspect
from matplotlib import pyplot as plt
import numpy as np
from math import sqrt
from scipy.optimize import curve_fit

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
    class NonLinearRegression():
        def __init__(self):
            pass
        
        def generate(self, xyList: list[tuple[float, float]], coef: float, b: float):
            f = [[i for i, _ in xyList], # X
                 [j for _, j in xyList]] # Y
            
            # Atribuimos valores auxiliares
            self.coef = coef
            self.b = b

            # Calculamos os parametros que mais se adequem aos valores dados
            c, _ = curve_fit(self.predictY, f[0], f[1], self.coef)
            self.coef = c[0]
            
            # Geramos o conjunto de pontos conforme a previsão dada
            y = np.array([self.predictY(x, self.coef) for x in f[0]])
            
            return self
            
        def getCoeficient(self) -> float:
            return self.coef
        
        def getB(self) -> float:
            return self.b
            
        def predictX(self, y: float, coef: float) -> float:
            return (sqrt(-y + self.b) * coef)
            
        def predictY(self, x: float, coef: float) -> float:
            return (- (x**2) / coef + self.b)
        
        def __str__(self) -> str:
            return f"y = -(x**2)/{self.coef} + {self.b}"
    
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

    
    #EDITAR etsa funçao
    @staticmethod
    def pathDescription(path):
        """Formata um caminho em frases legíveis para humanos.
        Tem em consideração a formatação utilizada pelo zoneMap da classe Environment."""

        desc = ""
        for p in path:
            try:
                if p[0] == 'X':     # Robot, é sempre o primeiro elemento
                    continue
                elif p[0] == 'Z':   # zona, dada pelo midpoint
                    desc += "\nEstá na zona {0:2d}.".format(int(p[1:]))
                elif p[0] == 'E':   # Porta -> indica um caminho a fazer entre duas salas
                    desc += "\nVá da zona {0:2d} para a zona {1:2d}.".format(int(p[1:3]), int(p[3:]))
                else:
                    raise Exception("I dunno!")     # Outros formatos desconhecidos, interrompe a execução
            except:
                desc += "\n[Error: \"{0}\" was not understood by the path descriptor]".format(p)
        return desc if len(desc) > 0 else "Nenhum caminho foi encontrado."    