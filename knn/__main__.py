import knn
import click
from knn.knn import Knn
from typing import List, Set
from colorama.ansi import Fore
from knn.distance import EuclideanDistance
from knn.iris_data import IrisData, LabeledPoint
from knn.confusion_matrix import ClassificationReport


def classify(name: str, classifier: Knn, data_to_classify: List[LabeledPoint], unique_labels: Set[str], show_each_point: bool = False):
    if not data_to_classify:
        raise TypeError(f"Nothing to classify, the provided data set is empty.")

    click.echo(f"\n{Fore.GREEN}**** {name} **** {Fore.RESET}")
    report: ClassificationReport = ClassificationReport(unique_labels)

    for item in data_to_classify:
        predicted, confidence = classifier.classify(5, item.point)
        actual = item.label

        if show_each_point:
            click.echo(f"- {Fore.BLUE}{actual} [{item.point}]{Fore.RESET}: Predicted as {Fore.YELLOW}{predicted}{Fore.RESET} with {Fore.MAGENTA}{confidence}%{Fore.RESET} confidence.")

        report.append(actual, predicted)

    click.echo(f"\n{Fore.YELLOW}- Confusion Matrix:{Fore.RESET}")
    click.echo(report.create())
    click.echo(report.dump())


@click.command()
@click.version_option(version=knn.__version__, prog_name="knn")
def main():
    show_each_point: bool = False
    data: IrisData = IrisData()
    data.load("datasets/iris.data")
    unique_labels: Set[str] = data.get_unique_labels()
    train_data, validation_data, test_data = data.split(0.70, 0.30)

    classifier: Knn = Knn(train_data, distance=EuclideanDistance())

    classify("Validation Set", classifier, validation_data, unique_labels, show_each_point)
    #classify("Testing Set", classifier, test_data, unique_labels, show_each_point)


if __name__ == '__main__':
    main()
