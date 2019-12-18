# Containers to test Kubernetes isolation

This repository contains code to create containers that test the isolation of Kubernetes or other container orchestrators. Typically, the containers in this repository excessively consume resources, which may affect other containers or processes running on the same host.

## Description

The following containers are available in this repository:

### cpuload

The `cpuload` container consumes all the CPU that it sees. It checks for the available cores and spawns a process for each core consuming CPU cycles.

### memoryeater

The `memoryeater` container consumes all memory resources. This will lead to the container typically being OOM killed by the orchestrator.

### forkbomb

The `forkbomb` container runs a script that forks infinitely. This creates new processes, potentially affecting other workload by using up system resources (e.g. PIDs).

### filedescriptors

The `filedescriptors` container opens as many file descriptors as possible. The file `/etc/hosts` is used to create the file descriptors. Typically, file descriptors are shared system-wide and not namespaced.

### entropy

The `entropy` container consumes randomness by repeatedly querying `/dev/random`. This will deplete the entropy pool for the kernel. Typically, entropy is system-wide and is not namespaced.

### logspam

The `logspam` container writes a lot of data to `stdout`. Depending on your configuration, this can overwhelm your logging stack or logging infrastructure.

## Usage

The containers in this repository are available as trusted builds on [Docker Hub](https://hub.docker.com/r/simonkrenger/).

To run these containers locally:

```
podman run simonkrenger/forkbomb
podman run simonkrenger/cpuload
podman run simonkrenger/memoryeater
podman run simonkrenger/filedescriptors
podman run simonkrenger/entropy
podman run simonkrenger/logspam
```

To run these containers on Kubernetes as a pod (example):

```
apiVersion: v1
kind: Pod
metadata:
  name: simonkrenger-cpuload
spec:
  containers:
  - name: cpuload
    image: simonkrenger/cpuload:latest
```
