#!/bin/bash
docker run -d --hostname rmq --name rabbit-server --platform=linux/arm/v7 -p 8080:15672 -p 5672:5672 rabbitmq:3-management
