FROM python:3.6
WORKDIR /usr/src/app
RUN pip3 install -U Pillow --user
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /usr/src/app/
CMD [ "python3", "./server.py" ]
EXPOSE 5003
