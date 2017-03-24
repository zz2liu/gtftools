# gtf2csv / GTF converters / gtf_to_csv 
Convert a GTF file to a comma seperated file (CSV) with the original order of fields and attributes.
# Installation
Extract source files to a directory.
# Install dependencies/requirements
python2.7+  or python3.5+
```
pip install future
```
# Usage
From your installation folder,
```
python gtf_to_csv.py test_gtf.gtf > test_gtf.csv
```
The attribute names are extracted from the first 100 GTF lines. The place holder for a missing attribute is '.'.  Please see the test_gtf.gtf and test_gtf.csv for an example input and output. 
# Contributors
* Zongzhi Liu - Associate Research Scientist, Dept. of Pathology, Yale University

You are welcome to contact me by email: firstname.lastname@yale.edu

Enjoy!
