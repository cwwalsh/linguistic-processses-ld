import sys
import os
import re

file_path = sys.argv[1]
file_name = sys.argv[2]

with open(file_path) as file:
  lines = file.read().splitlines()

lines = lines[:-1]

format_file = file_path + ".format"
with open(format_file ,"w") as file:
  file.write("#begin document (%s); part 000\n" % file_name)
  
  word_number = 0
  for line in lines:
    if not line.strip():
      file.write("\n")
      word_number = 0
    else:  
      line_pieces = line.split()
      file.write("%s  0 %d  %s  %s\n" % (file_name, word_number, line_pieces[1], line_pieces[9]))
      word_number += 1
  
  file.write("#end document\n")