if [[ $0 == -* ]]; then
    echo 'Please do not source this script in an interactive shell' >&2
fi



APP_NAME='ocr_server'

APP_PATH=$(cd $(dirname $0)/../ && pwd -P)

APP_LOG_DIR=$APP_PATH/logs
APP_TMP_DIR=$APP_PATH/tmp

PYTHONPATH=$APP_PATH:PYTHONPATH
export PYTHONPATH
