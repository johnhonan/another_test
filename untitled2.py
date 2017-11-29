# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:26:11 2017

@author: 89514
"""

from collections import OrderedDict
import csv
import re

def analyze_log(f):
    stats = OrderedDict()
    for line in f:
        _, _, rw_datatype, _, core_varname, _ = line.split()
        match = re.search(r'.*[*\\](.*)', core_varname)
        if not match:
            continue
        var = match.group(1)
        match = re.search(r'([01])\\Global', core_varname)
        core = match and match.group(1) or 'X'
        rw, datatype = rw_datatype.split('-', 1)

        var_stats = stats.get(var, {'rd': {'0': 0, '1': 0, 'X': 0},
                                    'wr': {'0': 0, '1': 0, 'X': 0},
                                    'type': datatype })
        stats[var] = var_stats
        var_stats[rw][core] += 1
    return stats


def main(input_filename, output_filename):
    with open(input_filename) as input_file:
        stats = analyze_log(input_file)


if __name__ == '__main__':
    main(r'C:\Users\AEC_FULL\…\core1_sram_ReadWrite.txt',
         r'C:\Users\AEC_FULL\…\ParsedOutput.csv')
    
    