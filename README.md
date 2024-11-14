# Hiragana recognition model server
ML model code taken from [this repo](https://github.com/Nippon2019/Handwritten-Japanese-Recognition), licensed under the MIT license.

Meant to be used primarily with the [KikuKaku](https://github.com/vialab/JPHandwriting) Unity VR application.

# Usage

The API has only one useful endpoint: `/predict`. It accepts a multipart form with the body as follows:

|Key|Method|Information|Format|
|---|---|---|---|
|img|POST|The image containing a handwritten Hiragana character.|jpg or png image|

The API sends a response in JSON format. Here is a sample response:
```json
{
    "romaji": "a",
    "prediction": "あ"
}
```
There is also a `/ping` endpoint (GET) for health check purposes. The API sends this response if this endpoint is reached:
```json
{
    "status": "OK"
}
```

# Local Setup

This repository uses [Rye](https://rye.astral.sh) to manage Python packages. You can either set this repository up with Rye (recommended) or pip.

## Installing packages

### With `rye`

Clone this repository. In the project's root, run

```sh
rye sync
```

to set up the project.

### With `pip`

Clone this repository. In the project's root, run

```sh
pip install -r requirements-dev.lock
```

to set up the project. Note that pip is installing from `requirements-dev.lock` and not `requirements.lock` -- this is because I have set Tensorflow as a developer requirement so my linter (Ruff) knows I'm developing with Tensorflow without actually installing the package. (Docker is already set up with the `tensorflow/tensorflow` image.)

## Starting the server

After dependencies have been installed, simply run

```sh
fastapi dev main.py
```

in the project root. The API will be available on port 8000.

# Deployment

This assumes you have [Docker](https://www.docker.com/) installed, and the latest NVIDIA graphics drivers installed. Change port in `Dockerfile` (line 20), and in `compose.yaml` (line 5) as well if needed. Then, run

```
docker compose up --build
```

to build and start the server.
