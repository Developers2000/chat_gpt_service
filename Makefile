build:
	docker compose build app;
bash: 
	docker compose run app bash;
run:
	docker compose down; docker compose up;
dev:
	uvicorn app.main:app --reload;
virtual:
	chmod u+x ./venv.sh; ./venv.sh;