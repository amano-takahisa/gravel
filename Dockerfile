FROM ubuntu:latest

ARG UNAME=docker
ARG UID=1000
ARG GID=1000
ENV PATH="/home/${UNAME}/.local/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3-pip gdal-bin libgdal-dev python3-numpy python-is-python3 \
    make \
    && groupadd -g ${GID} -o ${UNAME} \
    && useradd -m -u ${UID} -g ${GID} ${UNAME} \
    && echo "${UNAME}:${UNAME}" | chpasswd \
    && passwd -d ${UNAME} \
    && adduser ${UNAME} sudo

USER ${UNAME}
WORKDIR /home/${UNAME}
COPY --chown=${UNAME}:${UNAME} . /home/${UNAME}/gravel/

RUN pip install -U pip \
    && pip install ./gravel[plot,test,dev]

CMD ["/bin/bash"]
