FROM node:22-alpine

COPY package*.json ./
COPY .npmrc* ./
COPY .yarnrc.yml* ./



RUN npm ci --only=production

COPY ./server.js ./

CMD ["npm", "start"]