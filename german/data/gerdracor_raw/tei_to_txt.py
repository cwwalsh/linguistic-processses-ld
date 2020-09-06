#reads through the raw XML source file, and converts the speech of the two characters into a simple txt file

from bs4 import BeautifulSoup

with open("./german_source.xml", "r") as  tei_doc:
  act_5 = BeautifulSoup(tei_doc, "lxml").find_all(type="act")[4]

  with open("../valer_speech.txt", "w") as valer_file:
    valer_parts = act_5.find_all(who="#valer")

    for part in valer_parts:
      valer_file.write(part.p.getText() + "\n")

  with open("../johann_speech.txt", "w") as valer_file:
    valer_parts = act_5.find_all(who="#johann")

    for part in valer_parts:
      valer_file.write(part.p.getText() + "\n")