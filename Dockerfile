FROM python:3.8.2-alpine
WORKDIR /usr/src/app
COPY app.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /root/.aws
RUN echo "[default]" > /root/.aws/config
RUN echo "output = json" >> /root/.aws/config
RUN echo "region = us-east-1" >> /root/.aws/config
CMD ["python", "app.py"]
