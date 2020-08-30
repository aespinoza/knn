import math
from typing import List


class Vector(List[float]):
    @staticmethod
    def subtract(v: 'Vector', w: 'Vector') -> 'Vector':
        """Subtracts corresponding elements"""
        assert len(v) == len(w), "vectors must be the same length"

        return Vector([v_i - w_i for v_i, w_i in zip(v, w)])

    @staticmethod
    def dot_product(v: 'Vector', w: 'Vector') -> float:
        """Computes v_1 * w_1 + ... + v_n * w_n"""
        assert len(v) == len(w), "vectors must be same length"

        return sum(v_i * w_i for v_i, w_i in zip(v, w))

    def sum_of_squares(self) -> float:
        """Returns v_1 * v_1 + ... + v_n * v_n"""
        return self.dot_product(self, self)

    def magnitude(self) -> float:
        """Returns the magnitude (or length) of v"""
        return math.sqrt(self.sum_of_squares())

