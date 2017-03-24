#!/usr/bin/env python
from __future__ import division, print_function, absolute_import, unicode_literals
from builtins import * #dict, zip, map, range, open, str, int, super,...
import unittest, pdb, difflib, collections, os
import gtf_to_db

gtf_file = 'test_gtf.gtf'
gtf_lines = [x for x in open(gtf_file, 'r') if not x.startswith('#')]

class GtfToDbTests(unittest.TestCase):
    """tests for gtf_to_db"""
    def test__get_attr_names_from_first_line(self):
        res = gtf_to_db._get_attr_names_from_first_line(gtf_file)
        #print(res)
        self.assertEquals(res, ['gene_id', 'transcript_id', 'exon_number',
            'gene_name', 'oId', 'nearest_ref', 'class_code', 'tss_id', 'p_id'])
    def test_gtf_to_db(self):
        if os.path.isfile('tmp.sqlite'): 
            os.remove('tmp.sqlite')
        gtf_to_db.main(gtf_name='test_gtf.gtf', db_name='tmp.sqlite')

if __name__ == '__main__':
    unittest.main()

