FROM ghcr.io/astral-sh/uv:0.4.16 AS uv
FROM tensorflow/tensorflow:2.14.0-gpu

# Env variables
ENV DEB_PYTHON_INSTALL_LAYOUT='deb'

RUN apt remove python3-blinker -y

# Full send everything to /server/ directory
WORKDIR /server

COPY requirements.txt ./

# https://github.com/astral-sh/uv/blob/main/docs/docker.md
RUN --mount=from=uv,source=/uv,target=/bin/uv \
    --mount=type=cache,target=/root/.cache/uv \
    PYTHONDONTWRITEBYTECODE=1 \
    uv pip install --system \
    -r requirements.txt

COPY models/ models/

COPY *.py ./

# Run on all addresses, port 5000
EXPOSE 5000
CMD [ "python", "app.py", "--host=0.0.0.0 --port=5000" ]