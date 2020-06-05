"""
This module is here for string completions. This means mostly stuff where
strings are returned, like `foo = dict(bar=3); foo["ba` would complete to
`"bar"]`.

It however does the same for numbers. The difference between string completions
and other completions is mostly that this module doesn't return defined
names in a module, but pretty much an arbitrary string.
"""
import re

from medi._compatibility import unicode
from medi.inference.names import AbstractArbitraryName
from medi.inference.helpers import infer_call_of_leaf
from medi.api.classes import Completion
from medi.parser_utils import cut_value_at_position

_sentinel = object()


class StringName(AbstractArbitraryName):
    api_type = u'string'
    is_value_name = False





def _get_string_prefix_and_quote(string):
    match = re.match(r'(\w*)("""|\'{3}|"|\')', string)
    if match is None:
        return None, None
    return match.group(1), match.group(2)


def _matches_quote_at_position(code_lines, quote, position):
    string = code_lines[position[0] - 1][position[1]:position[1] + len(quote)]
    return string == quote


def get_quote_ending(string, code_lines, position, invert_result=False):
    _, quote = _get_string_prefix_and_quote(string)
    if quote is None:
        return ''

    # Add a quote only if it's not already there.
    if _matches_quote_at_position(code_lines, quote, position) != invert_result:
        return ''
    return quote
