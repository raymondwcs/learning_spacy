# import pandas as pd
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

# nlp.tokenizer.pkuseg_update_user_dict(['匯控','和黄','中電','派息','低開','高開','股份回購','每股盈利'])

db = DocBin() # create a DocBin object

for line in tqdm(TRAIN_DATA): # data in previous format
    # print(type(line),line['text'],line['label'])
    doc = nlp.make_doc(line['text']) # create doc object from text
    ents = []
    for start, end, label in line["label"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object


EVAL_DATA = []
with open('eval_data.jsonl') as f:
    for jsonObj in f:
        x = json.loads(jsonObj)
        EVAL_DATA.append(x)

db = DocBin() # create a DocBin object

for line in tqdm(EVAL_DATA): # data in previous format
    # print(type(line),line['text'],line['label'])
    doc = nlp.make_doc(line['text']) # create doc object from text
    ents = []
    for start, end, label in line["label"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./eval.spacy") # save the docbin object
