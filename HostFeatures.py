from whois import whois
from wayback import CdxRecord
from socket import gethostbyname
from requests import get
from urllib.parse import urlparse
from datetime import datetime
from ipaddress import ip_address 

class HostFeatures:
    def __init__(self, url):
        self.url = url
        self.urlparse = urlparse(self.url)
        self.host = self.__get_ip()
        self.now = datetime.now()
        self.whois = self.__get__whois_dict()
        self.snapshots = self.__get_site_snapshots()
        
    def __get_ip(self):
        try:
            ip = self.urlparse.netloc if self.url_host_is_ip() else gethostbyname(self.urlparse.netloc)
            return ip
        except:
            return None

    def __get__whois_dict(self):
        try:
            whois_dict = whois(self.host)
            return whois_dict
        except:
            return {}

    def __parse__before__date(self, date_string):
        month_year = date_string.split()[-1]
        d = '01-{}'.format(month_year)
        d = datetime.strptime(d, '%d-%b-%Y')
        return d

    def __parse_whois_date(self, date_key):
        cdate = self.whois.get(date_key, None)
        if cdate:
            if isinstance(cdate, str) and 'before' in cdate:
                d = self.__parse__before__date(cdate)
            elif isinstance(cdate, list):
                d = cdate[0]
            else:
                d = cdate
        return d if cdate else cdate

    def __get_site_snapshots(self):
        try:
            snapshots = CdxRecord(self.urlparse.netloc).snapshots()
            snapshots = [snapshot.datetime_timestamp for snapshot in snapshots]
            return snapshots
        except:
            return []
        
    def url_host_is_ip(self):
        host = self.urlparse.netloc
        try: 
            ip_address(host)
            return 1
        except:
            return 0

    def url_creation_date(self):
        d = self.__parse_whois_date('creation_date')
        return d

    def url_expiration_date(self):
        d = self.__parse_whois_date('expiration_date')
        return d
    
    def url_last_updated(self):
        d = self.__parse_whois_date('updated_date')
        return d
    # Age
    def url_age(self):
        try:
            days = (self.now - self.url_creation_date()).days
        except:
            days = -1
        return days
     
    #IntendedLife_Span
    def url_intended_life_span(self):
        try:
            lifespan = (self.url_expiration_date() - self.url_creation_date()).days
        except:
            lifespan = -1
        return lifespan
    
    #LifeRemaining
    def url_life_remaining(self):
        try:
            rem = (self.url_expiration_date() - self.now).days
        except:
            rem = -1
        return rem
    
    #IsLive
    def url_is_live(self):
        url = '{}://{}'.format(self.urlparse.scheme, self.urlparse.netloc)
        try:
            return int(get(url).status_code == 200)
        except:
            return 0
    #ConnectionSpeed
    def url_connection_speed(self):
        url = '{}://{}'.format(self.urlparse.scheme, self.urlparse.netloc)
        if self.url_is_live():
            return get(url).elapsed.total_seconds()
        else:
            return 100000000000
        
    #AvgUpdateFrequency
    def average_update_frequency(self):
        snapshots = self.snapshots
        diffs = [(t-s).days for s, t in zip(snapshots, snapshots[1:])]
        l = len(diffs)
        if l > 0:
            return sum(diffs)/l
        else:
            return 0
        
    #NumUpdates
    def number_of_updates(self):
        return len(self.snapshots)
    
    def first_seen(self):
        try:
            fs = self.snapshots[0]
            return fs
        except:
            return datetime.now()
    #TTL
    def ttl_from_registration(self):
        earliest_date_seen = self.first_seen()
        try:
            ttl_from_reg = (earliest_date_seen - self.url_creation_date()).days
        except:
            ttl_from_reg = -1
        return ttl_from_reg
    
    