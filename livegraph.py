import matplotlib.pyplot as plt

def single_plot(dt, step, ts, K1s, K2s, Kts, fig, ax1):

    ax1.plot(ts, K1s, color='r', label='K1')
    ax1.plot(ts, K2s, color='g', label='K2')
    ax1.plot(ts, Kts, color='b', label='Kt')
    if step == 0:
        lg = ax1.legend()

    ax1.set_xlim(max(0, dt * step - 3), max(3, dt * step))
    fig.show()
    plt.pause(0.001)

def plot(dt, step, ts, K1s, K2s, Kts, fig, ax1, ax2, ax3):
    ax1.plot(ts, K1s, color='r', label='K1')
    ax2.plot(ts, K2s, color='g', label='K2')
    ax3.plot(ts, Kts, color='b', label='Kt')

    ax1.set_xlim(max(0, dt * step - 3), max(3, dt * step))
    ax2.set_xlim(max(0, dt * step - 3), max(3, dt * step))
    ax3.set_xlim(max(0, dt * step - 3), max(3, dt * step))
    fig.show()
    plt.pause(0.001)