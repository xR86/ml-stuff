# ml-stuff
##Tensorflow

**Prerequisites**:
- Install Docker

**Set-up** (Windows):
<!-- - Run `docker-machine start` -->
- Run `docker-bash.bat` or `docker-cmd.bat` - prefferably bash
- Navigate in Docker Bash to this folder
- Run `docker build -t "tensorflow" .`
- Run `docker run -p 8888:8888 tensorflow`
- Manually add port forwarding rule  **OR** Run `VBoxManage modifyvm "default" --natpf1 "tensorflow,tcp,0.0.0.0,8888,,8888"` (in which context ? cmd, bash, boot2docker ssh ?)
- Check with `ipconfig` the address of the docker-machine, and access that port on that IP (eg: something like `http://192.168.0.10x:8888/tree`)
- Open the notebook (`1_hello_tensorflow.ipynb`)

- You can check the container name through `docker ps [-a]`
- If needed, connect with ssh to the container through `docker exec -it <container-name> bash`
- To bring your file from the docker container to this folder, run `docker cp <container-name>:/notebooks/1_hello_tensorflow.ipynb
 ./`


###Useful links

- Tensorflow installation guide [here](https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip-installation)
- Tensorflow box reference [here](https://hub.docker.com/r/tensorflow/tensorflow/)
- Visualization - intro to neural networks: [github.com/tensorflow/playground](https://github.com/tensorflow/playground)

