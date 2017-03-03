#!/usr/bin/python3

import re

def build_match_and_apply_function(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

                # pattern            search  replace
patterns = \
            (
                (r'[sxz]$',            '$',  'es'),
                (r'[^aeioudgkprt]h$',  '$',  'es'),
                (r'[^aeiou]y$',        'y$', 'ies'),
                (r'$',                 '$',  's')
            )


rules = [build_match_and_apply_function(pattern, search, replace )
         for (pattern, search, replace) in patterns]

def plural(noun):
    for matches_rules, apply_rules in rules:
        if matches_rules(noun):
            return apply_rules(noun)
