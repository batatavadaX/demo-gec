FROM kalilinux/kali-rolling

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV PIP_NO_CACHE_DIR 1

WORKDIR /app/

RUN apt-get update && apt upgrade -y && apt-get install sudo -y
RUN apt -qq install -y --no-install-recommends \
    python3 \
    python3-dev \
    python3-pip 

COPY requirements.txt .

RUN pip install -U setuptools setuptools-scm wheel && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 6969

RUN rm okteto-stack.yml

CMD [ "bash", "./Creatus-est" ]
