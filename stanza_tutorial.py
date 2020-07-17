import stanza
import os
os.environ["CORENLP_HOME"] = "./corenlp"
from stanza.server import CoreNLPClient

with CoreNLPClient(properties="corenlp.properties", memory="6G") as client:

  text = "Albert Einstein and Kiera Cullen were pretty neat. They made things. He was old and she was young. She was an engineer."

  document = client.annotate(text)

  # print(document.text)
  # print(document)
  # print ("----MENTIONS----")
  # print(document.mentions)
  # print ("----MENTIONS----")
  # print(document.mentionsForCoref)
  # print ("----CHAINS----")
  # print(document.corefChain)
  # print ("----CHAINSParsed----")
  
  chains = document.corefChain
  for chain in chains:
    print(chain.chainID)
    for m in chain.mention:
      print(document.mentionsForCoref[m.mentionID].headString)
      print(m)
    print("---------------")


  # print(document)