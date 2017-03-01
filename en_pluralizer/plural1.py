#!/usr/bin/python3

import re

def plural(noun):
    if re.search(r'[xzs]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search(r'[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search(r'[^aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'
