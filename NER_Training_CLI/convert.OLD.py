TRAIN_DATA = [
  (
    '現時恒指已跌穿重要支持位26500點來看，港股繼續尋底的機會是頗高的。',
    {
        'entities':
        [
         (2,4,'FIN'),(9,12,'FIN'),(21,23,'FIN'),(25,27,'FIN')
        ]
    }
  ),
  (
    '恆生指數和創業板指數。',
    {
      'entities': 
      [
        (0,4,'FIN'),(5,10,'FIN')          
      ]
    }
  ),  
  (
    '中電、匯控、和黃8月暴升8.5%。',
    {
      'entities': 
      [
        (0,2,'STOCK'),(3,5,'STOCK'),(6,8,'STOCK'),(8,10,'DATE'),(10,12,'FIN')         
      ]
    }
  ),
  (
    '恆指小雙底9月盼反彈。中電、匯控、和黃8月齊齊跌8.5%金融海嘯後最差。',
    {
      'entities': 
      [
        (0,2,'FIN'),(2,5,'FIN'),(5,7,'DATE'),(8,10,'FIN'),(11,13,'STOCK'),(14,16,'STOCK'),(17,19,'STOCK'),(19,21,'DATE'),(24,28,'DATE')      
      ]
    }
  ),     
  (
    '匯控(00005)將於下周一（2日）公布2021年度中期業績。',
    {
        'entities':
        [
          (0,2,'STOCK'),(11,14,'DATE'),(26,30,'FIN')
        ]
    }
  ),
  (
    '查看香港最新的股市報價、記錄、新聞及其他重要資訊，助你賣買股票及投資。',
   {
      'entities':
      [
        (2,4,'GPE'),(7,9,'FIN'),(9,11,'FIN')
      ]
   }
  ),
  (
    '匯控低開4%。港股收市跌。',
    {
        'entities':
        [
         (0,2,'STOCK'),(7,9,'FIN')
        ]
    }
  ),
  (
    '港股高開173點。',
   {
       'entities': [(0,2,'FIN'),(2,4,'FIN')]
   }
  ),
  (
    '報道引述匯控內部電郵稱',{'entities':[(4,6,'STOCK')]}
  ),
  (
    '匯控將在第四季開始進行股份回購',{'entities':[(0,2,'STOCK')]}
  ),
    (
    '花旗發表研究報告，下調匯控（0005）每股盈利預測',{'entities':[(11,13,'STOCK')]}
  ),
    (
    '匯控將恢復派息。',{'entities':[(0,2,'STOCK'),(5,7,'FIN')]}
  )
]

import pandas as pd
from tqdm import tqdm
import spacy
from spacy.tokens import DocBin

spacy_model = 'zh_core_web_lg'

nlp = spacy.load(spacy_model) # load a new spacy model

nlp.tokenizer.pkuseg_update_user_dict(['匯控','和黄','中電','派息','低開','高開','股份回購','每股盈利'])

db = DocBin() # create a DocBin object

for text, annot in tqdm(TRAIN_DATA): # data in previous format
    doc = nlp.make_doc(text) # create doc object from text
    ents = []
    for start, end, label in annot["entities"]: # add character indexes
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents # label the text with the ents
    db.add(doc)

db.to_disk("./train.spacy") # save the docbin object