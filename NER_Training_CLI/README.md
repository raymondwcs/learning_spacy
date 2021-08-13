# NER Training via Command Line Interface ([CLI](https://spacy.io/api/cli#train))
## Steps
1. Prepare training data. Convert `train_data.jsonl` and `eval_data.jsonl` to [DocBin](https://spacy.io/api/docbin) format:

```Shell
python ./convert.py
```

2. Start training via cli. To use GPU, change `--gpu-id -1` to `--gpu-id 0`

```Shell
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./eval.spacy --gpu-id -1
```

3. *Trained* model is saved in `output` folder.  To use the trained model:
```Python
import spacy
nlp = spacy.load('output/model-last')
```
