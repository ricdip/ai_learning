.POSIX:

PYTHON ?= python3
PIP ?= pip


.DEFAULT_GOAL: help

help:
	@printf "%s \\t\\t %s\n" "help" "show this help message"
	@printf "%s \\t\\t %s\n" "build" "init, install"
	@printf "%s \\t\\t %s\n" "init" "init venv"
	@printf "%s \\t %s\n" "install" "install requirements"
	@printf "%s \\t\\t %s\n" "run" "run game"
	@printf "%s \\t\\t %s\n" "clean" "clean venv files"

build: init install

.ONESHELL:
init:
	$(PYTHON) -m venv venv
	. venv/bin/activate
	$(PYTHON) -m pip install --upgrade pip

.ONESHELL:
install: venv
	. venv/bin/activate
	$(PIP) install -r requirements.txt

.ONESHELL:
run: venv
	. venv/bin/activate
	$(PYTHON) src/main.py

clean: venv
	rm -rf venv

.PHONY: help build init install run clean
