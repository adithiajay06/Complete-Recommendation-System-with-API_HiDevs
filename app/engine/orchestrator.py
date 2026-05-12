from app.engine.content_based import ContentBasedEngine
from app.engine.cold_start import ColdStartEngine
from app.engine.explainer import RecommendationExplainer

from app.core.cache import recommendation_cache


class RecommendationOrchestrator:

    def __init__(self):

        self.content_engine = ContentBasedEngine()
        self.cold_engine = ColdStartEngine()

    def recommend(
        self,
        user,
        contents,
        interactions,
        user_skills,
        top_k=5
    ):

        cache_key = f"user:{user.id}"

        if cache_key in recommendation_cache:
            return recommendation_cache[cache_key]

        # Cold start users
        if len(interactions) == 0:

            recommendations = self.cold_engine.recommend(
                contents,
                top_k
            )

            results = [
                RecommendationExplainer.generate(
                    c,
                    "Trending content for new users"
                )
                for c in recommendations
            ]

            recommendation_cache[cache_key] = results

            return results

        # Content-based recommendations
        content_results = self.content_engine.recommend(
            user_skills,
            contents,
            top_k
        )

        final_results = []

        for content, score in content_results:

            final_results.append(
                RecommendationExplainer.generate(
                    content,
                    f"Recommended because of your interest in {content.category}"
                )
            )

        recommendation_cache[cache_key] = final_results

        return final_results