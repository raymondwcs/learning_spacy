import spacy_pkuseg

# Training file: 'msr_training.utf8'.
# Test file: 'msr_test_gold.utf8'.
# Save the trained model to './models'.
# The training and test files are in utf-8 encoding.
spacy_pkuseg.train('cityu_training.utf8', 'cityu_test_gold.utf8', './models')	