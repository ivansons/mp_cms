PS1="\[\e[0;32m\]\u\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[1;32m\]$\[\e[m\] \[\e[1;37m\]"
export PROJECT_DIR="/mp_cms"
export DJANGO_SETTINGS_MODULE="project.settings.dev"
export PGHOST="localhost"
export PGPORT="5432"
export PGDATABASE="mp_cms"
export PGUSER="mp_cms"
export PGPASSWORD="matterport"
alias ll="ls -l"
alias la="ls -a"
alias lla="ls -la"
alias pm="python ${PROJECT_DIR}/manage.py"
. ${HOME}/venv/bin/activate
cd ${PROJECT_DIR}
