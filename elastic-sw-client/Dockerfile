FROM python:alpine
EXPOSE 8080
RUN /bin/sh
RUN pip install elasticsearch
COPY upload_logs.py .
COPY upload_diagnostics.py .
COPY search.py .
COPY update.py .
COPY delete.py .
CMD sleep 10000000
