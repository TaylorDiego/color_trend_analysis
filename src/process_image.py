import matplotlib.pyplot as plt
%matplotlib inline


palette_list = []
color_tup_lst = []
color_val = []

def display_color(color_arr):
    return plt.imshow([(color_arr)])
    #color_tup_lst = []

def convert_rgb_to_percent(pal_test):
    for color in pal_test:
        for rgb_val in color:
            color_val.append(rgb_val/255)
        color_tup_lst.append(tuple(color_val))
        color_val.clear()

    return color_tup_lst
