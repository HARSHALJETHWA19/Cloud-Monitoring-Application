FROM python:3.9-slim-buster
WORKDIR /app
COPY requirement.txt .
RUN pip3 install --no-cache -r requirement.txt
COPY . .
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000
CMD ["flask", "run"]