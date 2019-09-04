import matplotlib.pylab as plt
from struct import iter_unpack

y = []
file = "ecg.log"

with open(file, "rb") as f:
	bytes = f.read()
	for value in iter_unpack("h", bytes):
		y.append(value)

plt.plot(y)
plt.show()
