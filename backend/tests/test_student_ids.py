import os
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from sqlalchemy.schema import CreateSchema, DropSchema

from app.database import Base, engine as application_engine, get_db
from app.main import app
from app.models.student import HealthProfile, Student


@pytest.fixture
def client():
    schema = None
    if os.getenv("RUN_POSTGRES_TESTS") == "1":
        assert application_engine is not None
        schema = "student_id_test_" + uuid4().hex
        engine = create_engine(
            application_engine.url,
            execution_options={"schema_translate_map": {"public": schema}},
        )
        with engine.begin() as connection:
            connection.execute(CreateSchema(schema))
    else:
        engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
            execution_options={"schema_translate_map": {"public": None}},
        )

    tables = [Student.__table__, HealthProfile.__table__]
    Base.metadata.create_all(engine, tables=tables)

    def test_db():
        with Session(engine) as db:
            yield db

    app.dependency_overrides[get_db] = test_db
    try:
        with TestClient(app) as client:
            yield client
    finally:
        app.dependency_overrides.pop(get_db, None)
        if schema:
            with engine.begin() as connection:
                connection.execute(DropSchema(schema, cascade=True))
        engine.dispose()


@pytest.mark.parametrize("student_id", ["DEMO-025", "demo_026", "025", "A"])
def test_accepted_id_can_be_created_read_and_updated(client, student_id):
    payload = {"id": student_id, "full_name": "Synthetic Student", "class_name": "6A1"}
    created = client.post("/students", json=payload)
    assert created.status_code == 201, created.text
    assert client.get(f"/students/{student_id}").json()["id"] == student_id

    changed = client.patch(f"/students/{student_id}", json={"medical_notes": "Saved"})
    assert changed.status_code == 200, changed.text
    assert client.get(f"/students/{student_id}").json()["medical_notes"] == "Saved"


@pytest.mark.parametrize("student_id", [
    "DEMO/025", "DEMO%2F025", "DEMO?025", "DEMO#025", "DEMO 025",
    "DEMO\\025", ".", "ĐEMO-025", "A" * 51,
])
def test_unsafe_id_is_rejected_without_creating_a_student(client, student_id):
    response = client.post("/students", json={
        "id": student_id, "full_name": "Synthetic Student", "class_name": "6A1",
    })
    assert response.status_code == 422, response.text
    assert client.get("/students").json() == []
