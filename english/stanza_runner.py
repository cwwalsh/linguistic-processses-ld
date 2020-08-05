import stanza
import os
import sys
import stanza_2_conll12
os.environ["CORENLP_HOME"] = "./corenlp"
from stanza.server import CoreNLPClient

#get name to use for document and path to raw document from command parameters
file_path = sys.argv[1]
file_name = sys.argv[2]

#start corenlp server with necessary annotators, 8gb RAM, 10 minute timeout and max file characters of 150k
with CoreNLPClient(properties={
  "annotators": "tokenize, ssplit, pos, lemma, ner, parse, coref",
  "coref.algorithm": "neural"
}, 
memory="8G", 
timeout=600000,
max_char_length=150000) as client:
  with open(file_path,mode="r") as file:
    raw_text = file.read()

  document = client.annotate(raw_text)

test = stanza_2_conll12.Converter(document)
test.parse_stanza_object()
test.write_to_conll12(file_name, "%s.response" % (file_name))