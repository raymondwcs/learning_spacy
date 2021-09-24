from tqdm import tqdm
import spacy
import json
from spacy.tokens import DocBin

spacy_model = 'zh_core_web_lg'
train_file = 'train_data.jsonl'
eval_file = 'eval_data.jsonl'

nlp = spacy.load(spacy_model) # load a new spacy model

TRAIN_DATA = []
with open(train_file) as f:
    for line in f:
        jsonObj = json.loads(line)
        TRAIN_DATA.append(jsonObj)

print('read from {}, {} lines'.format(train_file,len(TRAIN_DATA)))

db = DocBin() # create a DocBin object
for line in tqdm(TRAIN_DATA): # data in previous format
    doc = nlp.make_doc(line['text']) # create doc object from text
    ents = []
    for start, end, entities in line["entities"]: # add character indexes
        span = doc.char_span(start, end, label=entities, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # entities the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object


EVAL_DATA = []
with open(eval_file) as f:
    for line in f:
        jsonObj = json.loads(line)
        EVAL_DATA.append(jsonObj)

print('read from {}, {} lines'.format(eval_file,len(EVAL_DATA)))


db = DocBin() # create a DocBin object
for line in tqdm(EVAL_DATA): # data in previous format
    doc = nlp.make_doc(line['text']) # create doc object from text
    ents = []
    for start, end, entities in line["entities"]: # add character indexes
        span = doc.char_span(start, end, label=entities, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # entities the text with the ents
    db.add(doc)

db.to_disk("./eval.spacy") # save the docbin object
