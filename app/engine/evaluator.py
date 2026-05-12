import math


class Evaluator:

    @staticmethod
    def precision_at_k(recommended, relevant, k=5):

        recommended_k = recommended[:k]

        hits = len(
            set(recommended_k).intersection(set(relevant))
        )

        return hits / k

    @staticmethod
    def recall_at_k(recommended, relevant, k=5):

        recommended_k = recommended[:k]

        hits = len(
            set(recommended_k).intersection(set(relevant))
        )

        return hits / len(relevant)

    @staticmethod
    def ndcg_at_k(recommended, relevant, k=5):

        dcg = 0

        for i, item in enumerate(recommended[:k]):

            if item in relevant:
                dcg += 1 / math.log2(i + 2)

        idcg = sum(
            1 / math.log2(i + 2)
            for i in range(min(len(relevant), k))
        )

        return dcg / idcg if idcg > 0 else 0