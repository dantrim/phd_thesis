"""Demo: practical use of numpy (mexhat-numpy.py)"""

import time
import math
import numpy as np

N = 10000


def mexhat_py(t, sigma=1):
    """Computes Mexican hat shape, see
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet for
    equation (13 Dec 2011)"""
    c = 2. / math.sqrt(3 * sigma) * math.pi ** 0.25
    return c * (1 - t ** 2 / sigma ** 2) * \
        math.exp(-t ** 2 / (2 * sigma ** 2))


def mexhat_np(t, sigma=1):
    """Computes Mexican hat shape using numpy, see
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet for
    equation (13 Dec 2011)"""
    c = 2. / math.sqrt(3 * sigma) * math.pi ** 0.25
    return c * (1 - t ** 2 / sigma ** 2) * \
        np.exp(-t ** 2 / (2 * sigma ** 2))


def test_is_really_the_same():
    """Checking whether mexhat_np and mexhat_py produce
    the same results."""
    xs1, ys1 = loop1()
    xs2, ys2 = loop2()
    deviation = math.sqrt(sum((ys1 - ys2) ** 2))
    print("error:", deviation)
    assert deviation < 4e-15


def loop1():
    """Compute arrays xs and ys with mexican hat function
    in ys(xs), returns tuple (xs,ys)"""
    xs = np.linspace(-5, 5, N)
    ys = []
    for x in xs:
        ys.append(mexhat_py(x))
    return xs, ys


def loop2():
    """As loop1, but uses numpy to be faster."""
    xs = np.linspace(-5, 5, N)
    return xs, mexhat_np(xs)


def time_this(f):
    """Call f, measure and return number of seconds
    execution of f() takes"""
    starttime = time.time()
    f()
    stoptime = time.time()
    return stoptime - starttime


def make_plot(filenameroot):
    import pylab
    pylab.figure(figsize=(6, 4))
    xs, ys = loop2()
    pylab.plot(xs, ys, label='Mexican hat function')
    pylab.legend()
    pylab.savefig(filenameroot + '.png')
    pylab.savefig(filenameroot + '.pdf')


def main():
    test_is_really_the_same()
    # make_plot('mexhat1d')
    time1 = time_this(loop1)
    time2 = time_this(loop2)
    print("Numpy version is %.1f times faster" %
          (time1 / time2))

if __name__ == "__main__":
    main()

"""Demo: practical use of numpy (mexhat-numpy.py)"""

import time
import math
import numpy as np

N = 10000


def mexhat_py(t, sigma=1):
    """Computes Mexican hat shape, see
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet for
    equation (13 Dec 2011)"""
    c = 2. / math.sqrt(3 * sigma) * math.pi ** 0.25
    return c * (1 - t ** 2 / sigma ** 2) * \
        math.exp(-t ** 2 / (2 * sigma ** 2))


def mexhat_np(t, sigma=1):
    """Computes Mexican hat shape using numpy, see
    http://en.wikipedia.org/wiki/Mexican_hat_wavelet for
    equation (13 Dec 2011)"""
    c = 2. / math.sqrt(3 * sigma) * math.pi ** 0.25
    return c * (1 - t ** 2 / sigma ** 2) * \
        np.exp(-t ** 2 / (2 * sigma ** 2))


def test_is_really_the_same():
    """Checking whether mexhat_np and mexhat_py produce
    the same results."""
    xs1, ys1 = loop1()
    xs2, ys2 = loop2()
    deviation = math.sqrt(sum((ys1 - ys2) ** 2))
    print("error:", deviation)
    assert deviation < 4e-15


def loop1():
    """Compute arrays xs and ys with mexican hat function
    in ys(xs), returns tuple (xs,ys)"""
    xs = np.linspace(-5, 5, N)
    ys = []
    for x in xs:
        ys.append(mexhat_py(x))
    return xs, ys


def loop2():
    """As loop1, but uses numpy to be faster."""
    xs = np.linspace(-5, 5, N)
    return xs, mexhat_np(xs)


def time_this(f):
    """Call f, measure and return number of seconds
    execution of f() takes"""
    starttime = time.time()
    f()
    stoptime = time.time()
    return stoptime - starttime


def make_plot(filenameroot):
    import pylab
    pylab.figure(figsize=(6, 4))
    xs, ys = loop2()
    pylab.plot(xs, ys, label='Mexican hat function')
    pylab.legend()
    pylab.savefig(filenameroot + '.png')
    pylab.savefig(filenameroot + '.pdf')


def main():
    #test_is_really_the_same()
    make_plot('mexhat1d')
    time1 = time_this(loop1)
    time2 = time_this(loop2)
    print("Numpy version is %.1f times faster" %
          (time1 / time2))

if __name__ == "__main__":
    main()


