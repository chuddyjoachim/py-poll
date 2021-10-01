FROM python:3.8 as base

# Setup env
ENV PYTHONNUNBUFFERED=1

# Based on https://sourcery.ai/blog/python-docker/
FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Running as the root user is a security risk, so we create a new user and use their home directory as the working directory:
# Create and switch to a new user
RUN useradd --create-home appuser
USER appuser

# FastAPI config
ENV PORT=8000
ENV PYTHONPATH=/app
EXPOSE $PORT

# Install application into container
WORKDIR /
COPY . ./app

CMD ["uvicorn", "app.main:app", "--reload"]