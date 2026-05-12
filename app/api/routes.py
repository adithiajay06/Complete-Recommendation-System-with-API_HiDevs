from app.db.models import Interaction
from app.api.schemas import FeedbackRequest
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.repositories import (
    UserRepository,
    ContentRepository,
    InteractionRepository
)

from app.engine.orchestrator import RecommendationOrchestrator

from app.core.logger import logger, generate_trace_id
from app.core.metrics import (
    metrics_store,
    MetricsCollector
)

router = APIRouter()

engine = RecommendationOrchestrator()


@router.get("/recommendations/{user_id}")
def get_recommendations(
    user_id: int,
    db: Session = Depends(get_db)
):

    trace_id = generate_trace_id()

    metrics = MetricsCollector()
    metrics.start()

    logger.info(f"Trace={trace_id} Request started")

    user_repo = UserRepository(db)
    content_repo = ContentRepository(db)
    interaction_repo = InteractionRepository(db)

    user = user_repo.get_user(user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    contents = content_repo.get_all_content()

    interactions = interaction_repo.get_user_interactions(
        user_id
    )

    skills = [
        skill.skill_name
        for skill in user.skills
    ]

    recommendations = engine.recommend(
        user,
        contents,
        interactions,
        skills
    )

    elapsed = metrics.stop()

    logger.info(
        f"Trace={trace_id} completed in {elapsed:.2f}ms"
    )

    return {
        "trace_id": trace_id,
        "response_time_ms": elapsed,
        "recommendations": recommendations
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@router.get("/metrics")
def get_metrics():
    return metrics_store
@router.post("/feedback")
def submit_feedback(
    payload: FeedbackRequest,
    db: Session = Depends(get_db)
):

    interaction = Interaction(
        user_id=payload.user_id,
        content_id=payload.content_id,
        interaction_type=payload.interaction_type,
        rating=payload.rating
    )

    db.add(interaction)
    db.commit()

    return {
        "message": "Feedback recorded"
    }