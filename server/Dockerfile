FROM python:3
WORKDIR /server
COPY . /server
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python", "./app.py"]
