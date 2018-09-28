import requests
import pandas as pd
pd.set_option('display.max_columns', 100)
from datetime import timedelta
import requests
import os
import random
import string
from urllib.parse import urlparse, parse_qsl
from random import randint
import time
import datetime


class GetAccessToken(object):
    """
        Get a header authentication item for access token
        for using the internal API's
        by logging in as type = 'employee'
        Usage:
            from accesstoken import AccessToken
            getToken = AccessToken()
            accessToken = getToken.getAccessToken()
            requests.get(url, headers= accessToken)
    """
    def getAccessToken(self, email, password, acceptance):

        def randomword(length):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for i in range(length))

        state = randomword(10)
        scopes = ['SIG/ALL']
        acc_prefix = 'acc.' if acceptance else ''
        authzUrl = f'https://{acc_prefix}api.data.amsterdam.nl/oauth2/authorize'
        params = {
            'idp_id': 'datapunt',
            'response_type': 'token',
            'client_id': 'citydata',
            'scope': ' '.join(scopes),
            'state': state,
            'redirect_uri' : f'https://{acc_prefix}data.amsterdam.nl/'
        }
        print('url', authzUrl)
        response = requests.get(authzUrl, params, allow_redirects=False)
        if response.status_code == 303:
            location = response.headers["Location"]
        else:
            return {}

        data = {
            'type':'employee_plus',
            'email': email,
            'password': password,
        }

        response = requests.post(location, data=data, allow_redirects=False)
        if response.status_code == 303:
            location = response.headers["Location"]
        else:
            return {}

        response = requests.get(location, allow_redirects=False)
        if response.status_code == 303:
            returnedUrl = response.headers["Location"]
        else:
            return {}

        # Get grantToken from parameter aselect_credentials in session URL
        parsed = urlparse(returnedUrl)
        fragment = parse_qsl(parsed.fragment)
        access_token = fragment[0][1]
        os.environ["ACCESS_TOKEN"] = access_token
        return access_token
    
# acceptance = False
# email = os.getenv('SIGNALS_USER', '')
# password = os.getenv('SIGNALS_PASSWORD', '')
# bearer_token = GetAccessToken().getAccessToken(email, password, acceptance)