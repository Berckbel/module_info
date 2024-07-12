import csv

composer_local_show_path = 'composer_local_show.txt'
output_composer_local_module_versions_file = 'composer_local_module_versions.csv'

data = []
with open(composer_local_show_path, 'r') as composer_local_show:
    for line in composer_local_show:
        parts = line.split()
        module_name = parts[0]
        module_version = parts[1]
        data.append([module_name, module_version])

with open(output_composer_local_module_versions_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['module', 'composer_version'])
    writer.writerows(data)

print(f"Los datos se han guardado en {output_composer_local_module_versions_file}")

composer_live_show_path = 'composer_live_show.txt'
output_composer_live_module_versions_file = 'composer_live_module_versions.csv'

data = []
with open(composer_live_show_path, 'r') as composer_live_show:
    for line in composer_live_show:
        parts = line.split()
        module_name = parts[0]
        module_version = parts[1]
        data.append([module_name, module_version])

with open(output_composer_live_module_versions_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['module', 'composer_version'])
    writer.writerows(data)

print(f"Los datos se han guardado en {output_composer_live_module_versions_file}")