import numpy as np
import cv2
from colorthief import ColorThief
import io
import matplotlib.pyplot as plt
%matplotlib inline

class Palettization():
    """processes a single image path and returns image, centroids(dominant colors), palette"""

    def __init__(self, img_path):
        self.img_path = img_path
        self.img_palette = self.get_palette_()
        self.color_arr = self.get_color_array()
        self.centroid_lst = self.arrayify_centroids()
        self.counts = self.centroid_cos_similar()

    def get_palette_(self):
        """return image color palette"""
        colorthief = ColorThief(self.img_path)
        img_palette = colorthief.get_palette(color_count=7, quality=1)
        return img_palette


    def get_color_array(self):
        """return array of palette colors"""
        color_arr = []
        for color in self.img_palette:
            color_val = []
            for rgb_val in color:
                color_val.append(rgb_val/255)
            color_arr.append(tuple(color_val))
        return color_arr


    def arrayify_centroids(self):
        """return array of image palette (centroids)"""
        self.centroid_lst = np.array(self.img_palette)
        return self.centroid_lst

    def _centroid_cos_similar(self, pixels, centroid):
        numerator = (pixels * centroid).sum(axis=1)
        denominator = (np.linalg.norm(pixels, axis=1) * np.linalg.norm(centroid))
        return (numerator / denominator)


    def centroid_cos_similar(self):
        """"""
        lst = []
        self.centroid_lst = self.img_palette
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        for centroid in self.centroid_lst:
            lst.append(self._centroid_cos_similar(img.reshape(-1, 3), centroid))

        centroid_argmax = np.array(lst).argmax(axis=0)

        _, counts = np.unique(centroid_argmax, return_counts=True)
        return counts


    def zip_centroid_count(self):
        """"""
        return [{'rgb': rgb, 'count':count} for rgb, count in zip(self.img_palette, self.counts)]


    def display_palette(self):
        """"""
        self.get_color_array()
        return plt.imshow([(self.color_arr)])


    def display_img(self):
        """"""
        colorthief = ColorThief(self.img_path)
        img = colorthief.image
        return img
