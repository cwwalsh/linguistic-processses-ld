import stanza
import os
import stanza_2_conll12
os.environ["CORENLP_HOME"] = "./corenlp"
from stanza.server import CoreNLPClient

with CoreNLPClient(properties="corenlp.properties", memory="6G") as client:

  text = "Albert Einstein and Kiera Cullen were pretty neat. They made things. He was old and she was young. She was an engineer."

  document = client.annotate(text)

  test = stanza_2_conll12.Converter(document)
  test.parse_stanza_object()
  test.write_to_conll12("tes", "tes.response")