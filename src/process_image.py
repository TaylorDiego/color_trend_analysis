from skimage import io as skio








url = 'http://i.stack.imgur.com/SYxmp.jpg'
img = skio.imread(url)

print("shape of image: {}".format(img.shape))
print("dtype of image: {}".format(img.dtype))
