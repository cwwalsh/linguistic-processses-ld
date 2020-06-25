import stanza
import os
os.environ["CORENLP_HOME"] = "./corenlp"
from stanza.server import CoreNLPClient

client = CoreNLPClient(annotators=["coref"], memory="4G")

text = "Albert Einstein and Kiera Cullen were pretty neat. They made things. He was old and she was young. She was an engineer."

document = client.annotate(text)

print(document.text)
print(document.mentions[0].entityMentionText)
print(document.corefChain)
# print(document)