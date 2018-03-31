FROM fedora:27

ADD . /code
RUN pip3 install -r requirements.txt
WORKDIR /code

CMD ["python3", "bot.py"]
