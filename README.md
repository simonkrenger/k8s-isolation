# Containers to test Kubernetes isolation

This repository contains code to create containers that test the isolation of Kubernetes. Typically, the containers in this repository excessively consume resources in order to influence other containers running on the same node.

## Description

The following containers are available in this repository:

### forkbomb

The `forkbomb` container runs a script that forks infinitely. This creates new processes, potentially affecting other workload by using up system resources.

### cpuload

The `cpuload` container consumes all the CPU that it sees. It checks for the available cores and spawns a process for each core consuming CPU cycles.

### memoryeater

The `memoryeater` container consumes all memory resources. This will lead to the container typically being OOM killed by the orchestrator.

### filedescriptors

The `filedescriptors` container opens file descriptors in a loop. The file `/etc/hosts` is used to create the file descriptors. Typically, file descriptors are shared system-wide and not namespaced - this can lead to other processes being affected

## Usage

The containers in this repository are available as trusted builds on Docker Hub: https://hub.docker.com/r/simonkrenger/

To run these containers locally:
```
docker run simonkrenger/forkbomb
docker run simonkrenger/cpuload
docker run simonkrenger/memoryeater
docker run simonkrenger/filedescriptors
```

To run these containers on Kubernetes as a pod:
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
