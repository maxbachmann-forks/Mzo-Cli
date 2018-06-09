import json
from enum import Enum

from monzo.utils import ascii_table, csv
from monzo.utils.dict_helpers import unify_dicts


class Format(Enum):
    human = 'human'
    json = 'json'
    csv = 'csv'

    def dumps(self, dicts=None, keys=None, title=None, fill=None):
        if self is Format.human:
            return ascii_table(dicts=dicts, columns=keys, title=title, fill=fill)
        elif self is Format.json:
            dicts = unify_dicts(dicts, key_order=keys, fill=fill)
            return json.dumps(dicts, indent=2)
        elif self is Format.csv:
            dicts = unify_dicts(dicts, key_order=keys, fill=fill)
            return csv.dumps(dicts)
        else:
            raise NotImplementedError('Unknown output format', self)