# Makefile

.PHONY: all venv activate install_env copy_env docker

all: venv activate install_env copy_env docker

venv:
	python -m venv venv

activate:
	@echo "To activate the virtual environment, run:"
	@echo "source venv/bin/activate"  # On Windows, use `venv\Scripts\activate`

install_env: venv
	venv/bin/pip install -r requirements.txt  # On Windows, use `venv\Scripts\pip install -r requirements.txt`

copy_env:
	cp .env.template .env

docker:
	docker-compose up --build
