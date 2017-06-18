#
# CSS Inliner
#

# Database Settings
SHELL=/bin/bash
BASE_GIT_DIR=/git
OSX_PIP_OPTS=

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Darwin)
        OSX_PIP_OPTS += --global-option=build_ext --global-option="-I/usr/local/opt/openssl/include/" --global-option="-L/usr/local/opt/openssl/lib/"
endif

prepare_env: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install $(OSX_PIP_OPTS) -U -I -r requirements.txt
	touch venv/bin/activate

clean:
	find . -name "*.pyc" -exec rm '{}' ';'

