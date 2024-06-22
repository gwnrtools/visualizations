import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
import matplotlib

class SphericalHarmonicsVisualizer:
    def __init__(self, ell, emm):
        self.ell = ell
        self.emm = emm
        self.theta, self.phi = np.meshgrid(np.linspace(0, np.pi, 100), np.linspace(0, 2 * np.pi, 200))
        self.Y_lm = None
        self.x = None
        self.y = None
        self.z = None

    def compute_spherical_harmonics(self):
        self.Y_lm = sph_harm(self.emm, self.ell, self.phi, self.theta)
        self.x = np.sin(self.theta) * np.cos(self.phi)
        self.y = np.sin(self.theta) * np.sin(self.phi)
        self.z = np.cos(self.theta)

    def plot_spherical_harmonics(self, save_fig=False, file_path=None):
        if self.Y_lm is None:
            self.compute_spherical_harmonics()

        r0 = np.abs(self.Y_lm)
        R_y = np.real(self.Y_lm)

        xr = r0 * self.x
        yr = r0 * self.y
        zr = r0 * self.z

        # Assign color dimension
        color_dimension = R_y
        minn, maxx = color_dimension.min(), color_dimension.max()
        norm = matplotlib.colors.Normalize(minn, maxx)

        m = plt.cm.ScalarMappable(norm=norm, cmap='viridis')
        m.set_array([])

        fcolors = m.to_rgba(color_dimension)

        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        # Set background color to dark
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')

        # Plot surface
        surf = ax.plot_surface(xr, yr, zr, linewidth=0, antialiased=False, facecolors=fcolors)

        # Create colorbar
        cbar = fig.colorbar(surf, ax=ax, pad=0.1)
        cbar.set_label('Real Part of Y_s', color='white')
        cbar.ax.tick_params(colors='white')

        # Set colormap
        surf.set_cmap('viridis_r')

        # Set axis labels and tick labels color
        ax.xaxis.label.set_color('white')
        ax.yaxis.label.set_color('white')
        ax.zaxis.label.set_color('white')

        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.tick_params(axis='z', colors='white')

        ax.set_title(f'l={ell},m={emm}', color='white', size=20)

        # Turn off axis and grid
        ax.axis('off')
        if save_fig==True: 
            plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
            print('Image is saved!')
        plt.show()
        plt.close()
