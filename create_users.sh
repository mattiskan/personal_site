#!/bin/sh
users_created_file="mongodb_data/_created_users"

if [ ! -e $users_created_file ]; then
    db_container_ip=$(docker inspect --format '{{ .NetworkSettings.IPAddress }}' "${PWD##*/}_db_1")

    if [ -z $db_container_ip ]; then
        echo "Error: no container running database was found."
        exit 1
    fi
    
    docker-compose run db mongo "$db_container_ip:27017" < create_users.cmd

    if [ $? -eq 0 ]; then
        docker-compose run db touch "/data/db/_created_users"
    fi
fi
