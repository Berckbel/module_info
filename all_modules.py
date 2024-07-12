all_modules_path = 'all_modules.txt'
enabled_modules_path = 'enabled_modules.txt'
disabled_modules_path = 'disabled_modules.txt'

enabled_modules = []
disabled_modules = []
reading_enabled = False
reading_disabled = False

with open(all_modules_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line == "List of enabled modules:":
            reading_enabled = True
            reading_disabled = False
            continue
        elif line == "List of disabled modules:":
            reading_enabled = False
            reading_disabled = True
            continue
        
        if reading_enabled and line:
            enabled_modules.append(line)
        elif reading_disabled and line:
            disabled_modules.append(line)

with open(enabled_modules_path, 'w') as f:
    for module in enabled_modules:
        f.write(module + '\n')

with open(disabled_modules_path, 'w') as f:
    for module in disabled_modules:
        f.write(module + '\n')

print(f'Se han escrito los módulos habilitados en {enabled_modules_path} y los deshabilitados en {disabled_modules_path}.')
