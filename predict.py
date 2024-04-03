from flair.data import Sentence
from flair.models import SequenceTagger

tagger: SequenceTagger = SequenceTagger.load("ner")

sentence: Sentence = Sentence("George Washington went to Washington .")
tagger.predict(sentence)


print("Analysing the sentence %s" % sentence)
>>>>>>> feature-13
print("\nThe following NER tags are found: \n")
print(sentence.to_tagged_string())
