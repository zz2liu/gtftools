"""parsers for gtf files

TODO: replace parseLine, composeLine with gtf = FieldAttrFomatter()
"""
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import * #dict, zip, map, range, open, str, int, super,...
import pdb, collections, functools, itertools


#gtf fields
CHR, SOURCE, FEATURE, START, END, SCORE, STRAND, FRAME, ATTR = range(9)
COMMON_ATTRS = ['gene_id', 'transcript_id', 'exon_number', 'gene_name']
fieldNames = ('CHROM', 'SOURCE', 'FEATURE', 'START', 'END', 'SCORE', 'STRAND', 'FRAME')
GtfTuple = collections.namedtuple('GtfTuple', 
    'CHR SOURCE FEATURE START END SCORE STRAND FRAME ATTRS')

# attr_maker: fun(pairs) => dict like
def parseLine(line, attr_maker=collections.OrderedDict):
    rec = line.strip().split('\t')
    raw = rec[-1]
    pairs = raw.strip(';').split('; ')
    attrs = attr_maker(pair.split() for pair in pairs)
    for k in attrs.keys():
        attrs[k] = attrs[k].strip('"')
    rec[-1] = attrs
    return rec

def parseFile(gtf_file, attr_names=None):
    """write the gtf file to a csv file
    Note: gtf with a single feature type is recommended, eg, exon only or gene only

    gtf_file: the GTF file object.
    attr_names: a list of attrs to attract as extened fields; None to yield (rec, attrs).
    """
    for line in gtf_file:
        if line.startswith('#'):
            continue
        raw = parseLine(line)
        if attr_names:
            rec, attrs = raw[:-1], raw[-1]
            rec.extend([attrs.get(k, '.') for k in attr_names])
            yield rec
        else:
            yield raw

def _getAttrNamesFromFile(gtf_file, limit=100):
    res = []
    for rec in parseFile(itertools.islice(gtf_file,limit)):
        for k in rec[-1].keys():
            if k in res:
                continue
            res.append(k)
    return res

##### not tested below
#def composeLine(rec):
#    attrs = rec[-1]
#    pairs = [''.join((k, ' ', '"', v, '"')) for k, v in attrs.items()]
#    raw = '; '.join(pairs) + ';'
#    rec[-1] = raw
#    line = '\t'.join(rec) + '\n'
#    return line
#    
#class GtfRow(object):
#    def __init__(self, line=None):
#        self._row = None
#        if line:
#            self.parse(line)
#
#    def parse(self, line):
#        self._row = GtfTuple._make(parseLine(line))
#
#    def compose(self):
#        return composeLine(self._row)
#
#    __str__ = compose
#
#def GtfParser(lines):
#    for line in lines:
#        yield GtfRow(line)
#
#def parseLineFlat(line):
#    rec = line.strip().split('\t')
#    fields, raw = rec[:-1], rec[-1]
#    pairs = raw.strip(';').split('; ')
#    values = [pair.split()[1].strip('"') for pair in pairs]
#    fields.extend(values)
#    return fields 

    
