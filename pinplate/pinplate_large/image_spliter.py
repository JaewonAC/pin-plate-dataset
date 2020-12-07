from pathlib import Path
from PIL import Image

spts_file = open('split_points.txt')

count = 0

for img_filename in Path('.').glob('*.jpg'):
    print(img_filename)
    img = Image.open(img_filename)
    hpts, vpts = spts_file.readline()[:-1].split('/')
    hpts = ('0,' + hpts + ',' + str(img.height)).split(',')
    vpts = ('0,' + vpts + ',' + str(img.width)).split(',')
    print(hpts)
    print(vpts)

    for i in range(len(hpts)-1):
        for j in range(len(vpts)-1):
            print([int(vpts[j]), int(hpts[i]), int(vpts[j+1]), int(hpts[i+1])])
            subimg = img.crop([int(vpts[j]), int(hpts[i]), int(vpts[j+1]), int(hpts[i+1])])

            subimg.save('cut/' + str(count).zfill(4) + '.jpg')
            count += 1

