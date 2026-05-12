class RecommendationExplainer:

    @staticmethod
    def generate(content, reason):

        return {
            "content_id": content.id,
            "title": content.title,
            "explanation": reason
        }