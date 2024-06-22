import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm

class SphericalHarmonicsVisualizer_radial:
    def __init__(self, ell, emm):
        self.ell = ell
        self.emm = emm
        self.theta, self.phi = np.meshgrid(np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 200))
        self.Y_lm = None
        self.x = None
        self.y = None
        self.z = None
        self.xr = None
        self.yr = None
        self.zr = None

    def compute_spherical_harmonics(self):
        self.Y_lm = sph_harm(self.emm, self.ell, self.phi, self.theta).real
        self.x = np.sin(self.theta) * np.cos(self.phi)
        self.y = np.sin(self.theta) * np.sin(self.phi)
        self.z = np.cos(self.theta)
        self.xr = self.Y_lm * self.x
        self.yr = self.Y_lm * self.y
        self.zr = self.Y_lm * self.z

    def plot_spherical_harmonics(self, save_fig=False, file_path=None):
        if self.Y_lm is None:
            self.compute_spherical_harmonics()

        fig = plt.figure(figsize=(10, 8))
        ax = plt.axes(projection='3d')

        # Calculate color dimension
        U = self.Y_lm.real

        # Create colormap
        norm = plt.Normalize(U.min(), U.max())
        cmap = plt.cm.viridis

        # Plot the surface
        surface = ax.plot_surface(self.xr, self.yr, self.zr, rstride=1, cstride=1, linewidth=0, antialiased=False, facecolors=cmap(norm(U)))

        # Set background color to dark
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        
        # Adding a colorbar
        cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
        cbar.set_label('Real Part of Y_s', color='white')
        cbar.ax.tick_params(colors='white')

        # Set axis labels and tick labels color
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.zaxis.label.set_color('white')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='z', colors='white')
        
        # Set aspect ratio
        ax.set_box_aspect([1, 1, 1])

        ax.set_title(f'l={ell},m={emm}', color='white', size=20)

        ax.axis('off')

        if save_fig==True: 
            plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
            print('Image is saved!')
        plt.show()
        plt.close()
