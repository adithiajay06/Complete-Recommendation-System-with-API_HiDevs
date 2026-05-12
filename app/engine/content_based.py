from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ContentBasedEngine:

    def recommend(self, user_skills, contents, top_k=5):

        documents = [c.category for c in contents]

        vectorizer = TfidfVectorizer()
        matrix = vectorizer.fit_transform(documents)

        user_profile = " ".join(user_skills)

        user_vector = vectorizer.transform([user_profile])

        similarities = cosine_similarity(
            user_vector,
            matrix
        ).flatten()

        ranked = sorted(
            zip(contents, similarities),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]