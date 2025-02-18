from FDDB import FDDB
dd = FDDB()
dd.runFDDB(pred='./result/FDDB_dets.txt', result_path='./result/', index=-1)

from matplotlib import pyplot as plt
import numpy as np

path_ContROC = "./result/ContROC.txt"
path_DiscROC = "./result/DiscROC.txt"
path_imgSave = "./result/result.png"

set_x_lim = 1000

# get data
with open(path_DiscROC, 'r') as fp:
    discROC = fp.readlines()

# get disc data x, y
discROC = [line.split() for line in discROC]
disc_x = [float(x[1]) for x in discROC]
disc_y = [float(y[0]) for y in discROC]

# get data we need to be print
count = len(discROC)

### plot data
plt.figure()

# set y limite
plt.ylim((-0.07,1))
# plt.xlim((-2,set_x_lim))
# print label
plt.xlabel('False Positive (FP)')
plt.ylabel('True Positive Rate (TPR)')

# plot data
plt.plot(disc_x,disc_y,color = '#007777', linewidth = 3.0)

# print data text
plt.title('Pytorch RetinaFace mobile0.25')
plt.text(disc_x[0] - disc_x[0] / 3,disc_y[0] + 0.03,'Discrete Score: %.3f' %(disc_y[0] * 100) + '%')

# 
plt.grid()

# save img
# plt.figure(figsize=(10, 10))
plt.savefig(path_imgSave)
plt.show()

