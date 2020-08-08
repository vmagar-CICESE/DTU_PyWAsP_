import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def plot_bwc(bwc):
    # Plot the wind speed distributions

    fig = plt.figure(figsize=(16, 5))

    # Wind speed distributions

    ax1 = fig.add_subplot(121)

    (bwc.wsfreq
        .squeeze()
        .plot
        .line(x='wsbin', 
              ax=ax1,
              lw=2.0));

    # Wind rose

    ax2 = fig.add_subplot(122, projection='polar')
    ax2 = plt.gca(projection='polar')
    ax2.set_theta_direction(-1)
    ax2.set_theta_zero_location('N')

    theta = np.deg2rad(bwc.sector.values)
    dtheta = 2.0 * np.pi / 12.

    ax2.bar(theta, 
            bwc.wdfreq.squeeze(), 
            width=dtheta*0.9,
            color='C0');

    return fig, (ax1, ax2)

