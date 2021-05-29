up_dev:
	docker compose up -d web

down_dev:
	docker compose down

build_prod:
	docker build --target=prod -t flask_web .

run_prod:
	docker run -d --rm -p 5001:5000 --name flask_web flask_web:latest
