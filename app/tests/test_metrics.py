from app.engine.evaluator import Evaluator


def test_precision():

    recommended = [1, 2, 3, 4, 5]
    relevant = [1, 3, 5]

    precision = Evaluator.precision_at_k(
        recommended,
        relevant
    )

    assert precision == 0.6


def test_recall():

    recommended = [1, 2, 3, 4, 5]
    relevant = [1, 3, 5]

    recall = Evaluator.recall_at_k(
        recommended,
        relevant
    )

    assert recall == 1.0