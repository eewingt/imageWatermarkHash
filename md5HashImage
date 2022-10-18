from PIL import Image
import hashlib

md5hash = hashlib.md5(Image.open('watermarkingimage\Capture.PNG').tobytes())
md5hash2 = hashlib.md5(Image.open('watermarkingimage\capture2.jpg').tobytes())
print(md5hash.hexdigest())
print(md5hash2.hexdigest())
