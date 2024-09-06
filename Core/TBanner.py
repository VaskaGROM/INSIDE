from colorama import Fore



_banner = '''
The Black Stalker
'''



def banner(host, port):
    '''Вывод баннера с ссылкой'''

    print(Fore.GREEN + _banner)
    print(f'Перейдите по http://{host}:{port}')
