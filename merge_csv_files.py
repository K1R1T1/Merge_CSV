# -*- coding: utf-8 -*-
"""
Author : Kiriti Yelamanchali 
Title: Merge CSV files into one. 
"""

###############################################################################
#Import Libraries 
import glob
###############################################################################

###############################################################################
#User Input 
#Change the input directory
directory = "C:/Users/E046088/Desktop/MEE" 
###############################################################################


###############################################################################
#Code
to_merge = glob.glob(directory+"/*.csv")
to_merge.sort()
header_saved = False
outputfile = "Merged_File.csv"
with open(outputfile,'w', encoding = 'utf-8-sig') as mergedfile:
    for filename in to_merge:
        with open(filename, encoding = 'utf-8-sig') as infiles:
            header = next(infiles)
            if not header_saved:
                mergedfile.write(header)
                header_saved = True
            for line in infiles:
                mergedfile.write(line)
print("Check the merged file located at: "+ directory + "/" + outputfile)
###############################################################################