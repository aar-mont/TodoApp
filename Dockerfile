FROM node:18.15

RUN mkdir -p /home

COPY . /home

EXPOSE 8080

CMD ["node", "/home/server.js"]
