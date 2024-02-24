FROM python:3.11.2
	RUN apt-get update -y && apt-get upgrade -y
	WORKDIR /app
	COPY ./requirements.txt ./
	RUN pip install -r requirements.txt
	COPY ./store ./store
	CMD ["bash", "-c", "./store/manage.py makemigrations && ./store/manage.py migrate && ./store/manage.py runserver 0.0.0.0:8009"]