import inspect
from math import sqrt
from scipy.optimize import curve_fit

# Lambda expression dedicado para debug de funções
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
    """Classe wrapper de ferramentas para a execução do programa."""
    
    class NonLinearRegression():
        def __init__(self):
            """Inicializa de forma vazia a classe."""
            pass
        
        def generate(self, xyList: list[tuple[float, float]], coef: float, b: float):
            """
            Gera os valores para o coeficiente e para o y inicial da curva de regressão.
            A partir de dados propostos.

            Args:
                xyList (list[tuple[float, float]]): Lista de pontos
                coef (float): Coeficiente proposto
                b (float): Y inicial proposto

            Returns:
                NonLinearRegression: a propria instancia com os dados agora calculados
            """
            f = [[i for i, _ in xyList], # X
                 [j for _, j in xyList]] # Y
            
            self.x = f[0]
            self.y = f[1]
            
            # Atribuimos valores auxiliares
            self.coef = coef
            self.b = b

            # Calculamos os parametros que mais se adequem aos valores dados
            c, _ = curve_fit(self.predictY, f[0], f[1], self.coef)
            self.coef = c[0]
            
            return self
            
        def getCoeficient(self) -> float:
            return self.coef
        
        def getB(self) -> float:
            return self.b
        
        # def plot(self):
        #     """Dá plot à regressão não linear"""
        #     import matplotlib.pyplot as plt
        #     plt.style.use('seaborn-whitegrid')
        #     plt.plot(self.x, self.y, '.')
        #     plt.plot(self.x, list(map(lambda x: self.predictY(x, self.coef), self.x)))
        #     plt.show()
        
        def predictX(self, y: float, coef: float) -> float:
            """
            Devolve X atraves de um Y.

            Args:
                y (float): valor de Y

            Returns:
                float: valor de X
            """
            return (sqrt(-y + self.b) * coef)
            
        def predictY(self, x: float, coef: float) -> float:
            """
            Devolve Y atraves de um X.

            Args:
                x (float): valor de X

            Returns:
                float: valor de Y
            """
            return (- (x**2) / coef + self.b)
        
        def __str__(self) -> str:
            return f"y = -(x**2)/{self.coef} + {self.b}"
    
    class LinearRegression():
        def __init__(self):
            """Inicializa de forma vazia a classe."""
            pass
        
        def generate(self, xyList: list[tuple[float, float]]):
            """
            Gera os valores para o declive e para o y inicial da reta de regressão.

            Args:
                xyList (list[tuple[float, float]]): Lista de pontos

            Returns:
                LinearRegression: a propria instancia com os dados agora calculados
            """
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
        
        # def plot(self):
        #     """Dá plot à regressão linear"""
        #     import matplotlib.pyplot as plt
        #     plt.style.use('seaborn-whitegrid')
        #     plt.plot(self.x, self.y, 'o')
        #     plt.plot(self.x, list(map(lambda x: self.predictY(x), self.x)))
        #     plt.show()
            
        def predictX(self, y: float) -> float:
            """
            Devolve X atraves de um Y.

            Args:
                y (float): valor de Y

            Returns:
                float: valor de X
            """
            return ((y - self.b) / self.m)
            
        def predictY(self, x: float) -> float:
            """
            Devolve Y atraves de um X.

            Args:
                x (float): valor de X

            Returns:
                float: valor de Y
            """
            return (self.m * x + self.b)
        
        def __str__(self) -> str:
            return f"y = ({self.m}) x + ({self.b})"
            
    @staticmethod
    def calcDistance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    
    @staticmethod
    def calcMidPoint(xRange: tuple[int, int], yRange: tuple[int, int]) -> tuple[int, int]:
        """
        Calcula o ponto medio através dos limites de coordenada X e Y.

        Args:
            xRange (tuple[int, int]): Limite de X
            yRange (tuple[int, int]): Limite de Y

        Returns:
            tuple[int, int]: Ponto medio
        """
        return ((xRange[0] + xRange[1]) / 2, (yRange[0] + yRange[1]) / 2)

    @staticmethod
    def timeToStr(t) -> str:
        """
        Formata um dado tempo em segundos e milissegundos.

        Args:
            t (float): tempo

        Returns:
            str: tempo em string
        """
        return "{0:3d} segundos e {1:3d} milissegundos".format(int(t), int((t - int(t)) * 1000))

    
    #EDITAR etsa funçao
    @staticmethod
    def pathDescription(path: list[str], currZone: str) -> str:
        """
        Formata um caminho em frases legíveis para humanos.
        Tem em consideração a formatação utilizada pelo zoneMap da classe Environment.

        Args:
            path (list[str]): lista do caminho de zonas e entradas
            currZone (str): zona atual em string

        Returns:
            str: descrição do caminho
        """        

        desc = ""
        for p in path:
            try:
                if p[0] == 'X':     # Robot, é sempre o primeiro elemento
                    desc += f"\nEstá na zona {int(currZone[1:]):2d}."
                elif p[0] == 'Z':   # zona, dada pelo midpoint
                    desc += f"\nChega na zona {int(p[1:]):2d}."
                elif p[0] == 'E':   # Porta -> indica um caminho a fazer entre duas salas
                    desc += f"\nPasse por entre as zonas {int(p[1:3]):2d} e {int(p[3:]):2d}."
                else:               # Outros formatos desconhecidos, interrompe a execução
                    raise Exception("I dunno!")
            except:
                desc += "\n[Error: \"{0}\" was not understood by the path descriptor]".format(p)
        return desc if len(desc) > 0 else "Nenhum caminho foi encontrado."    