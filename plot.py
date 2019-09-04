import matplotlib.pylab as plt
from struct import iter_unpack

file = "ecg.log"

with open(file, "rb") as f:
	y = list(iter_unpack("h", f.read()))

plt.plot(y)
plt.show()
