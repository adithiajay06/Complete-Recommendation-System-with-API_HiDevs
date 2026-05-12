from sqlalchemy.orm import Session

from app.db.models import User, Content, Interaction


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        return self.db.query(User).filter(
            User.id == user_id
        ).first()


class ContentRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_content(self):
        return self.db.query(Content).all()


class InteractionRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_user_interactions(self, user_id: int):

        return self.db.query(Interaction).filter(
            Interaction.user_id == user_id
        ).all()