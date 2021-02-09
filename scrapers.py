import requests as req 
from json import dumps
from configparser import ConfigParser
from collections import OrderedDict as od
import sys

config = ConfigParser()
config.read('settings.ini')
key = config['creds']['key']
count = config['creds']['count']
base_url = config['creds']['base_url'].replace("'","")
api_url = config['creds']['api_url'].replace("'","")
limit = config['creds']['limit'].split()[0]


def check_api_key():

    if key == '':
        
        print('[-] API Key is blank .......')
        print(f"[+] Get API key : {api_url}")
        return True
    else:
        return False

def first_time():
    if count == '0':
        print()
        print('[+] First time use detected ......')
        config.set('creds','COUNT','1')
        with open('settings.ini','w') as file:
            config.write(file)
        
        if check_api_key():
            sys.exit()
        else:
            pass        
        

    else:
        if check_api_key():
            sys.exit()
        else:
            pass
            

def  get_response(url):
    res = req.get(url)
    return res.json()


def check_error(res):
    if 'errors' in res:
        print(dumps(res,indent=4))
        exit()
        # return True
    else:
        return False


def get_details(res):
    details = od()
    sources = od()
    sources['uri'] = []
    sources['last_seen_on'] = []
    sources['extracted_on'] = []
    sources['still_on_page'] = []

    if not check_error(res):
        for i in res['data']:
            
            if i == 'sources':
                for j in res['data'][i]:
                    sources['uri'].append(j['uri'])
                    sources['last_seen_on'].append(j['last_seen_on']) 
                    sources['extracted_on'].append(j['extracted_on'])
                    sources['still_on_page'].append(j['still_on_page'])
            
            elif i == 'verification':
                date = res['data'][i]['date']
                status = res['data'][i]['status']

                if date is not None:
                    details['date'] = date
                
                if status is not None:
                    details['status'] = status
            else:
                details[i] = res['data'][i]
    
    return details , sources


key = key.replace("'","")

def domain_search(domain = None):

    url = '{base_url}domain-search?domain={domain}&api_key={key}&limit={limit}'.format(domain=domain, base_url = base_url , key = key , limit = limit )
    res = get_response(url)
    
    domain_details = od()
    details = od()

    details['emails'] = []
    details['full_name'] = []
    details['type'] = []
    details['position'] = []
    details['department'] = []
    details['phone_number'] = []
    details['linkedin'] = []
    details['twitter'] = []
    details['source'] = []

    if not check_error(res):
        domain_details['domain'] = res['data']['domain']
        domain_details['organization'] = res['data']['organization']
        domain_details['country'] = res['data']['country']
        domain_details['state'] = res['data']['state']

        for i in res['data']['emails']:
            details['emails'].append( i['value'] )
            details['full_name'].append( f'{i["first_name"]} {i["last_name"]}')
            details['type'].append( i['type'] )
            details['position'].append( i['position'] )
            details['department'].append( i['department'] )
            details['phone_number'].append( i['phone_number'] )
            details['linkedin'].append( i['linkedin'] )
            details['twitter'].append( i['twitter'] )
            details['source'].append( i['sources'][0]['uri'] )
    
    return domain_details , details


def email_finder(domain = None, first_name = None , last_name = None , company = None):

    if company == '':
        url = '{base_url}email-finder?domain={domain}&first_name={first_name}&last_name={last_name}&api_key={key}'.format(domain = domain , first_name = first_name , last_name  = last_name,  base_url = base_url , key = key )
    else:
        url = '{base_url}email-finder?company={company}&full_name={first_name}+{last_name}&api_key={key}'.format(company = company , first_name = first_name , last_name = last_name ,  base_url = base_url , key = key )
    res = get_response(url)

    details , source = get_details(res)

    return details , source


def email_verifier(email = None):
    
    url = '{base_url}email-verifier?email={email}&api_key={key}'.format(email = email ,  base_url = base_url , key = key )
    res = get_response(url)

    details , source = get_details(res)

    return details , source


def email_count(domain = None , company = None):
    
    if company != '':
        url = '{base_url}email-count?domain={domain}&company={company}'.format(domain = domain, company = company ,  base_url = base_url )
    else:
        url = '{base_url}email-count?domain={domain}'.format(domain = domain, base_url = base_url )

    res = get_response(url)

    details = od()

    details['domain'] = domain
    details['company'] = company
    for i in res['data']:
        details[i] = res['data'][i]

    return details , None