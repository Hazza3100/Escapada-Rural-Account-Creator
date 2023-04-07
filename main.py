import threading

from string   import *
from random   import *
from requests import *
from colorama import *


class Escapada:
    def __init__(self) -> None:
        self.session = Session()
    created = 0
    errors  = 0

    def __gen__(self, use) -> None:
        try:
            with self.session as session:
                name     = ''.join(choices(ascii_letters, k=7))
                email    = ''.join(choices(ascii_letters + digits, k=10)) + "@gmail.com"
                surname  = ''.join(choices(ascii_letters, k=7))
                password = ''.join(choices(ascii_letters + digits , k=12))

                headers = {
                    'authority'         : 'www.escapadarural.com',
                    'accept'            : '*/*',
                    'accept-language'   : 'en-GB,en-US;q=0.9,en;q=0.8',
                    'content-type'      : 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin'            : 'https://www.escapadarural.com',
                    'referer'           : 'https://www.escapadarural.com/',
                    'sec-ch-ua'         : '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile'  : '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest'    : 'empty',
                    'sec-fetch-mode'    : 'cors',
                    'sec-fetch-site'    : 'same-origin',
                    'user-agent'        : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                    'x-requested-with'  : 'XMLHttpRequest',
                }
                parms = {
                    'traveler[user_name]'    : name,
                    'traveler[user_email]'   : email,
                    'traveler[user_surname]' : surname,
                    'traveler[user_password]': password,
                    'traveler[user_type]'    : 'traveler',
                    'traveler[conditions]'   : '1',
                    'popUpLog'               : 'undefined'
                    }
                if use == True:
                    proxy = choice(open('data/proxies.txt', 'r').read().splitlines())
                    response = session.post('https://www.escapadarural.com/dynamic/popup/login/signUp', params=parms, headers=headers, proxies={'http': f'http://{proxy}', 'https': f'http://{proxy}'})
                else:
                    response = session.post('https://www.escapadarural.com/dynamic/popup/login/signUp', params=parms, headers=headers)
                if response.status_code == 200:
                    Escapada.created += 1
                    print(f"{Fore.BLUE}[ {Fore.GREEN}+ {Fore.BLUE}]{Fore.RESET} Generated Acccount ({Escapada.created})")
                    with open('data/accounts.txt', 'a') as f:
                        f.write(f'{email}:{password}:{name}:{surname}\n')
                else:
                    Escapada.errors += 1
                    print(f"{Fore.BLUE}[ {Fore.RED}x {Fore.BLUE}]{Fore.RESET} Unknown Error ({self.errors})")
        except Exception as e:
            pass



threads = int(input(f"{Fore.BLUE}[ {Fore.YELLOW}> {Fore.BLUE}]{Fore.RESET} Threads > "))
usePR   = input(f"{Fore.BLUE}[ {Fore.YELLOW}> {Fore.BLUE}]{Fore.RESET} Use Proxies (y/n) > ")
if usePR == 'y':
    use = True
else:
    use = False
for i in range(threads):
    threading.Thread(target=Escapada().__gen__, args=(use,)).start()

#print(f"{Fore.BLUE}[ {Fore.YELLOW}+ {Fore.BLUE}]{Fore.RESET} Finished with {Escapada.created}/{threads}, {Escapada.errors} Errors ")
