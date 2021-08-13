!/bin/sh
python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./eval.spacy --gpu-id -1