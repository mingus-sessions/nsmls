#PREFIX=/usr/local
PROGRAM=nsmls
VERSION=0.0.1
CONFIG=src/config

.PHONY: clean install uninstall

all: nsmls 


nsmls: src/config/config.py
	python -m build

src/config/config.py:
	cp "$(CONFIG)/config.def.py" "$(CONFIG)/config.py"


install:
	pip install "dist/nsmls2-$(VERSION)-py3-none-any.whl"

uninstall:
	pip uninstall nsmls2



