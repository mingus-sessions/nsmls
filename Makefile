#PREFIX=/usr/local
PROGRAM=nsmls
VERSION=0.0.1
CONFIG=src/config

.PHONY: clean install uninstall


"$(CONFIG)/config.py":
	cp "$(CONFIG)/config.def.py" "$(CONFIG)/config.py"

all:
	python -m build

clean:
	# remove config.py?

install:
	pip install "dist/nsmls2-$(VERSION)-py3-none-any.whl"

uninstall:
	pip uninstall nsmls2



