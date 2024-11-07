# Hiragana recognition model server
ML model code taken from [this repo](https://github.com/Nippon2019/Handwritten-Japanese-Recognition), licensed under the MIT license.

~~The Docker image is ~22GB of storage. There are probably ways to trim it down, but I'm not a sysadmin.~~ As of latest commit I don't think this is true anymore but I'm too busy with the prototype to check :P

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
There is also a `/ping` endpoint (GET) for health check purposes.

# Deployment

This assumes you have [Docker](https://www.docker.com/) installed, and the latest NVIDIA graphics drivers installed. Change port in `Dockerfile` (line 20), and in `compose.yaml` (line 5) as well if needed. Then, run

```
docker compose up --build
```

to build and start the server.

By default, *it is not prod-ready*.