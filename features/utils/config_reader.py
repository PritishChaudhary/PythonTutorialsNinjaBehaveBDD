import os
from configparser import ConfigParser

config = ConfigParser()

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
