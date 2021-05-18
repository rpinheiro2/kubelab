<h1>Documentation</h1>

The present repository contains the source code of the deployment of a simple python web-server.
It was built using Docker Desktop 20.10.6 and Kubernetes v1.19.7, in a Windows 10 Pro workstation.

<h1>Pre-requisites</h1>

As requested,  the docker image was built locally, using the Docker Desktop. It´s possible to use `eval $(minikube docker-env)` to set docker-daemon locally using Minikube only in Linux, because this command doens´t work in Windows machines.
So, you must copy the k8s (containing manifests-k8s.yaml) and python-docker (containing the files: app.py, requirements.txt and Dockerfile) directories to the local machine.

<h2>Deployment</h2>

With the directories copied to yhe local machine, run:

```
docker build --tag ecosia/python-docker:0.0.1 python-docker/. && \
kubectl apply -f k8s/manifests-k8s.yaml
```
This command will build the Docker image using the Dockerfile and deploy the k8s manifest, to create and configure: namespace, deployment, service and ingress.

<h2>Testing</h2>

To test the deployment you can run ```curl localhost/tree -H "host:local.ecosia.org"``` in a CMD prompt
