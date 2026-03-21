import imageio.v3 as iio

filenames = ['pic-1.jpg', 'pic-2.jpg']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

  iio.imwrite('tani.gif', images, duration = 500, loop = 0)