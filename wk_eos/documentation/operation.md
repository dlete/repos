# About this file
Operation instructions.

# Operate
## Normal day
This is what you do every day.

### Verify Docker is running
```bash
sudo service docker status
# or
docker run hello-world
```

### Start Docker
```bash
sudo service docker start
```
and verify again

### Verify the Docker images are available
```bash
docker images
```
Should display the Arista images (`arista/ceos:4.29.3M`) and the Containerlabs (`ghcr.io/srl-labs/clab`) images.

### Go to the containerlabs directory
```bash
cd <containerlabs_directory>
```

### Start containerlab
This is done by creating a Docker container from the containerlab image.
```bash
docker run --rm -it --privileged \
    --name container_containerlab \
    --network host \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /var/run/netns:/var/run/netns \
    -v /etc/hosts:/etc/hosts \
    -v /var/lib/docker/containers:/var/lib/docker/containers \
    --pid="host" \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    ghcr.io/srl-labs/clab bash
```
You will see that the prompt has changed. 

### Verify containerlab is running
Either by:
* Observing that the prompt has changed. 
* `docker ps` does render a running container with the name tag you gave it at the moment of creating it. 

### Deploy/launch a lab
```bash
containerlab deploy --topo <path_to_topology_file>
```
topology files must have the extension `*.clab.yml`
It will not bring the lab immediately. It may take about 1 minute (or more, depending on the number of containers).

### Connect to the nodes
```bash
docker exec -it <container_name> bash
# example
# docker exec -it clab-my_srlceos01-ceos1 bash
```

### Destroy the lab lab
```bash
containerlab destroy --topo <path_to_topology_file>
```



# Archive, daily routine
## Start the `dockerd` daemon
Starting the daemon directly does not seem to work (at least in an Ubuntu instance in WLS). I have found that what it works is this sequence. 
1. Stop the `dockerd` daemon
```bash
sudo start-stop-daemon -K -v --name dockerd
```

2. Start the `dockerd` daemon
```bash
sudo dockerd > /dev/null 2>&1 & disown
```

3. Verify the `dockerd` daemon has started
```bash
docker run hello-world
```


## Start the container
```bash
# map the host directory "$(pwd)/host_directory" (in your PC), to the directory "ansible" in the image"
docker run --rm -it -v $(pwd)/host_directory:/ansible_root dl_dockerfile_02 bash
docker run --rm -it -v $(pwd)/host_directory:/ansible_root dl_image_02 bash
```

This is the canonical way, through `dockercompose.yml` files:
```bash
docker-compose up -d
```


## Docker, connect to a running container
```bash
# for a server
docker exec -it <container_name> bash
# for an Arista
docker exec -it <container_name> Cli
docker exec -it ceos1 Cli
```

## Docker, restart containers
```bash
# restart container without loss configuration
docker-compose stop
```

## Docker, wipe out everything
```bash
# wipe out everything
docker-compose down
```

## Execute ansible commands
```bash
docker exec ceos_basic_01_my_ans_1 ansible localhost -m ping -i ansible_root/inventory.txt
```

## Execut ansible playbook
```bash
docker exec ceos_basic_01_my_ans_1 ansible-playbook <playbook_filename>
```