FROM registry.fedoraproject.org/fedora:34
LABEL maintainer="Simon Krenger <simon@krenger.ch>"

WORKDIR /usr/src/app
COPY consume_entropy.py .

CMD [ "/usr/bin/python3", "-u", "./consume_entropy.py"]
