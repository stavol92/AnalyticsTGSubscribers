##!/usr/bin/env bash
#
#APP_DIR="\Users\stavo\PycharmProjects\AnalyticsTGSubsrcibers"
#POETRY_PATH="\Users\stavo\AppData\Local\pypoetry\Cache"
#
#export DJANGO_SETTINGS_MODULE=core.settings
#export PYTHONPATH="${PYTHONPATH}:${APP_DIR}"
#echo ${PYTHONPATH}
#
#exit 0
#cd ${APP_DIR} && ${POETRY_PATH} run python ${APP_DIR}/core/manage.py $1

########################################################################

## Set the variables
#$APP_DIR = "\Users\stavo\PycharmProjects\AnalyticsTGSubsrcibers"
#$POETRY_PATH = "\Users\stavo\AppData\Local\pypoetry\Cache"
#
## Set environment variables
#$env:DJANGO_SETTINGS_MODULE = "core.settings"
#$env:PYTHONPATH = "${env:PYTHONPATH};${APP_DIR}"
#Write-Host $env:PYTHONPATH
#
## Change directory and run the Python script
#Set-Location $APP_DIR
#& "${POETRY_PATH}\run" python "${APP_DIR}\core\manage.py" $args[0]

########################################################################

# Set variables
$APP_DIR = "\Users\stavo\PycharmProjects\AnalyticsTGSubsrcibers"
$POETRY_PATH = "\Users\stavo\AppData\Local\pypoetry\Cache"

# Set environment variables
$env:DJANGO_SETTINGS_MODULE = "core.settings"
$env:PYTHONPATH = $APP_DIR

# Change directory and run Python script
Set-Location $APP_DIR
& "$POETRY_PATH\run" python "$APP_DIR\core\manage.py" $args[0]
