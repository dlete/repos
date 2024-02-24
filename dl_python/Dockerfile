
# https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file

# Pull base image.
FROM ubuntu:16.04

# LABEL about the custom image
LABEL maintainer="daniel.lete@heanet.ie"
LABEL version="2020-12-14"
LABEL description="This is custom Docker Image for \
with Ubuntu 16.04, python 3.5 and pyez."

RUN \
    apt-get update && apt-get install -y \
    git \
    htop \
    python3-pip \
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
RUN useradd appuser && chown -R appuser /app
ADD .vimrc /home/appuser/
RUN chown -R appuser /home/appuser
USER appuser

# Define default command.
CMD ["bash"]