add /etc/hosts  
`127.0.0.1 db.lan, redis.lan`  

env  
`poetry install`  

run  
`docker-compose up -d`  
`python manage.py makemigrations`  
`python manage.py migrate`  

db
`python manage.py loaddata db.json`  

login `folt`  
pass `1`  
