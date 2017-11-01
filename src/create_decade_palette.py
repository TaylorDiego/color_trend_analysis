from set_similarity import SetSimilarity
import pickle
import pandas as pd

with open('../../pickle/sliced_fashion.pkl', 'rb') as f:
    df = pickle.load(f)

# print(df.head())

decade_list = [decade for decade in sorted(df['decade'].unique())]

decade_palettes = {}

def create_decade_palette(df):
    for decade in decade_list:
        decade_palettes[decade] = list(df.loc[df['decade'] == decade, 'slice_palette'])
    return decade_palettes

d_p_list = create_decade_palette(df)

for decade in decade_list:
    # print(decade)
    print(SetSimilarity().set_central_list(d_p_list[decade]))



# print(type(d_p_list))
