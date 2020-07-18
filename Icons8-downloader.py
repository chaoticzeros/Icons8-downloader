import os
import shutil

import imageio
import requests

# Enter URL of icon category to download

PACK = "flat_round"
DEFAULT_SIZE = "2x"

URL = "https://icons8.com/icons/" + PACK

if DEFAULT_SIZE.endswith("x"):
    target = "100x"
else:
    target = "1100"

# Get list of categories
pack_name = URL.split("/")[-1]
r = requests.get(URL)
response = r.content.decode('utf-8')
response = response.split(' ')
category_list = [x for x in response if x.startswith("href=\"/icons/pack")]
category = [x.split("/")[-1][:-1] for x in category_list]
category_url = ['https://icons8.com/icon/pack/' + x + '/' + pack_name for x in category]

# Create directories
png_path = "{} PNG".format(PACK.capitalize())
ico_path = "{} ICO".format(PACK.capitalize())

if not os.path.exists("data"):
    os.mkdir("data")

if not os.path.exists(os.path.join("data", png_path)):
    os.mkdir(os.path.join("data", png_path))
if not os.path.exists(os.path.join("data", ico_path)):
    os.mkdir(os.path.join("data", ico_path))

for cat in category:
    path = os.path.join("data", png_path, cat)
    if not os.path.exists(path):
        os.mkdir(path)
    path = os.path.join("data", ico_path, cat)
    if not os.path.exists(path):
        os.mkdir(path)

# Download PNG
print("Downloading PNG files")
length = len(category)
count = 1
cats = zip(category, category_url)
for cat, url in cats:
    r = requests.get(url)
    print('\n{} ({}/{})'.format(cat, count, length))
    response = r.content.decode('utf-8')
    response = response.split(' ')
    icon_list = [x for x in response if x.startswith("src=\"https://img.icons8.com")]
    icon_list = [x.replace(DEFAULT_SIZE, target)[5:-1] for x in icon_list]

    for icon in icon_list:
        print("downloading {}".format(icon))
        name = icon.split("/")[-1]
        filename = os.path.join("data", png_path, cat, name)
        icon_file = requests.get(icon, stream=True)
        icon_file.raw.decode_content = True
        with open(filename, 'wb') as f:
            shutil.copyfileobj(icon_file.raw, f)
    count += 1

# Convert to ICO
path_list = []
for subdir, dirs, files in os.walk("data"):
    for file in files:
        filepath = subdir + os.sep + file
        if filepath.endswith(".png"):
            path_list.append(filepath)

filename = ["" + x.split("\\")[-1].split(".")[0] + ".ico" for x in path_list]
category = [x.split("\\")[-2] for x in path_list]
icons = zip(category, filename, path_list)

for category, icon, path in icons:
    img = imageio.imread(path)
    save_path = os.path.join("data", ico_path, category, icon)
    print("saving {}".format(save_path))
    imageio.imwrite(save_path, img)
