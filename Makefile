#PREFIX=/usr/local
PROGRAM=nsmls
VERSION=0.0.1

.PHONY: clean install uninstall

all:
	# copy config.def.h to config.py if config.py not available
	python -m build

clean:
	# remove config.py?

install:
	pip install "dist/nsmls2-$(VERSION)-py3-none-any.whl"

uninstall:
	pip uninstall nsmls2



