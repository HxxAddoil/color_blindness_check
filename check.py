import random
import os
import matplotlib.pyplot as plt
from PIL import Image

answer = {1: '98',     14: '☆',           23: '壶',          38: '899022',     52: '99',
          2: '291',    15: '△与○',       24: '眼镜',        39: '621989',     53: '60',
          3: '628',    16: '☆',           25: '○与剪刀',    40: '812',        54: '266',
          4: '88',     17: '○与○',       26: '杯',          41: '908',        55: '928',
          5: '69',     18: '○',           27: '鱼',          42: '6098',       56: '68',
          6: '60',     19: '○与▽',       28: '鹅',          43: '8609',       57: '26',
          7: '98',     20: '△与○与▽',   29: '燕',          44: '698',        58: '16',
          8: '816',    21: '□与▽',       30: '蝴蝶',        45: '6289',       59: '○',
          9: '9',      22: '○与☆',       31: '蜻蜓',        46: '2901',       60: '○与□',
          10: '286',                       32: '鸽',          47: '899',        61: '○与△',
          11: '62',                        33: '牛',          48: '602',        62: '□与○',
          12: '2与9',                      34: '狗',          49: '820',        63: '△与○',
          13: '6与0',                      35: '羊',          50: '2619',       64: '△与□',
                                           36: '伞',          51: '606',        65: '○与○',
                                           37: '熊猫'
          }

img_root = r'./imgs'
l = list(range(1, 66, 1))
l_random = random.sample(l, len(l))
# l_random = random.sample([8, 30, 11, 3, 49, 40, 45, 26, 42], 9)

for i in l_random:
    img_path = os.path.join(img_root, str(i) + '.jpg')
    img = Image.open(img_path)
    plt.figure(figsize=(12, 8))
    plt.imshow(img)
    print('图{}的真实答案是：{}'.format(i, answer[i]))
    plt.show()



# rename

# dir = r'G:\hxxfile\jiakapo\img'
# l = os.listdir(dir)
# for i in l:
#     src = os.path.join(dir, i)
#     name = int(i[-6:-4]) - 31
#     dst = os.path.join(dir, str(name)+'.jpg')
#     os.rename(src, dst)

# rotate

# dir = r'G:\hxxfile\jiakapo\img'
# l = os.listdir(dir)
# for i in l:
#     src = os.path.join(dir, i)
#     im = Image.open(src)
#     im_rotate = im.transpose(Image.ROTATE_270)
#     im_rotate.save(src)

