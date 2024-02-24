# Installation instructions

Two flavours: with Docker or with Python Virtual Environment. Pick wichever you want.

## Docker

<https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run>
<https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/>
<https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file>
<https://github.com/dockerfile/ubuntu/blob/master/Dockerfile>

### Create the image

You should only need to to this once.

```bash
docker build -t sandbox_dl .
```

### Run the container

Execute in the directory where you have the files, the code you want to run.

```bash
# docker run -ti --rm -v ${PWD}:/app myimage
# docker run -ti --rm -v ${PWD}:/app

# interactive session, you will be dropped into the Docker container in CLI
docker run -ti -v ${PWD}:/app --rm --name test-container sandbox_dl
```

## Virtualenv

### Create a virtual environment for this project

* Install `apt-get install python3-venv`, this is necessary to create virtual environments with Python3.

```bash
sudo apt-get install python3-venv
```

* Create a virtual environment. Then activate the virtual environment.

```bash
python3 -m venv </path/to/new/virtual/environment>
source </path/to/new/virtual/environment>/bin/activate
```

I find it convenient in the the root of the project

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Clone the code

```bash
git clone <url>
```

### Install Python packages

Upgrade `pip` in the virtual environment

```bash
pip install --upgrade pip
```

Install the Python packages

```bash
pip install -r requirements.txt
```
