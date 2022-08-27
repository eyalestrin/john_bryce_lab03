FROM python:3.8.2-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
WORKDIR /usr/src/app
COPY app.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /root/.aws
RUN echo "[default]" > /root/.aws/config
RUN echo "output = json" >> /root/.aws/config
RUN echo "region = ${REGION}" >> /root/.aws/config
CMD ["python", "-u", "app.py"]
