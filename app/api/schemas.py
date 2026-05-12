from pydantic import BaseModel


class FeedbackRequest(BaseModel):
    user_id: int
    content_id: int
    interaction_type: str
    rating: float