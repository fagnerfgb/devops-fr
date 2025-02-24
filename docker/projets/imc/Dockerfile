FROM nginxinc/nginx-unprivileged:1.27-alpine3.21
EXPOSE 8080
LABEL author="Fagner Geraldes Braga"
LABEL contact="fagner.fgb@gmail.com"
COPY --chown=nginx:nginx . /usr/share/nginx/html
WORKDIR /usr/share/nginx/html
HEALTHCHECK --interval=5s --timeout=5s --start-period=30s --retries=3 CMD [ "curl","-f","http://localhost:8080/health.html" ]
USER nginx