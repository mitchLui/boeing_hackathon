FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /workspace
ARG BUILD_DATE
LABEL org.opencontainers.image.create=$BUILD_DATE
ARG TITLE
LABEL org.opencontainers.image.title=$TITLE

COPY . ./

RUN \
pip3 install -U -r requirements.txt

EXPOSE 80
CMD [ "uvicorn","backend_api:app", "--host", "0.0.0.0", "--port", "80"]
