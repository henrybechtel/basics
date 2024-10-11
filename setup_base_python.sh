# Port mapping: Map port 1 on the Docker host (your machine) to TCP port 2 in the container.
# For volume mapping, use "/" on mac and linux and "\" on windows.
# Run the container from the bash shell with 
docker run -it \
    --name base_python_container \
    -v ./code:/code \
    -v ./data:/data \
	python bash
