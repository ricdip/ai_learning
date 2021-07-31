.POSIX:

PYTHON ?= python3

PIP ?= pip

.DEFAULT_GOAL: help

help:
	@printf "%s \\t\\t %s\n" "help" "Show this help message"
	@printf "%s \\t\\t %s\n" "build" "Create Python virtual env"
	@printf "%s \\t\\t %s\n" "clean" "Clean virtual env"
	@printf "%s \\t\\t %s\n" "run" "Run main.py"
	@printf "%s \\t\\t %s\n" "all" "Build and run main.py"


.ONESHELL:
init:
	$(PYTHON) -m venv venv
	. venv/bin/activate
	$(PYTHON) -m pip install --upgrade pip

.ONESHELL:
install: venv
	. venv/bin/activate
	$(PIP) install -r requirements.txt

build: init install

clean: venv
	rm -rf venv

.ONESHELL:
.SILENT: run
run: venv
	. venv/bin/activate
	$(PYTHON) main.py

all: build run


.PHONY: help build clean run all
