from __future__ import with_statement

import unittest

import sys
import os.path
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../../../lib'))

from sickbeard.indexers.indexer_api import indexerApi
from sickbeard.indexers.indexer_exceptions import indexer_exception

class APICheck(unittest.TestCase):
    indexer_id = 'Continum'
    indexer = 'TVRage'
    # Set our common indexer_api options here
    INDEXER_API_PARMS = {'apikey': 'Uhewg1Rr0o62fvZvUIZt',
                      'language': 'en',
                      'useZip': True}


    INDEXER_API_PARMS['indexer'] = indexer
    lindexer_api_parms = INDEXER_API_PARMS.copy()

    try:
#        showurl = indexerApi(**lindexer_api_parms).config['base_url'] + str(indexer_id) + '/all/en.zip'
        t = indexerApi(cache=True, **lindexer_api_parms)
        myEp = t[indexer_id]

        if getattr(myEp, 'seriesname', None) is not None:
            print "FOUND"

    except indexer_exception as e:
        print e
        pass

if __name__ == "__main__":
    unittest.main()