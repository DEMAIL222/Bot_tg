FROM python:3.10-slim
ENV TOKEN='8058508687:AAFzN3IE_b5ZYhvyTmBqc8MeyjGEOONaUGw'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py"]