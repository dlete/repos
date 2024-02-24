
# https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file

# Pull base image.
FROM ubuntu:16.04

# LABEL about the custom image
LABEL maintainer="daniel.lete@heanet.ie"
LABEL version="2020-12-12"
LABEL description="This is custom Docker Image for \
the sandobox_dl and CSD API."

# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#run
# Install.
#RUN \
#  apt-get update && \
#  #apt-get -y upgrade && \
#  apt-get install -y python3-venv  && \
#  apt-get install -y git htop vim && \
#  apt-get clean && \
#  rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-venv \
    python3-pip \
    git \
    htop \
    vim \
    # Official Debian and Ubuntu images automatically run apt-get clean, so explicit invocation is not required.
    # apt-get clean && \
&& rm -rf /var/lib/apt/lists/*

# Define working directory.
WORKDIR /app

# Install pip requirements
ADD requirements/development.txt .
#RUN pip3 install -r development.txt
RUN python3 -m pip install --upgrade pip && python3 -m pip install -r development.txt


# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
#RUN useradd appuser && chown -R appuser /app
#USER appuser

# Define default command.
CMD ["bash"]