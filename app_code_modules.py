import csv
import json
import os
import re

base_path = 'app/code'
output_file = 'app_vendor_modules.csv'

data = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file == 'module.xml':
            module_xml_path = os.path.join(root, file)
            with open(module_xml_path, 'r') as module_xml_file:
                content = module_xml_file.read()
                match = re.search(r'<module name="([^"]+)"', content)
                if match:
                    module_name = match.group(1)
                    module_version = 'N/A'
                    
                    module_dir = os.path.dirname(os.path.dirname(module_xml_path))
                    composer_json_path = os.path.join(module_dir, 'composer.json')
                    
                    if os.path.isfile(composer_json_path):
                        with open(composer_json_path, 'r') as composer_json_file:
                            try:
                                composer_data = json.load(composer_json_file)
                                module_version = composer_data.get('version', 'N/A')
                            except json.JSONDecodeError:
                                pass
                    
                    data.append([module_name, module_version])

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['module', 'composer_version'])
    
    writer.writerows(data)

print(f"Los datos se han guardado en {output_file}")