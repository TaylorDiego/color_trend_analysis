from set_similarity import SetSimilarity
import pickle
import pandas as pd

with open('../../pickle/fashion.pkl', 'rb') as f:
    df = pickle.load(f)

print(df.head())
