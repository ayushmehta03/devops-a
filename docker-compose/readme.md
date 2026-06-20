# Docker Compose

A tool developed by **Docker Inc.** for defining and managing multi-container applications.

## Overview

Docker Compose lets you describe an entire application stack — multiple containers, their configuration, and how they relate to each other — in a single YAML file. Instead of starting each container manually with long `docker run` commands, you define everything once and bring the whole stack up or down with a single command.

### Main use cases

- **Lifecycle and dependency management** — start, stop, and rebuild all the services that make up an application together, in the correct order.
- **Eliminating repetitive commands** — no need to manually re-type long, repetitive `docker run` flags for every container every time.

### How it fits with Docker

```
Dockerfile → docker compose → Docker → builds and runs containers
```

The `build` step in a `docker-compose.yml` file depends on a `Dockerfile`. Docker Compose reads the compose file, hands the build instructions to the Docker engine, and the engine builds the image and runs the resulting containers.

## Advantages

- **Local development efficiency** — spin up an entire multi-service environment with one command.
- **CI/CD support** — run the same stack locally that you test and deploy in your pipeline, ensuring consistency.
- **Testing** — quickly create and tear down isolated, reproducible environments for testing.

## Common components

| Component | Description |
|---|---|
| `services` | The containers to run — either pre-built images or custom images built from a Dockerfile. |
| `ports` | The port(s) on which the application is exposed/running. |
| `hostname` | A name that distinguishes one service/container from another on the network. |
| `depends_on` | Defines a startup dependency — a service only starts once the service(s) it depends on are running. |

## Example `docker-compose.yml`

```yaml
version: "3.9"

services:
  web:
    build: .
    ports:
      - "3000:3000"
    hostname: web
    depends_on:
      - api

  api:
    image: my-api-image
    ports:
      - "8080:8080"
    hostname: api
    depends_on:
      - db

  db:
    image: postgres:16
    ports:
      - "5432:5432"
    hostname: db
```

## Useful commands

```bash
# Build and start all services
docker compose up

# Start in detached (background) mode
docker compose up -d

# Stop and remove containers, networks
docker compose down

# Rebuild images before starting
docker compose up --build

# View logs from all services
docker compose logs -f
```