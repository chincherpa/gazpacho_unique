import os
import sys
import tempfile
import urllib.request

from gazpacho import Soup, get

import resize

url = sys.argv[1]
print(url)

folder_download = tempfile.gettempdir()
folder_save = "U:/Fotos/Austausch Hannah - Lutz/unique"

# urls = ["https://www.juniqe.de/a-hero-premium-poster-portrait-2674808.html?_sp=c5abf008-92e6-4178-933b-0b317361bccd.1571860545825",
# "https://www.juniqe.de/wild-world-premium-poster-portrait-2841204.html?_sp=c5abf008-92e6-4178-933b-0b317361bccd.1571860722313"]

# for url in urls:
print("Fetch URL:", url)
html = get(url)
soup = Soup(html)

result = soup.find("div", {"class": "filter-by-design-header__image-wrap"})
result = result.find("img")

path_to_image_sm = result.attrs["src"]
path_to_image_big = path_to_image_sm.replace("x386", "x1200")

filename = path_to_image_big.rsplit("/")[-1]
path = os.path.join(folder_download, filename)
print(filename, "->", path)

print("Save Image:", filename)
urllib.request.urlretrieve(path_to_image_big, path)

filename_in = path
filename_out = os.path.join(folder_save, filename)
new_width = 3000

print("Resize Image:", filename)
resize.resize_image(filename_in, filename_out, new_width)

print("done")
