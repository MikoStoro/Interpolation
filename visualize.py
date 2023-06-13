from matplotlib import pyplot as plt

def visualize(base, start = 0, end = 100, step = 0.1):
    length = end - start
    steps = int(length // step)
    currx = start
    xarr = []
    yarr = []
    for i in range(steps):
        y = base.val(currx)
        if y is not None:
            xarr.append(currx)
            yarr.append(y)
        currx += step
    plt.figure()
    plt.plot(xarr,yarr)
    plt.show()

