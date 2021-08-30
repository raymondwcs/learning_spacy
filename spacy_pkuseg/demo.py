import spacy
MODEL = 'zh_core_web_lg'

text = '（星島日報報道）本港運動員在東奧取得一金兩銀三銅的歷史佳績，令全城掀起一片體育熱。體育專員楊德強接受本報專訪時表示，本港運動風氣隨奧運而得到提升，直接有助啟德體育園日後營運，透露園區有機會早至二○二三年初便開始試運，率先舉辦小規模賽事和測試票務系統，意味市民屆時已可享用園區部分設施。隨著國務院日前批准粵港澳承辦二○二五年全運會，楊德強指本港過去已累積不少大型單項國際賽事的舉辦經驗，加上啟德體育園屆時已啟用，成為區內最先進場地之一，可承辦賽事的可能性十分多，而本港在硬件設施上，甚至有能力舉辦賽事的開幕和閉幕禮，但強調當屆賽事是由大灣區共同舉辦，一切有待粵港澳政府共同研究和分工'

nlp = spacy.load(MODEL)
doc1 = nlp(text)
print(doc1.text)
for token in doc1:
    print(token.text, token.pos_, token.dep_)

print()

nlp.tokenizer.initialize(pkuseg_model="./models")
doc2 = nlp(text)
print(doc2.text)
for token in doc2:
    print(token.text, token.pos_, token.dep_)
