import csv

enabled_modules_file = 'enabled_modules.txt'
app_vendor_modules_file = 'app_vendor_modules.csv'
output_app_modules_info_file = 'app_modules_info.csv'

data = []
with open(app_vendor_modules_file, 'r') as app_modules, open(enabled_modules_file, 'r') as enabled_modules:
    reader = csv.DictReader(app_modules)
    list_enabled_modules = enabled_modules.read().splitlines()
    for row in reader:
        module_name = row['module']
        composer_version = row['composer_version']
        
        enabled = "Yes" if module_name in list_enabled_modules else "No"
        data.append({
            'module': module_name,
            'enabled': enabled,
            'composer_version': composer_version,
            'installation_mode': 'app/code'
        })

with open(output_app_modules_info_file, 'w', newline='') as csvfile:
    fieldnames = ['module', 'enabled', 'composer_version', 'installation_mode']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f'El archivo {output_app_modules_info_file} ha sido creado con éxito.')