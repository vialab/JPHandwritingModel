FROM ghcr.io/astral-sh/uv:latest AS uv
FROM tensorflow/tensorflow:latest

# Env variables
ENV DEB_PYTHON_INSTALL_LAYOUT='deb'

WORKDIR /server

# Python project files
COPY requirements.lock ./
COPY pyproject.toml ./

# logging config
COPY log_conf.yaml ./

# remove constraints from constraint file
# the constraints, in this case, are editable requirements
RUN sed -ir 's/^-e /# -e /g' requirements.lock

# https://github.com/astral-sh/uv/blob/main/docs/docker.md
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    PYTHONDONTWRITEBYTECODE=1 \
    uv pip install --system \
    --constraint requirements.lock \
    -e .

COPY models/ models/

COPY *.py ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000", "--log-config=log_conf.yaml"]
