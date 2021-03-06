# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.6

RUN set -ex && apt-get update && apt-get install -y \
     less \
     vim \
     emacs \
     curl \
     zsh \
     tmux \
     htop \
     man \
     wget \
     cmake \
     byobu \
     unzip \
     git \
     libgtk2.0-dev \
     libjpeg-dev \
     libpng-dev \
     libtiff-dev

# Copy local code to the container image.
# ENV APP_HOME /app
ARG project_dir=/home/work/
# WORKDIR $APP_HOME
COPY . .

ADD requirements.txt $project_dir

# Change Timezone to JP
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

# Install production dependencies.
RUN pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib pandas \
    && curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /app/google-cloud-sdk.tar.gz  \
    && mkdir -p /usr/local/gcloud \
    && tar -C /usr/local/gcloud -xvf /app/google-cloud-sdk.tar.gz \
    && /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

# other package
WORKDIR $project_dir
RUN pip install -r requirements.txt

CMD ["python" "main.py"]