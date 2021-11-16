from typing import overload

class Utils():
    class LinearFunction():
        def __init__(self) -> None:
            self._m = float()
            self._b = float()
            self._fst = tuple(int(), int())
            self._scnd = tuple(int(), int())
            self._defined = False

        @overload
        def __init__(self, firstPoint: tuple[int, int], secondPoint: tuple[int, int]) -> None:
            try:
                self._m = (firstPoint[1] - secondPoint[1]) / (firstPoint[0] - secondPoint[0])
                self._b = firstPoint[1] - self._m * firstPoint[0]
                self._fst = firstPoint
                self._scnd = secondPoint
                self._defined = True
            except ZeroDivisionError:
                self._defined = False
                
    
    @staticmethod
    def calcDistance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return ((a[1] - a[0]) ** 2 + (b[1] - b[0]) ** 2) ** 0.5