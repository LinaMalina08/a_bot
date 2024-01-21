run:
	#запустить приложение
	env $(cat .env | grep ^\[A-Z\] | xargs) python src/manage.py runserver

makemigrations:
	#переменные окружения берутся из .env и добавляются в терминал
	env $(cat .env | grep ^\[A-Z\] | xargs) python src/manage.py makemigrations app

migrate:
	#добавить таблицу в базу данных
	env $(cat .env | grep ^\[A-Z\] | xargs) python src/manage.py migrate

superuser:
	env $(cat .env | grep ^\[A-Z\] | xargs) python src/manage.py createsuperuser

runbot:
		env $(cat .env | grep ^\[A-Z\] | xargs) python src/manage.py runbot

rundb:
	docker compose up -d

stopdb:
	docker compose down
