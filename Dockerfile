FROM occano/ds:pi
WORKDIR usr/src/app
COPY requirements.txt ./
RUN apt-get install -y llvm
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 5001
CMD [ "python3", "./server.py" ]
