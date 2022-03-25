FROM osgeo/gdal:ubuntu-small-latest

ENV USER docker
ENV PASS docker_pass

USER root
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m ${USER} && \
	gpasswd -a ${USER} sudo && \
	echo "${USER}:docker_pass" | chpasswd

USER ${USER}

WORKDIR /home/${USER}

COPY --chown=${USER}:${USER} dist dist
COPY --chown=${USER}:${USER} tests tests

# RUN python -m pip install -r gravel/requirements_dev.txt

# RUN python -m pip install -e gravel[test]

