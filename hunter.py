from scrapers import *
from banner import *
import pandas as pd
import argparse 


def print_sources(source):
    print()
    df = pd.DataFrame(source)
    pd.set_option('display.max_columns',None)
    pd.set_option('display.max_rows',None)
    pd.set_option('display.width', 1000)

    print(df)

def print_details(details):
    print()
    for i in details:
        print(f"{i} - {details[i]}")


def save(details, filename):
    
    df = pd.DataFrame(details)
    df.to_csv(f"{filename}.csv")

def check_domain(domain):

    n = len(domain.split('.'))
    if not n > 1:
        domain += '.com'
    
    return domain

def main():
    help = '''
    [0] - search by domain (domain search) \n
    [1] - gets the info for the specified person (email finder) \n
    [2] - gets the info for the specified email (email verifier) \n
    [3] - gets the number of emails in the specified domain (email counter)
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scrape', help = help , type = int )
    parser.add_argument('-o', '--output', help = 'Saves the output to a file', action = 'store_true')

    args = parser.parse_args()

    filename = "hunter"

    print('[+] inputs that contains [*] are not to be left blank')
    print()
    if args.scrape == 0:

        domain = input('[*] Domain : ')
        domain = check_domain(domain)

        details , source = domain_search(domain = domain)

        filename = domain
        print_details(details)
        print_sources(source)

    elif args.scrape == 1:

        print('[*] Either Domain or Company should be specified or both .. \n')
        domain = input('[*] Domain : ')
        domain = check_domain(domain)

        first_name = input('[*] First name : ')
        last_name  = input('[*] Last name : ')
        company = input('[+] Company : ')
        details , source = email_finder(domain = domain , first_name  = first_name , last_name = last_name , company = company )

        filename = domain
        print_details(details)
        print_sources(source)

    elif args.scrape == 2:

        email = input('[*] Email : ')
        details , source = email_verifier(email = email)

        filename = email.split('@')[0]
        print_details(details)
        print_sources(source)

    elif args.scrape == 3 :

        print('[*] Either Domain or Company should be specified or both .. \n')
        domain = input('[*] Domain : ')
        domain = check_domain(domain)

        company = input('[+] Company : ')
        details , source = email_count(domain = domain , company = company)

        filename = domain
        print_details(details)

    else:

        raise ValueError('[-] Specify the arguments or "--help" to see the commands')


    if args.output :
        if details is not None and source is not None:
            details.update(source)
            save(details, filename)
        else:
            if details is not None:
                save(details, filename)
            else:
                save(details, filename)


banners()
first_time()
main()