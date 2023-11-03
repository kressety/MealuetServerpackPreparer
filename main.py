from configparser import ConfigParser
from logging import getLogger, basicConfig, INFO
from os.path import exists

from client.prep_client import prep_client
from server.prep_server import prep_server

if __name__ == '__main__':
    basicConfig()

    config = ConfigParser()
    log = getLogger()
    log.setLevel(INFO)

    if not exists('config.ini'):
        log.info('config.ini created. ')
        config.read_dict({
            'DEFAULT': {
                'loader': '%(Enter modloader name here, etc. fabric)s',
                'game_version': '%(Enter game version name here, etc. 1.20.1)s',
                'pack_name': '%(Enter pack name here, etc. Create Astral)s'
            },
            'client': {
                'enable': 'True',
                'game_path': '%(Enter client path here, etc. /root/mc)s'
            },
            'server': {
                'enable': 'True',
                'server_path': '%(Enter server path here, etc. /root/mc)s',
                'memory_limit': '20'
            }
        })
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
    else:
        log.info('config.ini was read. ')
        config.read('config.ini', encoding='UTF-8')
        if config['client']['enable'].strip().lower() == 'true':
            prep_client(
                config['client']['game_path'],
                config['client']['loader'],
                config['client']['game_version']
            )
        if config['client']['enable'].strip().lower() == 'true':
            prep_server(
                config['server']['server_path'],
                config['server']['game_version'],
                config['server']['memory_limit'],
                config['server']['pack_name']
            )
