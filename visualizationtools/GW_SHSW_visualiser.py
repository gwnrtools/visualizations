import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from waveformtools.transforms import Yslm_vec
from waveformtools.grids import UniformGrid

class GW_SpinWeightedSphericalHarmonicsVisualizer:
    def __init__(self, ell, emm, spin_weight=-2):
        self.ell = ell
        self.emm = emm
        self.spin_weight = spin_weight
        self.ginfo = UniformGrid(600,600)

        # Extract the theta and phi meshgrid
        self.theta, self.phi = self.ginfo.meshgrid
        
        # Ensure that theta and phi are properly reshaped
        if self.theta.shape != self.phi.shape:
            raise ValueError("Theta and Phi must have the same shape.")
        
        self.Y_slm = None
        self.x = None
        self.y = None
        self.z = None
        self.xr = None
        self.yr = None
        self.zr = None

    def compute_spherical_harmonics(self):
        # Compute the real part of spin-weighted spherical harmonics
        self.Y_slm = Yslm_vec(self.spin_weight, self.ell, self.emm, self.theta, self.phi).real
        
        # Convert spherical to Cartesian coordinates
        self.x = np.sin(self.theta) * np.cos(self.phi)
        self.y = np.sin(self.theta) * np.sin(self.phi)
        self.z = np.cos(self.theta)

        # Multiply the coordinates by the spherical harmonics
        self.xr = self.Y_slm * self.x
        self.yr = self.Y_slm * self.y
        self.zr = self.Y_slm * self.z

    def plot_spherical_harmonics(self, save_fig=False, file_path=None):
        if self.Y_slm is None:
            self.compute_spherical_harmonics()

        fig = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection='3d')

        # Calculate color dimension
        U = self.Y_slm

        # Create colormap
        norm = plt.Normalize(U.min(), U.max())
        cmap = plt.cm.viridis

        # Ensure the arrays are 2D for surface plotting
        if self.xr.ndim != 2 or self.yr.ndim != 2 or self.zr.ndim != 2:
            raise ValueError("The xr, yr, and zr must be 2-dimensional arrays.")

        # Plot the surface
        surface = ax.plot_surface(self.xr, self.yr, self.zr, rstride=1, cstride=1, linewidth=0,antialiased=False, facecolors=cmap(norm(U)))

        # Adding a colorbar
        cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
        cbar.set_label('Real Part of Y_slm', color='white')
        cbar.ax.tick_params(colors='white')

        # Set background color to dark
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        
        # Set aspect ratio
        ax.set_box_aspect([1, 1, 1])

        ax.axis('off')

        ax.set_title(f'l={self.ell}, m={self.emm}', color='white', size=20)

        if save_fig:
            plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
            print('Image is saved!')
        
        plt.show()
        plt.close()
