#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import json
import time
import pprint
from hashlib import md5
from collections import namedtuple

import requests

Keys = namedtuple('Keys', ['public_key', 'private_key'])
MARVEL = Keys(
    '1494f93954555aa469085ee2c2facfaa',
    '7f1d072438a8a077429e00821b5ba27154f349ce'
    )

def calc_hash(ts):
    '''
    Server-side applications must pass two parameters in addition
    to the apikey parameter:

    - ts: a timestamp (or other long string which can change on a 
          request-by-request basis)
    - hash: a md5 digest of the ts parameter, your private key and 
            your public key (e.g. md5(ts+privateKey+publicKey)

    For example, a user with a public key of "1234" and a private key
    of "abcd", for a ts of 1, needs this hashcode:

        ffd275c5130566a2916217b101f26150

    since:
    
        >>> from hashlib import md5
        >>> print(md5('1abcd1234').hexdigest())
        ffd275c5130566a2916217b101f26150
        >>> 
    '''

    return md5('{}{}{}'.format(
        ts, MARVEL.private_key, MARVEL.public_key
        )).hexdigest()


def find_character(name):
    host = 'gateway.marvel.com'
    version = '1'
    path = 'characters'
    url = 'https://{h}/v{v}/public/{p}'.format(
            h=host,
            v=version,
            p=path,
            )
    logging.warning(url)
    ts = int(time.time())
    r = requests.get(url, params={
        'apikey': MARVEL.public_key, 
        'ts': ts,
        'hash': calc_hash(ts),
        'name': name,
        })
    logging.warning(r.url)
    logging.warning(r.status_code)
    if r.status_code == 200:
        return json.loads(r.content)
    else:
        print(r.status_code)
        print(r.content)
        print(pprint.pformat(r))

