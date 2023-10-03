build:
	docker compose build app;
bash: 
	docker compose run app bash;
run:
	docker compose -f down docker-compose.yml; docker compose -f docker-compose.yml run app;