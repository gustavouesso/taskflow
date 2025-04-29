FROM node:20-alpine
WORKDIR /usr/src/app
COPY package.json ./
COPY tsconfig.json ./
RUN npm install
COPY src ./src
RUN npx tsc
CMD ["node", "dist/main.js"]
