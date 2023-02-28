from math import log
from re import compile
from urllib.parse import urlparse
from socket import gethostbyname
from pyquery import PyQuery
from requests import get
from json import dump
from string import ascii_lowercase
from numpy import array
from ipaddress import ip_address
import re
class LexicalURLFeatures:
    def __init__(self, url):
        self.url = url
        self.urlparse = urlparse(self.url)
         #listing shortening services
        self.shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                            r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                            r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                            r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                            r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                            r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                            r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                            r"tr\.im|link\.zip\.net"
        
    # extract lexical features

    #UrlLength
    def url_length(self):
        return len(self.url)

    #PathLength
    def url_path_length(self):
        return len(self.urlparse.path)

    #Hostlength
    def url_host_length(self):
        return len(self.urlparse.netloc)

    #HostIsIp
    def url_host_is_ip(self):
        host = self.urlparse.netloc
        try: 
            ip_address(host)
            return 1
        except:
            return 0

    #PortInUrl
    def url_contains_port(self):
        port = self.urlparse.netloc.split(':')
        return int(len(port) > 1 and port[-1].isdigit())

    #NumDigits
    def num_of_digits(self):
        digits = [i for i in self.url if i.isdigit()]
        return len(digits)
    
    #NumQueryParams
    def num_of_parameters(self):
        params = self.urlparse.query
        return 0 if params == '' else len(params.split('&'))

    #NumFragments
    def num_of_fragments(self):
        frags = self.urlparse.fragment
        return 0 if frags == '' else len(frags.split('#'))

    #IsEncoded
    def is_encoded(self):
        return 1 if '%' in self.url.lower() else 0

    #NumEncodings
    def num_encoded_chars(self):
        encs = [i for i in self.url if i == '%']
        return len(encs)
    
    #NumSubDirs
    def num_of_subdirectories(self):
        d = self.urlparse.path.split('/')
        count = 0 
        for s in d:
            if s != "":
                count += 1
        return count
    
    #NumPeriods
    def num_of_periods(self):
        periods = [i for i in self.url if i == '.']
        return len(periods)

    #HasClient
    def has_client_in_string(self):
        return int('client' in self.url.lower())

    #HasAdmin
    def has_admin_in_string(self):
        return int('admin' in self.url.lower())

    #HasServer
    def has_server_in_string(self):
        return int('server' in self.url.lower())

    #HasLogin
    def has_login_in_string(self):
        return int('login' in self.url.lower())
    
    #HasAtsign
    def has_at_sign(self):
        return int("@" in self.url)
    
    #Redirection
    def redirection(self):
        pos = self.url.rfind('//')
        if pos > 6:
            if pos > 7:
                return 1
            else:
                return 0
        else:
            return 0
    #UrlShortened
    def tiny_url(self):
        match=re.search(self.shortening_services,self.url)
        if match:
            return 1
        else:
            return 0
    #UsesHttps
    def uses_https(self):
        domain = self.urlparse.netloc
        if 'https' in domain:
            return 1
        else:
            return 0
        
    # DashInDomain
    def dash_in_domain(self):
        domain = self.urlparse.netloc
        return int('-' in domain)
    