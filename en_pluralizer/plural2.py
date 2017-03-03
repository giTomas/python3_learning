#!/usr/bin/python3

import re

def match_sxz(noun):
    return  re.search(r'[sxz]$', noun)

def apply_sxz(noun):
    return re.sub(r'$', 'es', noun)

def match_h(noun):
    return re.search(r'[^aeioudgkprt]h$', noun)

def apply_h(noun):
    return re.sub(r'$', 'es', noun)

def match_y(noun):
    return re.search(r'[^aeiou]y$', noun)

def apply_y(noun):
    return re.sub('y$', 'ies', noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + 's'

rules = ((match_sxz, apply_sxz),
         (match_h, apply_h),
         (match_y, apply_y),
         (match_default, apply_default))

def plural(noun):
    for matches_rules, apply_rules in rules:
        if matches_rules(noun):
            return apply_rules(noun)
