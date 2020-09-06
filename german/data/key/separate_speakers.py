#quick rough script to split the Dirndl key file into the two speakers

with open("./Candidaten_Act5.part.xml.r2r7.0.Dirndl.conll", "r") as key_file:
  lines = key_file.read().splitlines()

  valer_file = open("./valer_speech.conll.response", "r+")
  johann_file = open("./johann_speech.conll.response", "r+")

  lines = lines[1:-1]

  for line in lines:
    print(line)
    if not line.strip():
      valer_file.write("\n")
      johann_file.write("\n")
    else:
      line_pieces = line.split()
      if (line_pieces[9]) == "valer":
        valer_file.write(line + "\n")
      else: 
        if (line_pieces[9]) == "johann":
          johann_file.write(line + "\n")