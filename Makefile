PY:=`which python`
VENV_PATH:="$$PWD/venv"

default:
	$(info no target)

deps:
	$(VENV_PATH)/bin/pip install -r requirements.txt

update:
	$(VENV_PATH)/bin/pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U

migrate:
	$(VENV_PATH)/bin/alembic upgrade head

run:
	$(VENV_PATH)/bin/python wsgi.py


.PHONY: default venv deps update migrate run
.SILENT:
