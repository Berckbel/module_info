#!/bin/bash

output_file="composer_live_show.txt"

# modify this to live site
all_modules=$(composer show)

echo "$all_modules" >> "$output_file"

echo "El archivo $output_file ha sido creado con éxito."