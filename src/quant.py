# import the necessary packages
from sklearn.cluster import MiniBatchKMeans
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "/Users/Rabbit/Downloads/china_test.jpg")
ap.add_argument("-c", "--clusters", required = True, type = int, help="8")
args = vars(ap.parse_args())
