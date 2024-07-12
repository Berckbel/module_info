#!/bin/bash

output_file="composer_local_show.txt"

all_modules=$(composer show)

echo "$all_modules" >> "$output_file"

echo "El archivo $output_file ha sido creado con éxito."