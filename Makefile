#PREFIX=/usr/local
PROGRAM=nsmls2
VERSION=0.0.1

.PHONY: install uninstall

all: nsmls 


nsmls: src/config/config.py
	python -m build

src/config/config.py:
	cp "src/config/config.def.py" "src/config/config.py"


install:
	pip uninstall -y "$(PROGRAM)"
	pip install "dist/$(PROGRAM)-$(VERSION)-py3-none-any.whl"

uninstall:
	pip uninstall "$(PROGRAM)" 



