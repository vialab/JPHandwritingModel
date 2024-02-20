# Hiragana recognition model server
ML model code taken from [this repo](https://github.com/Nippon2019/Handwritten-Japanese-Recognition), licensed under the MIT license.

The Docker image is ~22GB of storage. There are probably ways to trim it down, but I'm not a sysadmin.

# Deployment

This assumes you have [Docker](https://www.docker.com/) installed, and the latest NVIDIA graphics drivers installed. Change port in `Dockerfile` (line 20), and in `compose.yaml` (line 5) as well if needed. Then, run

```
docker-compose up
```

to build and start the server.

By default, *it is not prod-ready, and also uses the default Flask dev port (5000)*.