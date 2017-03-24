#convenient wrapper of gtf.py
import collections
from working import gtf

def parseLineReplacingGeneId(line):
    """replacing gene_id with gene_id|gene_name, keep others in ori order."""
    row = gtf.parseLine(line, _attr_maker)
    row[-1]['gene_id'] = '|'.join((row[-1].get('gene_id', '.'), row[-1].get('gene_name', '.')))
    return row

def _attr_maker(pairs):
    """make sure that gene_id is the first key."""
    res = collections.OrderedDict.fromkeys(['gene_id'], '.')
    res.update(pairs)
    return res

