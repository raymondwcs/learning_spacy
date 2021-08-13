from tqdm import tqdm
import spacy
import json
from spacy.tokens import DocBin

spacy_model = 'zh_core_web_lg'

TRAIN_DATA = []
with open('train_data.jsonl') as f:
    for jsonObj in f:
        x = json.loads(jsonObj)
        TRAIN_DATA.append(x)

nlp = spacy.load(spacy_model) # load a new spacy model
db = DocBin() # create a DocBin object

for line in tqdm(TRAIN_DATA): # data in previous format
    # print(type(line),line['text'],line['entities'])
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
with open('eval_data.jsonl') as f:
    for jsonObj in f:
        x = json.loads(jsonObj)
        EVAL_DATA.append(x)

db = DocBin() # create a DocBin object

for line in tqdm(EVAL_DATA): # data in previous format
    # print(type(line),line['text'],line['entities'])
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
