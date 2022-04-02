FROM python:3.7
ADD . /code
WORKDIR /code
RUN apt-get update
RUN apt install -y libgl1-mesa-glx
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=0
#COPY . .
#COPY ./entrypoint.sh .
#RUN chmod +x /usr/src/app/entrypoint.sh
CMD python3 app.py