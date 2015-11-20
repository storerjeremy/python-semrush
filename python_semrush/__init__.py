__author__ = 'jstorer'

__all__ = ['SemrushClient', 'SemrushClientException']

from python_semrush import SemrushClient, SemrushClientException

REGIONAL_DATABASES = {
    'google.com': 'us',
    'google.co.uk': 'uk',
    'google.ca': 'ca',
    'google.ru': 'ru',
    'google.de': 'de',
    'google.fr': 'fr',
    'google.es': 'es',
    'google.it': 'it',
    'google.com.br': 'br',
    'google.com.au': 'au',
    'bing.com': 'bing-us',
    'google.com.ar': 'ar',
    'google.be': 'be',
    'google.ch': 'ch',
    'google.dk': 'dk',
    'google.fi': 'fi',
    'google.com.hk': 'hk',
    'google.ie': 'ie',
    'google.co.il': 'il',
    'google.com.mx': 'mx',
    'google.nl': 'nl',
    'google.no': 'no',
    'google.pl': 'pl',
    'google.se': 'se',
    'google.com.sg': 'sg',
    'google.com.tr': 'tr',
    'google.com': 'mobile-us',
    'google.co.jp': 'jp',
    'google.co.in': 'in'
}
