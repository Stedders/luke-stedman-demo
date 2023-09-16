FROM python:3.11 AS builder

WORKDIR /opt/dashboard

RUN pip install pip -U && pip install poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

COPY ./poetry.lock .

COPY ./pyproject.toml .

RUN poetry install --no-root --with dashboard -vvv

FROM python:3.11 AS dashboard-runner

LABEL authors="stedders"

COPY --from=builder /opt/dashboard /opt/dashboard

ENV PATH="$PATH:/opt/dashboard/.venv/bin"

WORKDIR /opt/dashboard

COPY stedders/ ./stedders/

CMD streamlit run ./stedders/dashboard/Home.py




