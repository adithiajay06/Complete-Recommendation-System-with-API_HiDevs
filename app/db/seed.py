from faker import Faker
import random

from app.db.database import SessionLocal, engine
from app.db.models import Base, User, Content, Skill, Interaction

fake = Faker()

Base.metadata.create_all(bind=engine)

db = SessionLocal()

categories = [
    "AI",
    "Web Development",
    "Cloud",
    "Cybersecurity",
    "Data Science"
]

skills = [
    "python",
    "docker",
    "ml",
    "sql",
    "react",
    "aws"
]

for i in range(10):
    user = User(
        name=fake.name(),
        experience_level=random.choice(["beginner", "intermediate", "advanced"])
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    for _ in range(3):
        db.add(
            Skill(
                user_id=user.id,
                skill_name=random.choice(skills)
            )
        )

for i in range(20):
    content = Content(
        title=f"Course {i}",
        category=random.choice(categories),
        difficulty=random.choice(["easy", "medium", "hard"]),
        popularity_score=random.uniform(1, 5)
    )

    db.add(content)

db.commit()

for _ in range(50):
    interaction = Interaction(
        user_id=random.randint(1, 10),
        content_id=random.randint(1, 20),
        interaction_type=random.choice(["view", "click", "like"]),
        rating=random.uniform(1, 5)
    )

    db.add(interaction)

db.commit()

print("Database seeded successfully")