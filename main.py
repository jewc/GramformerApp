
# 1. Install and import dependencies
from gramformer import Gramformer

# 2. Instantitate Gramformer
gf = Gramformer(models=3, use_gpu=True) # 0 = detector, 1 = highlighter, 2 = corrector, 3 = all

#3. Run Correction
gf.correct('My camera battery a dead')

sentences = [
    'I like for walks',
    'World is flat',
    'Red a color',
    'I wish my Computer was run faster.'
]

for sentence in sentences:
    res = gf.correct(sentence)
    print(res[0])
