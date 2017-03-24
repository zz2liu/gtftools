from __future__ import division, print_function, absolute_import, unicode_literals
import sys, csv 
import gtf

usage = """convert a gtf file to csv rows with header. 

example: PROG a.gtf > a.csv
"""

def main(gtf_name, outfile):
    attrNames = gtf._getAttrNamesFromFile(open(gtf_name), 100)
    outCsv = csv.writer(sys.stdout)
    outCsv.writerow(list(gtf.fieldNames)+list(attrNames))
    for row in gtf.parseFile(open(gtf_name), attrNames):
        outCsv.writerow(row)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args)!=1:
        print (usage)
        sys.exit(1)

    (gtf_fname,) = args
    main(gtf_fname, sys.stdout)



