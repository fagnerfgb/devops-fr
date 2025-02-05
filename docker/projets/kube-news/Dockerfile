FROM node:23.7.0-alpine3.20
LABEL author="Fagner Geraldes Braga"
LABEL contact="fagner.fgb@gmail.com"
WORKDIR /app
COPY --chown=node:node package*.json .
RUN npm install
COPY --chown=node:node . .
EXPOSE 8080
CMD [ "node", "server.js" ]
USER node