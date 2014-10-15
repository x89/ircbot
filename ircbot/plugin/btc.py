try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import json
from datetime import datetime, timedelta


class BTC:
    url = 'https://api.bitcoinaverage.com/ticker/global/{0}/last'
    currencies = {
        'USD': False,
        'EUR': False, 
        'GBP': False,
        }
    last_update = datetime.now()

    def update_prices(self):
        for currency, value in self.currencies.items():
            get_request = urlopen(self.url.format(currency)).read()
            self.currencies[currency] = float(get_request)
        self.last_update = datetime.now()
        return self.currencies

    def get_latest_price(self, currency='USD'):
        if not isinstance(currency, str):
            return "Deets pretty scurvy."
        if len(currency) < 2:
            currency = 'USD'
        currency = currency.upper()
        if currency not in self.currencies.keys():
           return "Aye mate, {currency} ain't no fuckin' deet. Use one of: {currencies}.".format(
               currency=currency,
               currencies=', '.join(self.currencies.keys())
           )
        if not self.currencies[currency] or \
           datetime.now() - self.last_update > timedelta(minutes=5):
            self.update_prices()
        return str(str(self.currencies[currency]) + currency)
