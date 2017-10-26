from set_similarity import SetSimilarity
import pickle
import pandas as pd

with open('../../pickle/fashion.pkl', 'rb') as f:
    df = pickle.load(f)

# print(df.head())

decade_list = [decade for decade in sorted(df['decade'].unique())]

decade_palettes = {}

def create_decade_palette(df):
    for decade in decade_list:
        print(decade)
        decade_palettes[decade] = list(df[df['decade'] == decade, 'palette'])
    return decade_palettes

d_p_list = create_decade_palette(df)

print(d_p_list)
