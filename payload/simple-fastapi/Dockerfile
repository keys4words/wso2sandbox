FROM registry.access.redhat.com/ubi8

RUN yum install python39 vim git sudo -y && \
    useradd keys4 && \
    echo "keys4:keys4" | chpasswd && \
    usermod -aG wheel keys4

USER keys4

WORKDIR /home/keys4

COPY . .

RUN pip3 install --user -r requirements.txt

CMD python3 main.py
