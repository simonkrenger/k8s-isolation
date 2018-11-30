# Containers to test Kubernetes isolation

This repository contains code to create containers that test the isolation of Kubernetes. Typically, the containers in this repository excessively consume resources in order to influence other containers running on the same node.

## forkbomb

The `forkbomb` container runs a script that forks infinitely.
