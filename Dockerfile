FROM ubuntu:18.04
RUN apt update -y

ENV FLASK_APP index.py
ENV LC_ALL 'C.UTF-8'
ENV LANG 'C.UTF-8'

RUN apt install -y  python3-pip \
                    python3-dev \
                    build-essential \
                    vim \
                    default-libmysqlclient-dev

WORKDIR /var/www/app
COPY requirements.txt .

RUN pip3 install -r requirements.txt
COPY . .

CMD ["nc", "-l", "-p", "2727"]
