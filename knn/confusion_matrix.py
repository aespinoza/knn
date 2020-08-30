import json
from collections import defaultdict
from typing import Dict, Tuple, Optional, Set


class ConfusionMatrix(object):
    def __init__(self, label: str):
        self.tp: int = 0
        self.fp: int = 0
        self.fn: int = 0
        self.tn: int = 0

        self._label: str = label

    def append(self, true_label: str, predicted_label: str):
        if self._label == true_label:  # it is spam
            if true_label == predicted_label:  # we predicted spam
                self.tp += 1

            if true_label != predicted_label:  # we predicted not spam
                self.fn += 1

        else:  # it is not spam
            if self._label == predicted_label:  # we predicted spam
                self.fp += 1

            if self._label != predicted_label:  # we predicted not spam
                self.tn += 1

    def accuracy(self) -> float:
        return (self.tp + self.tn) / (self.tp + self.fp + self.fn + self.tn)

    def precision(self) -> float:
        return self.tp / (self.tp + self.fp)

    def recall(self) -> float:
        return self.tp / (self.tp + self.fn)

    def f1_score(self, precision: Optional[float] = None, recall: Optional[float] = None) -> float:
        if not precision:
            precision = self.precision()

        if not recall:
            recall = self.recall()

        return (2 * precision * recall) / (precision + recall)

    def dump(self):
        report: str = f"\n** {self._label}: \n" \
                      f"- TP: {self.tp}\n" \
                      f"- FP: {self.fp}\n" \
                      f"- TN: {self.tn}\n" \
                      f"- FN: {self.fn}\n" \
                      f"\n" \
                      f"- Accuracy: {self.accuracy()}\n" \
                      f"- Precision: {self.precision()}\n" \
                      f"- Recall: {self.recall()}\n" \
                      f"- F1 Score: {self.f1_score()}\n"

        return report


class ClassificationReport(object):
    def __init__(self, unique_labels: Set[str]):
        self._results: Dict[Tuple[str, str], int] = defaultdict(int)
        self._report: Dict[str, ConfusionMatrix] = {}

        for label in unique_labels:
            self._report[label] = ConfusionMatrix(label)

    def append(self, actual: str, predicted: str):
        t: Tuple[str, str] = (actual, predicted)
        self._results[t] += 1
        for key in self._report.keys():
            self._report[key].append(actual, predicted)

    def create(self):
        correct: Dict[str, int] = {}
        confused: Dict[str, int] = {}

        num_correct: int = 0
        num_confused: int = 0

        total: int = 0
        for item in self._results.keys():
            labels: str = str(item).replace("(", "").replace(")", "").replace("'", "")
            value: int = self._results[item]
            total += value
            if item[0] == item[1]:
                correct[labels] = value
                num_correct += value
            else:
                confused[labels] = self._results[item]
                num_confused += value

        result: Dict = {
            f"correct [{num_correct}/{total}]": correct,
            f"confused [{num_confused}/{total}]": confused
        }

        return json.dumps(result, indent=4, sort_keys=False)

    def dump(self):
        report: str = ""
        for key in self._report.keys():
            report += self._report[key].dump()

        return report
