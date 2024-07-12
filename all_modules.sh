#!/bin/bash

output_all_modules_file="all_modules.txt"

all_modules=$(bin/magento module:status)

echo "$all_modules" >> "$output_all_modules_file"

echo "El archivo $output_all_modules_file ha sido creado con éxito."