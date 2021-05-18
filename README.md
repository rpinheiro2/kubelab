<h1>Web-server Deployment</h1>

The present repository contains the source code of the deployment of a simple python web-server.
It was built using Docker Desktop 20.10.6 and Kubernetes v1.19.7, in a Windows 2010 Pro workstation.

<h1>Documentation</h1>

As requested,  the docker image was built locally, using the Docker Desktop. It´s possible to use `eval $(minikube docker-env)` to set docker-daemon locally using Minikube only in Linux, because this command doens´t work in Windows machines.

<h2>Creating the Docker image</h2>
The directory web-server (containing the files: app.py, requirements.txt and Dockerfile) must be copied to the local machine.
After that, you will run docker build --tag ecosia/python-docker:0.0.1, to build the  

<h2>Setting kubernetes manifest</h2>

In order to create the kubernetes resources you must copy the directory k8s (containing manifest_k8s.yaml) to the local machine.

To create resources run: kubectl apply -f .k8s\manifest_k8s.yaml, that will create and configure: namespace, deployment, service and ingress.

<h2>Testing</h2>

To the the deployment you can run curl -v local.ecosia.org/tree -H "host:local.ecosia.org" in a CMD prompt
