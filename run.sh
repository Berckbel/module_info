#!/bin/bash

sh ./all_modules.sh
python3 ./all_modules.py
python3 ./app_code_modules.py
python3 ./app_code_modules_status_and_versions.py
sh ./composer_local_show.sh
# sh ./composer_live_show.sh
python3 ./composer_env_versions.py
python3 ./composer_live_local_diff.py
