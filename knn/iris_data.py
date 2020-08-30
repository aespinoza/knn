import csv
import random
import collections
from knn.linear_algebra import Vector
from typing import List, NamedTuple, Set, Tuple


class LabeledPoint(NamedTuple):
    point: Vector
    label: str


class IrisData(object):
    def __init__(self):
        self._data: List[LabeledPoint] = []

    def load(self, file_path: str):
        self._data = IrisData._parse_file(file_path)

    def data(self):
        return self._data

    def split(self, train_pct: float, validation_pct: float) \
            -> Tuple[List[LabeledPoint], List[LabeledPoint], List[LabeledPoint]]:
        data: List[LabeledPoint] = self._data
        random.shuffle(data)

        # 70 train, 20 validation, 10 test
        total_len: int = len(data)

        train_cut: int = int(total_len * train_pct)
        validation_cut: int = int(total_len * validation_pct) + train_cut

        train_set: List[LabeledPoint] = data[:train_cut]
        validation_set: List[LabeledPoint] = data[train_cut:validation_cut]
        testing_set: List[LabeledPoint] = data[validation_cut:]

        return train_set, validation_set, testing_set

    def get_unique_labels(self) -> Set[str]:
        labels: Set[str] = set([item.label for item in self._data])

        return labels

    @staticmethod
    def _parse_file(file_path: str) -> List[LabeledPoint]:
        with open(file_path, "r+") as f:
            rows: collections.Iterable = csv.reader(f)
            data: List[LabeledPoint] = [IrisData._parse_row(row) for row in rows]

        return data

    @staticmethod
    def _parse_row(row: List[str]) -> LabeledPoint:
        measurements: Vector = Vector([float(measurement) for measurement in row[:-1]])
        specie: str = row[-1].split("-")[-1]

        return LabeledPoint(measurements, specie)
