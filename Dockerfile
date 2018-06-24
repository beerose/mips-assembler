FROM python:2

COPY ./*.py ./workdir/
WORKDIR ./workdir

COPY requirements.txt ./
COPY tests/*.py ./
COPY tests/*.in ./tests/

RUN pip install --no-cache-dir -r requirements.txt
