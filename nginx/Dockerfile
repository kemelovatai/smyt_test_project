FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/templates/nginx.conf.template

CMD ["nginx", "-g", "daemon off;"]