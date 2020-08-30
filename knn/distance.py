import math
from abc import ABC
from knn.linear_algebra import Vector


class DistanceStrategy(ABC):
    def measure(self, v: Vector, w: Vector) -> float:
        pass


class MinkowskiDistance(DistanceStrategy):

    def __init__(self, norm_order: int):
        if norm_order not in [2, 1]:
            raise TypeError("The selected norm order value is not supported. Supported: 1, 2")
        self._norm_order: int = norm_order

    def measure(self, v: Vector, w: Vector) -> float:
        v: float = Vector.subtract(v, w).sum_of_squares()

        if self._norm_order == 1:
            return v

        if self._norm_order == 2:
            return math.sqrt(v)


class EuclideanDistance(MinkowskiDistance):
    def __init__(self):
        super(EuclideanDistance, self).__init__(2)

    def measure(self, v: Vector, w: Vector) -> float:
        return super(EuclideanDistance, self).measure(v, w)


class ManhattanDistance(MinkowskiDistance):
    def __init__(self):
        super(ManhattanDistance, self).__init__(1)

    def measure(self, v: Vector, w: Vector) -> float:
        return super(ManhattanDistance, self).measure(v, w)