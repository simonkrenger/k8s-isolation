FROM python:3.7-slim
LABEL maintainer="Simon Krenger <simon@krenger.ch>"

WORKDIR /usr/src/app
COPY consume_entropy.py .

CMD [ "python", "-u", "./consume_entropy.py"]
