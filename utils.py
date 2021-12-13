import inspect

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
    @staticmethod
    def calcDistance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return ((a[1] - a[0]) ** 2 + (b[1] - b[0]) ** 2) ** 0.5
    
    @staticmethod
    def calcMidPoint(xRange: tuple[int, int], yRange: tuple[int, int]) -> tuple[int, int]:
        return ((xRange[0] + xRange[1]) / 2, (yRange[0] + yRange[1]) / 2)