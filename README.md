# Complete Recommendation System with API

## Overview

This project is a production-ready recommendation system microservice built using FastAPI, SQLite, SQLAlchemy, and modular recommendation engine architecture.

The system provides:

* Personalized recommendations
* Cold-start handling
* Recommendation explanations
* REST API endpoints
* Request tracing and logging
* Evaluation metrics
* Concurrent load testing
* Caching for performance optimization

---

# Tech Stack

* Python 3
* FastAPI
* SQLite
* SQLAlchemy
* Scikit-learn
* Pytest
* CacheTools

---

# Project Architecture

```txt
app/
├── api/
│   ├── routes.py
│   └── schemas.py
│
├── core/
│   ├── cache.py
│   ├── logger.py
│   └── metrics.py
│
├── db/
│   ├── database.py
│   ├── models.py
│   ├── repositories.py
│   └── seed.py
│
├── engine/
│   ├── content_based.py
│   ├── cold_start.py
│   ├── evaluator.py
│   ├── explainer.py
│   └── orchestrator.py
│
├── tests/
│   ├── test_api.py
│   └── test_metrics.py
│
└── main.py
```

---

# Database Schema

## Tables

### Users

Stores user information.

### Skills

Stores user skills and preferences.

### Content

Stores recommendation content items.

### Interactions

Stores user-content interaction history.

---

# Recommendation Strategy

The recommendation engine uses:

* Content-based filtering
* Cold-start recommendation fallback
* Popularity-based ranking
* Recommendation explanation generation
* Caching layer for optimized performance

---

# API Endpoints

| Endpoint                   | Method | Description         |
| -------------------------- | ------ | ------------------- |
| /recommendations/{user_id} | GET    | Get recommendations |
| /feedback                  | POST   | Submit feedback     |
| /health                    | GET    | Health check        |
| /metrics                   | GET    | Performance metrics |

---

# API Example

## Get Recommendations

```http
GET /recommendations/1
```

### Response

```json
{
  "trace_id": "abc123",
  "response_time_ms": 78.2,
  "recommendations": [
    {
      "content_id": 4,
      "title": "Course 4",
      "explanation": "Recommended because of your interest in AI"
    }
  ]
}
```

---

# Setup Instructions

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Seed Database

```bash
python -m app.db.seed
```

## Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

---

# Swagger API Docs

```txt
http://localhost:8000/docs
```

---

# Evaluation Metrics

The system implements:

* Precision@5
* Recall@5
* NDCG@5

---

# Testing

Run unit tests:

```bash
pytest
```

---

# Load Testing

Run concurrent request simulation:

```bash
python load_test.py
```

### Performance Result

* Average response time: 78ms
* Concurrent users tested: 10

---

# Cold Start Handling

New users with no interaction history receive:

* Popular content recommendations
* Trending content suggestions

---

# Features

* Modular architecture
* Repository pattern
* Caching support
* Logging and request tracing
* Performance metrics
* REST API
* Recommendation explanations

---

# Demo Video

Add your YouTube demo link here:

```txt
https://youtu.be/kQqoyY_7gUI
```

---

# Future Improvements

* Redis caching
* PostgreSQL support
* Docker deployment
* JWT authentication
* Hybrid collaborative filtering
* Real-time recommendations

---

# Author

Adithi A
