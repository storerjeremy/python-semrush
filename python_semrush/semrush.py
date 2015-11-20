from __future__ import absolute_import, print_function, unicode_literals
import requests
from python_semrush import REGIONAL_DATABASES
from python_semrush.errors import *

SEMRUSH_API_URL = 'http://api.semrush.com/'

class SemrushClient(object):

    def __init__(self, key):
        if not key:
            raise SemRushKeyError('A Semrush key must be provided')

        self.url = SEMRUSH_API_URL
        self.key = key

    @staticmethod
    def get_database_from_search_engine(search_engine='google.com'):
        if search_engine in REGIONAL_DATABASES:
            return REGIONAL_DATABASES[search_engine]
        else:
            raise SemRushRegionalDatabaseError('%s - is not an accepted search engine.' % search_engine)

    # Report producing methods
    def produce(self, report_type, **kwargs):
        data = self.retrieve(report_type, kwargs)
        return self.parse(data)

    def retrieve(self, report_type, **kwargs):
        kwargs['type'] = report_type
        kwargs['key'] = self.key

        response = requests.get(self.url, params=kwargs)

        if response.status_code == 200:
            return response.content
        else:
            # Todo: Implement all errors from http://www.semrush.com/api-analytics/
            raise BaseSemrushError(response.content)

    @staticmethod
    def parse(data):
        results = []

        lines = data.split('\r')
        columns = lines[0].split(';')

        for line in lines[1:]:
            result = {}
            for i, datum in enumerate(line.split(';')):
                result[columns[i]] = datum.strip('"\n\r\t')
            results.append(result)

        return results

    # Overview Reports
    """
    Domain Overview (All Databases)
    This report provides live or historical data on a domain’s keyword rankings in both organic and paid search in all
    regional databases.

    Optional kwargs
    - display_date: date in format "YYYYMM15"
    - export_columns: Db, Dn, Rk, Or, Ot, Oc, Ad, At, Ac
    """
    def get_domain_overview_report_all_databases(self, domain, **kwargs):
        return self.produce('domain_ranks', domain=domain, **kwargs)

    """
    Domain Overview (One Database)
    This report provides live or historical data on a domain’s keyword rankings in both organic and paid search in a
    chosen regional database.

    Optional kwargs
    - export_escape: 1 to wrap report columns in quotation marks (")
    - export decode: 1 or 0, 0 to url encode string
    - display_date: date in format "YYYYMM15"
    - export_columns: Dn, Rk, Or, Ot, Oc, Ad, At, Ac
    """
    def get_domain_overview_report_one_database(self, domain, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', domain=domain, database=database, **kwargs)

    """
    Domain Overview (History)
    This report provides live and historical data on a domain’s keyword rankings in both organic and paid search in a
    chosen database.

    Optional kwargs
    - display_limit: integer
    - display_offset: integer
    - export_escape: 1
    - export_decode: 1 or 0
    - display_daily: 1
    - export_columns: Rk, Or, Ot, Oc, Ad, At, Ac, Dt
    - display_sort: dt_asc, dt_desc
    """
    def domain_overview_history(self, domain, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank_history', domain=domain, database=database, **kwargs)

    """
    Winners and Losers
    This report shows changes in the number of keywords, traffic, and budget estimates of the most popular websites in
    Google's top 20 and paid search results.


    Optional kwargs
    - display_limit: integer
    - display_offset: integer
    - export_escape: 1
    - export_decode: 1 or 0
    - display_date: date in format "YYYYMM15"
    - export_columns: Dn, Rk, Or, Ot, Oc, Ad, At, Ac, Om, Tm, Um, Am, Bm, Cm
    - display_sort: om_asc, om_desc, tm_asc, tm_desc, um_asc, um_desc, am_asc, am_desc, bm_asc, bm_desc, cm_asc, cm_desc
    """
    def winners_and_losers(self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('rank_difference', database=database, **kwargs)

    """
    Semrush Rank
    This report lists the most popular domains ranked by traffic originating from Google's top 20 organic search
    results.

    Optional kwargs
    - display_limit: integer
    - display_offset: integer
    - export_escape: 1
    - export_decode: 1 or 0
    - display_date: date in format "YYYYMM15"
    - export_columns: Dn, Rk, Or, Ot, Oc, Ad, At, Ac
    """
    def semrush_rank(self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('rank', database=database, **kwargs)

    # Domain Reports
    """
    Domain Organic Search Keywords
    This report lists keywords that bring users to a domain via Google's top 20 organic search results.

    Optional kwargs
    - display_limit: integer
    - display_offset: integer
    - export_escape: 1
    - export_decode: 1 or 0
    - display_date: date in format "YYYYMM15"
    - export_columns: Ph, Po, Pp, Pd, Nq, Cp, Ur, Tr, Tc, Co, Nr, Td
    - display_sort: tr_asc, tr_desc, po_asc, po_desc, tc_asc, tc_desc
    - display_positions: new, lost, rise or fall
    - display_filter:
    """
    def domain_organic_search_keywords(self, domain, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_organic', domain=domain, database=database, **kwargs)

    """
    Domain Paid Search
    This report lists keywords that bring users to a domain via Google's paid search results.

    Optional kwargs
    - display_limit: integer
    - display_offset: integer
    - export_escape: 1
    - export_decode: 1 or 0
    - display_date: date in format "YYYYMM15"
    - export_columns: Ph, Po, Pp, Pd, Ab, Nq, Cp, Tr, Tc, Co, Nr, Td, Tt, Ds, Vu, Ur
    - display_sort: tr_asc, tr_desc, po_asc, po_desc, tc_asc, tc_desc
    - display_positions: new, lost, rise or fall
    - display_filter:
    """
    def domain_paid_search_keywords(self, domain, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_adwords', domain=domain, database=database, **kwargs)

    """
    Ads Copies
    This report shows unique ad copies SEMrush noticed when the domain ranked in Google's paid search results for
    keywords from our databases.

    Optional kwargs
    -
    -
    """
    def ad(self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    # Keyword Reports
    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    # URL Reports
    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    # Display Advertising Reports
    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    # Backlinks
    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)

    """


    Optional kwargs
    -
    -
    """
    def (self, database, **kwargs):
        if database not in REGIONAL_DATABASES.values():
            raise SemRushRegionalDatabaseError('%s - is not an accepted database.' % database)
        return self.produce('domain_rank', database=database, **kwargs)
