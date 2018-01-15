FROM python:3-onbuild
# Update the sources list
RUN apt-get update

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

# Get pip to download and install requirements:
RUN pip install -r requirements.txt

COPY . /usr/src/app

EXPOSE 5000
CMD python block.py