import sys
import os
import re

#get name to use for document and path to document from command parameters
#this tool accepts files that have already been parsed by Corzu, or in theory any file similar in the CONLL format CorZu uses
file_path = sys.argv[1]
file_name = sys.argv[2]

with open(file_path) as file:
  lines = file.read().splitlines()

#remove the last trailing whitespace
lines = lines[:-1]

format_file = file_name + ".response"
with open(format_file ,"w") as file:
  file.write("#begin document (%s); part 000\n" % file_name)
  
  #iterate through each line,and write an entry to the output file with the relevant information for coreference - word, number and chain ID
  word_number = 0
  for line in lines:
    if not line.strip():
      file.write("\n")
      #when you get to the end of a sentence, reset the word number
      word_number = 0
    else:  
      line_pieces = line.split()
      file.write("%s  000 %d  %s  %s\n" % (file_name, word_number, line_pieces[1], line_pieces[9]))
      word_number += 1
  
  file.write("\n#end document\n")