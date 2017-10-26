from set_similarity import SetSimilarity
import pickle
import pandas as pd

with open('../../pickle/fashion.pkl', 'rb') as f:
    df = pickle.load(f)

print(df.head())

decade_list = [decade for decade in sorted(df['decade'].unique())]

decade_palettes = {}

def create_decade_palette(df):
    for decade in decade_list:
        decade_palettes[decade] = list(df['palette'])
    return decade_palettes

create_decade_palette(df)
