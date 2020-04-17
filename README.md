# Docker with Flask REST API

## Docker Concept

- Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and deploy it as one package

- Docker is a popular virtualization tool that replicates a specific operating environment on top of a host OS. Each environment is called a container.

- A container uses an image of a preconfigured operating system optimized for a specific task. When a Docker image is launched, it exists in a container. For example, multiple containers may run the same image at the same time on a single host operating system.

- Docker integrates with Jenkins and Bamboo, too. If you use it together with one of these automation servers, you can further improve your delivery workflow. Besides, Docker is also great for cloud computing. In recent years, all major cloud providers such as AWS and Google Cloud added support for Docker. So, if you are planning a cloud migration, Docker can ease the process for you.

### Docker Engine

Docker Engine is a client-server application with these major components:

   - A server which is a type of long-running program called a daemon process (the dockerd command).

   - A REST API which specifies interfaces that programs can use to talk to the daemon and instruct it what to do.

   - A command line interface (CLI) client (the docker command).

   <img src ="flow.png">
   
### Docker Compose

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see the list of features.

### Prerequisites

    - A Linux-based operating system
    - Access to a user account with root or sudo privileges
    - A preconfigured Docker installation with images

### Set up your Docker environment

- First, install docker-engine by following the below link:
  
  https://docs.docker.com/install/linux/docker-ce/ubuntu/

- then, install docker compose :

  https://docs.docker.com/compose/install/

## Docker Hub

Docker Hub is a service provided by Docker for finding and sharing container images with your team. It provides the following major features:

- **Repositories:** Push and pull container images.
- **Teams & Organizations:** Manage access to private repositories of container images.
- **Official Images:** Pull and use high-quality container images provided by Docker.
- **Publisher Images:** Pull and use high- quality container images provided by external vendors. Certified images also include support and guarantee compatibility with Docker Enterprise.
- **Builds:** Automatically build container images from GitHub and Bitbucket and push them to Docker Hub.
- **Webhooks:** Trigger actions after a successful push to a repository to integrate Docker Hub with other services.


#### Dockers Basic Commands

- The basic format for using docker is:

      sudo docker command [options]

- To list all running Docker containers, enter the following into a terminal window:

      sudo docker ps

- To list all containers, both running and stopped, add –a :

      sudo docker ps -a

- To list containers by their ID use –aq (quiet):

      sudo docker ps -aq

- To list the total file size of each container, use –s (size):

      sudo docker ps -s

- To list the latest created containers, use –l (latest):

      sudo docker ps -l

###  Start Docker Container

The main command to launch or start a single or multiple stopped Docker containers is docker start:

     sudo docker start [options] container_id 

### Stop Docker Container

- Use the docker stop command to stop a container:

      sudo docker stop [option] container_id
    
- Replace container_id with the container’s name or ID.

- By default, you get a 10 second grace period. The stop command instructs the container to stop services after that period. Use the --time option to define a different grace period expressed in seconds:

      sudo docker stop --time=20 container_id

- To immediately kill a docker container without waiting for the grace period to end use:

      docker kill [option] container_id

To stop all running containers, enter the following:

docker stop $(docker ps –a –q)

The same command could be used with kill. This would stop all containers without giving them a chance to exit.

