from rich.console import Console
from rich.table import Table
from requests import get, post
from collections import Counter
from time import sleep
import os
import re

console = Console()
NAME = list()

def header():
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(
        """
███╗   ██╗██╗   ██╗███╗   ███╗      ██╗███╗   ██╗███████╗ ██████╗ 
████╗  ██║██║   ██║████╗ ████║      ██║████╗  ██║██╔════╝██╔═══██╗
██╔██╗ ██║██║   ██║██╔████╔██║█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║╚██╗██║██║   ██║██║╚██╔╝██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║      ██║██║ ╚████║██║     ╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝  
                                                                                                                  
                   By @kmein iraqi - @KMIN09
        """, style="bold dark_red", justify="left"
    )

def Main():
    header()
    num = input('[+] Enter a Phone Number : ')
    if '+' in num:
        num = num.replace('+', '')
    
    try:
        code, number = num.split(' ')
    except ValueError:
        console.print('[!] Error Invalid Number, Example : [ 964 5055555555 ]')
        exit()
    
    header()
    Search_1(number, code)
    Search_2(code, number, code)
    Search_3(code, number, code)
    Search_4(code, number, code)
    Number_info(code, number, code)

def Search_1(number, code):
    country = None
    if code == '20':
        country = 'EG'
    elif code == '98':
        country = 'IR'
    elif code == '212':
        country = 'MA'
    elif code == '213':
        country = 'DZ'
    elif code == '216':
        country = 'TN'
    elif code == '249':
        country = 'SD'
    elif code == '252':
        country = 'SO'
    elif code == '961':
        country = 'LB'
    elif code == '962':
        country = 'JO'
    elif code == '963':
        country = 'SY'
    elif code == '964':
        country = 'IQ'
    elif code == '965':
        country = 'KW'
    elif code == '966':
        country = 'SA'
    elif code == '967':
        country = 'YE'
    elif code == '968':
        country = 'OM'
    elif code == '970':
        country = 'PS'
    elif code == '971':
        country = 'AE'
    elif code == '972':
        country = 'ISR'
    elif code == '973':
        country = 'BH'
    elif code == '974':
        country = 'QA'
    
    if country is None:
        console.print('[bold red]heros[/bold red]:-# Search 1 : Country Code Not Supported')
        return
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; RMX1821) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4660.11 Mobile Safari/537.36'
    }
    
    try:
        r = get(f'http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={number}&country_code={country}', headers=headers)
        r.raise_for_status()
        data = r.json()
        
        if 'result' in data and data['result']:
            name = data['result'][0]['name']
            if name:
                NAME.append(name)
                console.print('[bold red]heros[/bold red]:-# Search 1 : [bold green1]success[/bold green1]')
            else:
                console.print(f'[bold red]heros[/bold red]:-# Search 1 : No information Found For [ +{code}{number} ]')
        else:
            console.print(f'[bold red]heros[/bold red]:-# Search 1 : No information Found For [ +{code}{number} ]')
    except Exception as e:
        console.print(f'[bold red]heros[/bold red]:-# Search 1 : [bold red]Error[/bold red] {e}')

def Search_2(country, number, code):
    try:
        rq = get(f'http://146.148.112.105/caller/index.php/UserManagement/search_number?number={number}&country_code={country}')
        rq.raise_for_status()
        data = rq.json()
        
        if 'result' in data and data['result']:
            for item in data['result']:
                NAME.append(item['name'])
            console.print('[bold red]heros[/bold red]:-# Search 2 : [bold green1]success[/bold green1]')
        else:
            console.print(f'[bold red]heros[/bold red]:-# Search 2 : No information Found For [ +{code}{number} ]')
    except Exception as e:
        console.print(f'[bold red]heros[/bold red]:-# Search 2 : [bold red]Error[/bold red] {e}')

def Search_3(country, number, code):
    headers = {
        'Authorization': 'Basic YWEyNTAyOnp1enVBaGgy',
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G977N Build/LMY49I)',
        'Host': 'devappteamcall.site',
        'Connection': 'close',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '23'
    }
    
    try:
        r = post(f'https://devappteamcall.site/data/search_name?country={country}&phoneNumber={number}', headers=headers)
        r.raise_for_status()
        data = r.json()
        
        if 'errorDesc' in data and data['errorDesc'] == 'no data found':
            console.print(f'[bold red]heros[/bold red]:-# Search 3 : No information Found For [ +{code}{number} ]')
        else:
            for name in re.findall('"Name":"(.*?)"', str(data)):
                NAME.append(name)
            console.print('[bold red]heros[/bold red]:-# Search 3 : [bold green1]success[/bold green1]')
    except Exception as e:
        console.print(f'[bold red]heros[/bold red]:-# Search 3 : [bold red]Error[/bold red] {e}')

def Search_4(country, number, code):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'User-Agent': 'نمبربوك الخليج 1/3.3 CFNetwork/1240.0.4 Darwin/20.5.0'.encode('UTF-8'),
        'Accept-Encoding': 'gzip, deflate',
        'Host': '86.48.0.204:919',
        'Accept': '*/*',
        'Accept-Language': 'ar',
        'Authorization': 'Basic aW9zYWRtaW46cGFzc3BvcmQ=',
        'token': 'pcfgv64567ko1',
        'Content-Length': '19'
    }
    
    try:
        r = post('http://86.48.0.204:919/main', data={'number': str(code + number)}, headers=headers)
        r.raise_for_status()
        data = r.json()
        
        if 'name' in data:
            NAME.append(data['name'])
            console.print('[bold red]heros[/bold red]:-# Search 4 : [bold green1]success[/bold green1]')
        else:
            console.print(f'[bold red]heros[/bold red]:-# Search 4 : No information Found For [ +{code}{number} ]')
    except Exception as e:
        console.print(f'[bold red]heros[/bold red]:-# Search 4 : [bold red]Error[/bold red] {e}')

def Number_info(country, number, code):
    if len(NAME) == 0:
        console.print(f'[bold red]heros[/bold red]:-# Number-Info : No information Found For [ +{code}{number} ]')
        exit()
    
    sleep(2)
    header()
    console.print(f'[bold bright_white] Number information  [ +{code}{number} {country} ] [/bold bright_white]')
    
    table = Table(show_header=True, header_style="bold bright_blue")
    table.add_column('ID', style="bold dim", width=6)
    table.add_column('Name', style="bold red", min_width=20, justify="left")
    
    for id, name in enumerate(NAME, 1):
        table.add_row(str(id), str(name))
    
    console.print(table)
    
    try:
        console.print('[bold red]heros[/bold red]:-# [ [bold dark_orange3]INFO[/bold dark_orange3] ] We Have Found That The Most Common Names in The list are ')
        for i in Counter(str(NAME).replace("'", '').replace(',', '').split()).most_common(4):
            console.print(f'- [ {i[0]} ] It has been repeated about [ {i[1]} ] Times')
    except Exception as e:
        console.print(f'[bold red]heros[/bold red]:-# Number-Info [bold red]Error[/bold red] {e}')

Main()
