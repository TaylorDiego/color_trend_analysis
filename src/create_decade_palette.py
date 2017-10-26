from set_similarity import SetSimilarity
import pickle
import pandas as pd

with open('../../pickle/fashion.pkl', 'rb') as f:
    df = pickle.load(f)

decade_list = [decade for decade in sorted(df['decade'].unique())]

print(decade_list)

def create_decade_palette(df):
    pass
