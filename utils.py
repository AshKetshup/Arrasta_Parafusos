from typing import overload

class Utils():
    @staticmethod
    def calcDistance(a: tuple[int, int], b: tuple[int, int]) -> int:
        return ((a[1] - a[0]) ** 2 + (b[1] - b[0]) ** 2) ** 0.5
    
    @staticmethod
    def calcMidPoint(xRange: tuple[int, int], yRange: tuple[int, int]) -> tuple[int, int]:
        return ((xRange[0] + xRange[1]) / 2, (yRange[0] + yRange[1]) / 2)