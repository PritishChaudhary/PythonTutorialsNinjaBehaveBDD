import os
from configparser import ConfigParser

config = ConfigParser()
# config.read('configurations/config.ini')

# # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# # config_path = os.path.join(base_dir, 'configurations', 'config.ini')
# # config.read(config_path)
#
# current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# project_root = os.path.dirname(os.path.dirname(current_dir))
# config_path = os.path.join(project_root, 'configurations', 'config.ini')
#
# print(f"Looking for config at {config_path}")
# print(f"File exists: {os.path.exists(config_path)}")
# config.read(config_path)

config_path = 'configurations/config.ini'
print(f"Attempting to read configuration from {config_path}")
print(f"Absolute path: {os.path.abspath(config_path)}")
print(f"File exists: {os.path.exists(config_path)}")
config.read(config_path)
print(f"Sections found: {config.sections()}")

def get_browser():
    return config.get('browser', 'browser')

def get_headless():
    return config.getboolean('browser', 'headless')

def get_base_url():
    return config.get('urls', 'base_url')

def get_implicit_wait():
    return config.getint('timeout', 'implicit_wait')

def get_explicit_wait():
    return config.getint('timeout', 'explicit_wait')

def get_screenshot_dir():
    return config.get('reporting', 'screenshot_dir')
