# Dockerfile to build nginx container images

FROM nginx:1.13.8-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./compose/nginx/nginx.conf /etc/nginx/conf.d/nginx.conf
