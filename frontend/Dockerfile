FROM node:21.7-alpine3.18 as build

WORKDIR /app
COPY . /app

RUN npm install
RUN npm run build

FROM nginx:1.21.3-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /var/www/html/
EXPOSE 80
CMD ["nginx","-g","daemon off;"]