def load_config(config_file):
    with open(config_file, 'r') as f:
        config_data = f.readlines()
        for line in config_data:
            if line.startswith('working_directory'):
                working_directory = line.split('=')[1].strip()
                working_directory = working_directory.strip('"')
                return working_directory