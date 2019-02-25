import numpy as np
import h5py
import matplotlib.pyplot as plt

# plt.rcParams['figure.figsize'] = (5.0, 4.0)
# plt.rcParams['image.interpolation'] = 'nearest'
# plt.rcParams['image.cmap'] = 'gray'


def zero_pad(X, pad):
    X_padded = np.pad(X, ((0, 0), (pad, pad), (pad, pad), (0, 0)),
                      'constant', constant_values=0)
    return X_padded

np.random.seed(1)
x = np.random.randn(4, 3, 3, 2)
x_paded = zero_pad(x, 2)

print ("x.shape =", x.shape)
print ("x_paded.shape =", x_paded.shape)
print ("x[1, 1] =", x[1, 1])
print ("x_paded[1, 1] =", x_paded[1, 1])


fig , axarr = plt.subplots(1, 2)
axarr[0].set_title('x')
axarr[0].imshow(x[0, :, :, 0])
axarr[1].set_title('x_paded')
axarr[1].imshow(x_paded[0, :, :, 0])
