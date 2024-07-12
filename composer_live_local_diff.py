import csv

composer_local_module_versions_file = 'composer_local_module_versions.csv'
composer_live_module_versions_file = 'composer_live_module_versions.csv'
output_composer_modules_versions_diff_file = 'composer_modules_versions_diff.csv'

data_live = []
data_local = []
result = []
with open(composer_local_module_versions_file, 'r') as local_modules, open(composer_live_module_versions_file, 'r') as live_modules:
    local_reader = csv.DictReader(local_modules)
    live_reader = csv.DictReader(live_modules)

    for live_row in live_reader:
        data_live.append({"module": live_row['module'], "composer_version": live_row['composer_version']})

    for local_row in local_reader:
        data_local.append({"module": local_row['module'], "composer_version": local_row['composer_version']})

if len(data_live) == len(data_local):
    for i in range(len(data_live)):
        if data_live[i]['module'] == data_local[i]['module']:
            result.append({
                "module": data_live[i]['module'],
                "live_composer_version": data_live[i]['composer_version'],
                "local_composer_version": data_local[i]['composer_version'],
                "versions_match": data_local[i]['composer_version'] == data_live[i]['composer_version']
            })
        else:
            print('Modules do not match ' + data_live[i]['module'] + " - " + data_local[i]['module'])
else:
    print("the modules lenth do not match")


with open(output_composer_modules_versions_diff_file, 'w', newline='') as csvfile:
    fieldnames = ['module', 'live_composer_version', 'local_composer_version', 'versions_match']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(result)

print(f'El archivo {output_composer_modules_versions_diff_file} ha sido creado con éxito.')