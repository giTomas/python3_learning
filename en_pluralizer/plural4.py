#!/usr/bin/python3

import re

def build_match_and_apply_function(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

def rules(rules_filename):
    with open('plural4_rules.txt', encoding='utf-8') as pattern_file:
        for line in pattern_file:
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_function(
                pattern, search, replace)


def plural(noun, rules_filename='plural4_rules.txt'):
    for matches_rules, apply_rules in rules(rules_filename):
        if matches_rules(noun):
            return apply_rules(noun)
    raise ValueError('no matching rule for {0}'.format(noun))
