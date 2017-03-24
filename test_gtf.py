#!/usr/bin/env python
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import * #dict, zip, map, range, open, str, int, super,...
import unittest, pdb, difflib, collections, os
import gtf

gtf_fname = 'test_gtf.gtf'
gtf_lines = [x for x in open(gtf_fname, 'r') if not x.startswith('#')]

row0_fields = ['chr18', 'coding', 'exon', '19761414', '19761539', '.', '+', '.']
row0_attrs = [('gene_id', 'ucscCodingXLOC_011257'), ('transcript_id', 'ucscCodingTCONS_00032665'), 
    ('exon_number', '3'), ('gene_name', 'GATA6'),
    ('oId', 'uc002ktu.1'), ('nearest_ref', 'uc002ktu.1'),
    ('class_code', '='), ('tss_id', 'ucscCodingTSS16366'), ('p_id', 'P23329')]

class GtfRowTests():#unittest.TestCase):
    """tests for class GtfRow."""
    def test___init_with_line(self):
        obj0 = gtf.GtfRow(gtf_lines[0])
        #shelf['obj0'] = obj0; shelf.close()
        self.assertEquals(list(obj0._row), shelf['row0'])

    def test___init_default(self):
        obj = gtf.GtfRow()
        print (obj._row)
        obj.parse(gtf_lines[0])
        print (obj._row)
        #pdb.set_trace()

    def test___str(self):
        obj0 = shelf['obj0']
        print (str(obj0))
        
class Tests(unittest.TestCase):
    """tests for root functions"""
    def setUp(self):
        pass
    def test_parseLine(self):
        res = gtf.parseLine(gtf_lines[0])
        #shelf['row0'] = res; shelf.close()
        #print(res)
        self.assertEquals(res[:-1], row0_fields)
        self.assertEquals(res[-1], collections.OrderedDict(row0_attrs))

    def test__getAttrNamesFromFile(self):
        res = gtf._getAttrNamesFromFile(gtf_lines)
        self.assertEquals(res, ['gene_id', 'transcript_id', 'exon_number',
            'gene_name', 'oId', 'nearest_ref', 'class_code', 'tss_id', 'p_id', 'new_attr'])
        #print(res)

    def test_parseFile(self):
        res = list(gtf.parseFile(open(gtf_fname)))
        self.assertEquals(len(res[0]), 9)
        #print(len(res), len(res[0]))

    def test_parseFile_with_attrs(self):
        res = list(gtf.parseFile(open(gtf_fname), attr_names=['gene_id', 'transcript_id']))
        self.assertEquals(len(res[0]), 10)
        #print(res)

    def _test_composeLine(self):
        res = gtf.composeLine(shelf['row0'])
        self.assertEquals(gtf_lines[0], res)

    def _test_run_modify_gene_id(self):
        for line in gtf_lines:
            row = gtf_.parseLineReplacingGeneId(line)
            new_line = gtf.composeLine(row)
            delta = difflib.context_diff(line.split(), new_line.split(), n=0)
            #print ('\n'.join(i for i in delta if i not in ['*** \n', '--- \n']))
            print ((line, new_line))

    def tearDown(self):
        pass
    

if __name__ == '__main__':
    unittest.main()

