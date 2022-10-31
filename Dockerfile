# Pull a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade

# Add Tini
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT [ "/tini", "--"]

# create directory for the app user
WORKDIR /source

COPY setup.py README.md run.sh /source/

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir --compile --editable .

# copy project
COPY . .

RUN chmod +x run.sh

# Open a port on the container
EXPOSE 8000


# run run.sh
CMD ["/source/run.sh"]