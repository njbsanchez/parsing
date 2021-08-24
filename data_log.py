"""
thought process:
    - how many files would I need to ingest
    - would this process need to be scaled overtime?
    - will all entries have status code
    - how many different kinds of requests are there?
    - what are we optimizing?
        - time?
        - scalability?
        - memory?
    - will info in log be used for other uses?
    
simple solution (assumption - time, small files):
    - ingest files
    - if line meets given criteria, add to a compiled list
    - return list
    * no memory wasted, o(n) memory
    
alternative solution (assumption, scalability of data use is priority)

- import files
- create a db
- format info into sql table
- query on all data that meets given criteria

adtl assumption (assumption large files):
    - use map reduce to further split file up into smaller files
    - use either process to process data
    - in process of furthering knowledge in map reduce, can potentially use hadoop to track further data input, can auto ingest new lines in real time.


"""




import os
import pandas as pd
directory = 'parsing/text_txt'

def imp_files(dir):
    """
    """
    all_entries = []
    for filename in os.listdir(dir):
        if filename.endswith(".txt"):
            with open(filename) as f:
                for line in f:
                    line_details = format_info(line)
                    all_entries.append(line_details)
    
    return all_entries
                
def format_info(line):
    if len(line) < 20:
        return None
    details = line.split(" ", 2)
    details[2] = details[2].split(":", 1)
    
    return details

def get_all_warnings(entry_list):
    
    
    





