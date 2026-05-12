class ColdStartEngine:

    def recommend(self, contents, top_k=5):

        ranked = sorted(
            contents,
            key=lambda x: x.popularity_score,
            reverse=True
        )

        return ranked[:top_k]