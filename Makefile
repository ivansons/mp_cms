default: help
.default: help

BUILD_DIR = builds
VENV_DIR = venv
PIP_DIR = .pip
METADATA_DIR = .metadata
STATIC_DIR = public_html/static
VERSION_FILE = version.txt
VERSION_PY_FILE = project/settings/_version.py
REQUIREMENTS_FILE = requirements.txt

BIN_DIR = $(VENV_DIR)/bin
PIP_CMD = $(BIN_DIR)/pip
PYTHON_CMD = $(BIN_DIR)/python
SYS_PYTHON_CMD = $(shell which python2.7)
PIP_REQ_DIR = requirements
app_name = "mp_cms"
version = $(shell git describe --tags --long)
file_name = $(BUILD_DIR)/$(app_name)-$(version).tar.gz

info:
	@echo "BUILD_DIR=$(BUILD_DIR)"
	@echo "VERSION=$(version)"
	@echo "FILENAME=$(file_name)"
	@echo "SYS_PYTHON_CMD=$(SYS_PYTHON_CMD)"

clean:
	rm -rf $(BUILD_DIR)
	rm -rf $(STATIC_DIR)
	rm -rf $(VENV_DIR)
	rm -rf $(PIP_DIR)
	rm -rf $(METADATA_DIR)
	rm -rf $(VERSION_FILE)
	rm -rf $(REQUIREMENTS_FILE)

test:
	@echo "No tests, yet."

metadata:
	mkdir -p $(METADATA_DIR)
	lsb_release --all > $(METADATA_DIR)/lsb_release.txt
	hostname > $(METADATA_DIR)/hostname.txt
	git log -n 10 > $(METADATA_DIR)/git_log_10.txt
	git describe --all --long > $(METADATA_DIR)/git_describe.txt

venv:
	virtualenv --python=$(SYS_PYTHON_CMD) $(VENV_DIR)
	$(PIP_CMD) install -U pip

pip_download:
	mkdir -p $(PIP_DIR)
	$(PIP_CMD) -q download -d $(PIP_DIR) -r $(PIP_REQ_DIR)/server.txt

pip_install:
	$(PIP_CMD) install -f $(PIP_DIR) -r $(PIP_REQ_DIR)/server.txt

pip_freeze:
	cp $(PIP_REQ_DIR)/server.txt $(REQUIREMENTS_FILE)

django: venv pip_download pip_install pip_freeze
	rm -rf $(STATIC_DIR)
	@echo "MP_CMS_VERSION = '$(version)'" > $(VERSION_PY_FILE)
	DJANGO_SETTINGS_MODULE="project.settings.build" \
		$(PYTHON_CMD) manage.py compress
	DJANGO_SETTINGS_MODULE="project.settings.build" \
		$(PYTHON_CMD) manage.py collectstatic --noinput

build: metadata django
	mkdir -p $(BUILD_DIR)
	@echo "$(version)" > $(VERSION_FILE)
	tar -cvzf $(file_name) \
		--exclude="*.py?" \
		apps \
		project \
		public_html \
		static \
		templates \
		manage.py \
		$(REQUIREMENTS_FILE) \
		$(PIP_DIR) \
		$(METADATA_DIR) \
		$(VERSION_FILE)
	@echo $(file_name)

help:
	@echo "Please choose from one of the following:"
	@echo "    info            Show basic info of the build"
	@echo "    build           Create tar ball (gzipped) for deployment"
	@echo "    test            Run unit tests"
	@echo "    clean           Delete temporary directories"
	@echo "    help            This message"
