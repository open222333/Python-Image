from configparser import ConfigParser
import os

conf = ConfigParser()
conf.read(os.path.join('conf', 'config.ini'))


DIR_PATH = conf.get('BASIC', 'DIR_PATH', fallback='test')
if os.path.exists(DIR_PATH):
    os.makedirs(DIR_PATH)
