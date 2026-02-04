# `Docker Fundamentals`
## Why we need `docker`?
01. Makes it easy to `setup` project locally.
02. `Dockerize` your own app.
03. Learning to `deploy` via `Docker`
    - `Dockerfile`
    - `docker-compose.yml` 

## Why `Containarization` ?
01. Everyone has different `operating` system.
02. Steps to run a project can vary based on `OS`.
03. Extremely harder to keep track of `dependencies` as project grows.
04. What is there was a way to describe your projects configuration in a **single** file `?`
05. What if that could be run in an `isolated` environment `?`
06. Makes local setup of `OS` projects a breeze.
07. Makes installing `auxiliary` services `[Ex: DB, Redis]` easy.

## The Problem `Docker` Solves
- Everyone has different `operating` system. Example: `Linux`, `Window`, `Mac`.
- The way to install `node.js` or `python` or `Django` on `Mac` machine it's completely different in `Windows` machine.
- There are other dependencies such as `Database`, `Kafka` these needs to setup separately which is different for every `operating` system.
- Every developer on a team may use a different OS, requiring individual environment configuration.
- What if we could write all these in a `single file`?
    - **The Solution** is `Dockerfile` 
- Irrespects of whether you're on `Mac`, `Windows` or `Linux` machine you all have to just run a single commad and which will be same for everyone `(Mac, Windows or Linux)`
- **Docker is one way of containarization**
- `Containarization` involves building self sufficiant software packages that perform consistently, regardless of the `machines` they run on.
- **It's basically taking the snapshot of a machine, the filesystem and letting you use and deploy it as a construct**

## why `Docker` ?
- Makes your life easy when you're setting up project locally.
- Makes it easier to deploy `containers`. 
- Allows for `container orchestration` which makes `deployment` a breeze. `[Kubernetes]`

## Inside `Docker`
- `Docker` has 3 parts
    - `CLI`
    - `Engine`
    - `Registry` (Dockerhub)

![Inside Docker](media/docker_part.png)
- Instead of `code` `DockerHub` contains `images` that are going to be deployed.
- Once a developer created an image, they can deploy it to `dockerhub`.
- `AWS`, `GCP` can pull your image from the `Dockerhub` and run it immediately.
- **DockerHub isn't the only registry**
    - `AWS`, `GCP` both of them has their own registry.
    - **DockerHub is the most popular registry**