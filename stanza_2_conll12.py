class Converter:
  """
    converts the coreference from the stanza datatype obtained using the corenlp interface to conll12
    stanza_object -- stanza data obtained from stanza.annotate() or similar
  """
  def __init__(self, stanza_object):
    self.__stanza_object = stanza_object
    #list of sentences, which themselves are lists of word/coref info pairs
    #each pair has the word token and then a list of coref info markers in the format (start, (single line) or end)
    self.__sentence_list = []

  class WordInfoPair:
    """
    helper class for word pairs
    word -- word from token
  """
    def __init__(self, word):
      self.__word = word
      self.__coref_info = []

    def get_word(self):
      return self.__word

    def set_word(self, word):
      self.__word = word
    
    def get_coref_info(self):
      return self.__coref_info
    
    def add_to_coref_info(self, coref_marker):
      self.__coref_info.append(coref_marker)

  def parse_stanza_object(self):
    """
    Parse the given stanza object and add its words and coref info to sentence_list 
    """
    #add words to list
    print("adding words...")
    for _,s in enumerate(self.__stanza_object.sentence):
      word_list = []
      for t in s.token:
        word_list.append(self.WordInfoPair(t.word))
      
      self.__sentence_list.append(word_list)

    #go through the coref chains, and add info for all the mentions
    print("adding tokens...")
    chains = self.__stanza_object.corefChain
    for chain in chains:
      id = str(chain.chainID)
      for mention in chain.mention:
        start = mention.beginIndex
        #the document seems to index the spaces between tokens rather than the tokens themselves, so we subtract by 1 here
        end = mention.endIndex - 1

        #check if mention is one token long
        if start == end:
          self.__sentence_list[mention.sentenceIndex][start].add_to_coref_info("(" + id + ")")
        else:
          self.__sentence_list[mention.sentenceIndex][start].add_to_coref_info("(" + id)
          self.__sentence_list[mention.sentenceIndex][end].add_to_coref_info(id + ")")
      
  def write_to_conll12(self, document_name, output):
    """
      Writes the parsed sentence_list to the output file in CoNLL12 format.
      This skips a lot of the info that could be added, and just adds coref annotations.
      document__name -- name of document that was originally parsed by CoreNLP, or whatever you called your document in the gold mentions.
      output -- path to output file.
    """
    print("writing to file " + output)
    with open(output, "w") as file:
      file.write("#begin document (%s); part 000\n" % document_name)
      
      for s in self.__sentence_list:
        index = 0
        for w in s:
          raw_coref = w.get_coref_info()
          coref_string = ""
          if not raw_coref:
            coref_string = "-"
          else:
            coref_string = "|".join(raw_coref)
          
          line = "%s  0 %d  %s  %s\n" % (document_name, index, w.get_word(), coref_string)
          file.write(line)
          
          index = index + 1
        
        file.write("\n")

      file.write("#end document\n")

