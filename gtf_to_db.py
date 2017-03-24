from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import * #dict, zip, map, range, open, str, int, super,...
import sys, io, sqlite3 
import gtf

usage = """import a gtf file a single feature type (the 3rd column) to a sqlite database
example: PROG a.gtf, b.sqlite exon
"""
def main(db_name, gtf_name, 
        table_name='gtf', attr_names=True):
        #table_name='gtf', attr_names=COMMON_ATTRS):
    """write the gtf file to a sqlite database.
    Note: gtf with a single feature type is recommended, eg, exon only or gene only

    db_name: the database file name.
    table_name: the table to be created and populated with gtf fields.
    gtf_name: the GTF file name.
    attr_names: the list of GTF attribute names to be written to table.
    """
    if attr_names is True:
        attr_names = _get_attr_names_from_first_line(gtf_name)
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    CREATE = '''create table %s (Chrom text, Source text, Feature text,
            Start int, End int, Score real, Strand text, Frame text, %s)
            ''' % (table_name, ', '.join(attr_names))
    NFIELD = 8
    ncol = NFIELD + len(attr_names)
    INSERT = '''insert into %s values (%s)
            ''' % (table_name, ','.join('?'*ncol))

    cur.execute(CREATE)
    for rec in gtf.parseFile(open(gtf_name), attr_names):
        cur.execute(INSERT, tuple(rec)) 
    #import pdb; pdb.set_trace()
    con.commit()
    con.close()

def _get_attr_names_from_first_line(gtf_name):
    file = open(gtf_name)
    for line in file:
        if line.startswith('#'):
            continue
        raw = gtf.parseLine(line)
        return list(raw[-1].keys())

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args)!=3:
        print (usage)
        sys.exit(1)
    main(*args)

