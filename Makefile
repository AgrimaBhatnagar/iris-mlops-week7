.PHONY: test build run kind-load k8s-apply hpa-apply

APP_NAME=iris-api
IMG=ghcr.io/${GITHUB_USER}/${APP_NAME}:$(shell git rev-parse --short HEAD)

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8080

test:
	pytest -q

build:
	docker build -t $(APP_NAME):local .

kind-load: build
	kind load docker-image $(APP_NAME):local --name iris

k8s-apply:
	kubectl apply -f k8s/deployment.yaml -f k8s/service.yaml

hpa-apply:
	kubectl apply -f k8s/hpa.yaml
