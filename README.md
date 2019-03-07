# Docker Basics
Building application with 3 services: A, B and C.

A: Generates M square matrices of order N of random numbers. The matrices should be generated at a rate of F matrices per second. Sends the results to B.

B: Inverts the input matrix and calculates determinant. Sends the results to C.

C: Receives the value of the determinant and shows on the screen.

Each service must run in a different container.
## Installation
First of all you need to install docker. Go to [Oficial page](https://docs.docker.com/cs-engine/1.13/) for more details about installation.

## Image
Once you have docker installed, you can get the image of this aplication from my repository on Docker Hub.
```bash
docker pull luizcarloscf/servers-socket
```
Or you can build the image.
```bash
docker build --tag=servers-socket .
```
## Network
Create our user-definied network.
```bash
docker network create my-net
```
## Containers
Run the container that shows the results.
```bash
docker run --network=my-net servers-socket python3 result.py port=80
```
Run the container that calculate the determinant and forward the messages.
```bash
docker run -d --network=my-net servers-socket python3 forward-det.py port_on=80 port_to=80
```
Run the container that generate the matrix.
```bash
docker run --network=my-net servers-socket python3 generate-matrix.py port=80 m=1 n=10 f=2
