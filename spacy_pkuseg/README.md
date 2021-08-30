# Train `pkuseg` on Traditional Chinese Text
This project demonstrates how to train [`pkuseg`](https://github.com/explosion/spacy-pkuseg) on custom datasets.

## Training and Testing datasets
The following datasets were published by [ICWB2](https://github.com/yuikns/icwb2-data):

1. [`cityu_training.utf8`](cityu_training.utf8)
2. [`cityu_test_gold.utf8`](cityu_test_gold.utf8)

## Training
1. `pip install [`spacy-pkuseg`](https://github.com/explosion/spacy-pkuseg)`
2. `python [`train.py`](train.py)`
3. Trained model is saved in folder [`models`](./models)

## Using the trained model in spacy
```
import spacy
MODEL = 'zh_core_web_lg'

nlp.tokenizer.initialize(pkuseg_model="./models")
doc = nlp(text)
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)
```
See [`demo.py`](demo.py) for more details.
