from collections import defaultdict, OrderedDict
from operator import itemgetter
import numpy as np
import cv2
from colorthief import ColorThief
import io
from colorutils import Color
import matplotlib.pyplot as plt
%matplotlib inline


class SetSimilarity():
    """find set(palette) most 'central' of sets, consisting of items(rgb vector) """

    #def __init__(self, set_of_palettes):
    #    self.p_list= list_of_palettes

    def c2c_dist(self, color_a, color_b):
        """return the distance(float) between two items(rgb vectors)"""
        dist_c2c = np.linalg.norm(np.array(color_a) - np.array(color_b))
        return(dist_c2c)

    def c2p_dist(self, color_a, palette_b):
        """return minimum distance(float) between an item(rgb vector) and a set(palette)"""
        """find min dist between color_a and all colors in palet_b
        use c2c_dist"""
        dist_c2p_list = []
        for color in palette_b:
            dist = self.c2c_dist(color, color_a)
            dist_c2p_list.append(dist)
        dist_c2p = np.amin(dist_c2p_list)
        return(dist_c2p)

    def p2p_dist(self, palette_a, palette_b):
        """return sum(float) of c2p_dist between two sets(palette)"""
        # sum of c2p-dists
        dist_p2p_list = []
        for color in palette_a:
            dist_p2p_list.append(self.c2p_dist(color, palette_b))
            dist_p2p = np.sum(dist_p2p_list)
        return(dist_p2p)

    def set_central_list(self, list_of_palettes):
        """return most 'central' set(palette(s), if there are multiples)"""
        p_cent_list = []

        for palette_a in list_of_palettes:
            palette_a_centrality_list = []

            for palette in list_of_palettes:
                palette_a_centrality_list.append(self.p2p_dist(palette_a, palette))

            sum_temp = np.sum(palette_a_centrality_list)
            p_cent_list.append((sum_temp, palette_a))

        p_min = min(p_cent_list, key=itemgetter(0))[0]
        p_cent_list_srtd = sorted(p_cent_list, key=lambda x: x[0])

        p_central = [ x for x in p_cent_list_srtd if x[0]==p_min ]
        return(p_central)
