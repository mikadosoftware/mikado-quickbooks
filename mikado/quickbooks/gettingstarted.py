

"""
I am building a quickbooks client so I can hopefully automate the
process of assigning transactions 
I want to have a personal home account.  THe data grabbing seems to work quite well.

"""

from intuitlib.client import AuthClient
import yaml

def get_secrets():
    with open('/var/projects/.quickbooks') as fo:
        d = yaml.safe_load(fo)
    return d
    
def connect():
    d = get_secrets()
    auth_client = AuthClient(
        client_id=d['client'],
        client_secret=d['secret'],
        environment='sandbox',
        redirect_uri='http://localhost:8000/callback',
    )
    client = QuickBooks(
         auth_client=auth_client,
         refresh_token='REFRESH_TOKEN',
         company_id='COMPANY_ID',
     )


    return auth_client

from quickbooks import QuickBooks


    
if __name__ == '__main__':
    d = get_secrets()
    print(d.keys())

