import numpy as np
import matplotlib.pyplot as plt
font = "sans-serif"

mu2 = 1
lam = 2

r = np.arange(-1,1,.02)

mu_pos = np.add(mu2*np.power(r,2), lam*np.power(r,4))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(r,mu_pos,'k',color="blue",linewidth=4, zorder=5)
ax.set_ylim([-0.2,1])
ax.grid(False)
ax.set_title('')

# using 'spines', new in Matplotlib 1.0
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
#ax.spines['left'].set_smart_bounds(True)
#ax.spines['bottom'].set_smart_bounds(True)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axhline(linewidth=2,color="black")
ax.axvline(linewidth=2,color="black")
plt.text(0.05, 0.8, r"V($\phi$)", ha="left", family=font, size=25)
plt.text(0.8, -0.1, r"$\phi$", ha="left", family=font, size=25)

ax.set_yticklabels([])
ax.set_xticklabels([])

if mu2 < 0 :
    ax.plot([0.5,0.5],[-0.2,0.19], "k--")
    ax.plot([-0.5,-0.5],[-0.2,0.19], "k--")
    ax.text(0.47, 0.22, r"$v$", ha="left", family=font, size = 15)
    ax.text(-0.56, 0.22, r"$-v$", ha="left", family=font, size = 15)
plt.savefig("higgs_potential.svg")

plt.show()
