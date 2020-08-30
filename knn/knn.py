from typing import List
from knn.linear_algebra import Vector
from knn.iris_data import LabeledPoint
from knn.distance import EuclideanDistance, DistanceStrategy
from knn.voting import KReductionBasedMajorityVoting, VotingStrategy


class Knn(object):
    def __init__(self, data: List[LabeledPoint],
                 majority_voting: VotingStrategy = KReductionBasedMajorityVoting(),
                 distance: DistanceStrategy = EuclideanDistance()):
        self._data: List[LabeledPoint] = data
        self._majority_voting: VotingStrategy = majority_voting
        self._distance: DistanceStrategy = distance

    def classify(self, k: int, new_point: Vector) -> (str, int):
        distances: List[float] = []
        for item in self._data:
            distances.append(self._distance.measure(v=item.point, w=new_point))

        points_by_distance = sorted(self._data, key=lambda lp: self._distance.measure(v=lp.point, w=new_point))

        # Find the labels for the k closest
        k_nearest_labels = [point.label for point in points_by_distance[:k]]

        winner, vote_count = self._majority_voting.vote(k_nearest_labels)

        # Confidence
        confidence: float = vote_count * 100 / k

        return winner, confidence
