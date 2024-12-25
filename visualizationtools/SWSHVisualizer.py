import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from waveformtools.transforms import Yslm_vec
from waveformtools.grids import UniformGrid
from tqdm import tqdm

class SWSHvis_usph:
    def __init__(self, ell, emm, spin_weight=-2):
        """
        Base class for visualizing spin-weighted spherical harmonics on a uniform spherical grid.

        Parameters:
        - ell: Spherical harmonic degree (l).
        - emm: Spherical harmonic order (m).
        - spin_weight: Spin weight of the spherical harmonics (default: -2).
        - grid_resolution: Tuple defines the grid resolution for theta and phi.
        """
        self.ell = ell
        self.emm = emm
        self.spin_weight = spin_weight

        # Create a uniform grid for theta and phi
        self.ginfo = UniformGrid()

        # Initialize grid for theta and phi
        self.theta, self.phi = self._initialize_grid()

        # Attributes to store computed values
        self.Y_slm = None  # Spherical harmonics
        self.Y_slm_U = None  # Magnitude of spherical harmonics
        self.x = None  # Cartesian x-coordinates
        self.y = None  # Cartesian y-coordinates
        self.z = None  # Cartesian z-coordinates

    def _initialize_grid(self):
        """
        Initialize and update the theta and phi meshgrid to include 2π for better visualization.
        
        Returns:
        - theta_new: 2D numpy array of theta values.
        - phi_new: 2D numpy array of phi values.
        """
        theta, phi = self.ginfo.meshgrid

        # Extend phi to include the endpoint 2π
        phi_new = np.linspace(0, 2 * np.pi, phi.shape[1] + 1, endpoint=True)
        theta_new, phi_new = np.meshgrid(theta[:, 0], phi_new, indexing='ij')

        # Ensure theta and phi have the same shape
        if theta_new.shape != phi_new.shape:
            raise ValueError("Theta and Phi must have the same shape.")

        return theta_new, phi_new

    def compute_spherical_harmonics(self):
        """
        Compute spin-weighted spherical harmonics and corresponding Cartesian coordinates.
        """
        with tqdm(total=100, desc="Computing Spherical Harmonics", unit="%") as pbar:
            # Compute real part of spin-weighted spherical harmonics
            self.Y_slm = Yslm_vec(self.spin_weight, self.ell, self.emm, self.theta, self.phi).real
            self.Y_slm_U = np.abs(self.Y_slm)  # Magnitude of spherical harmonics
            pbar.update(50)

            # Convert spherical coordinates to Cartesian
            self.x = np.sin(self.theta) * np.cos(self.phi)
            self.y = np.sin(self.theta) * np.sin(self.phi)
            self.z = np.cos(self.theta)
            pbar.update(50)

    def plot(self, save_fig=False, file_path=None):
        """
        Plot the spin-weighted spherical harmonics on a 3D surface.

        Parameters:
        - save_fig: Boolean, whether to save the figure.
        - file_path: Path to save the figure if save_fig is True.
        """
        # Ensure harmonics are computed before plotting
        if self.Y_slm is None or self.x is None or self.y is None or self.z is None:
            self.compute_spherical_harmonics()

        with tqdm(total=100, desc="Generating Plot", unit="%") as pbar:
            fig = plt.figure(figsize=(8, 6))
            ax = plt.axes(projection='3d')

            # Create colormap for the plot
            norm = plt.Normalize(self.Y_slm_U.min(), self.Y_slm_U.max())
            cmap = plt.cm.viridis
            pbar.update(40)

            # Plot 3D surface
            surface = ax.plot_surface(
                self.x, self.y, self.z, rstride=1, cstride=1, linewidth=0,
                antialiased=False, facecolors=cmap(norm(self.Y_slm_U))
            )

            # Add colorbar for magnitude
            cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
            cbar.set_label('Real Part of Y_slm', color='white')
            cbar.ax.tick_params(colors='white')

            # Set background and aspect ratio
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
            ax.set_box_aspect([1, 1, 1])

            # Hide axes for better visualization
            ax.axis('off')

            # Add title with harmonic indices
            ax.set_title(f'l={self.ell}, m={self.emm}', color='white', size=20)
            pbar.update(40)

            # Save figure if required
            if save_fig:
                if file_path is None:
                    raise ValueError("File path must be provided if save_fig is True.")
                plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
                print('Image is saved!')

            # Display the plot
            plt.show()
            plt.close()
            pbar.update(20)

# The second class SWSHvis has similar functionality but differs in plotting.
# It is used for high-resolution computations with some changes in Cartesian coordinate scaling.


from tqdm import tqdm


class SWSHvis:
    def __init__(self, ell, emm, spin_weight=-2):
        """
        Initializes the GW_SWSHvis class, which visualizes gravitational wave 
        spin-weighted spherical harmonics.

        Parameters:
        - ell: Spherical harmonic degree (l).
        - emm: Spherical harmonic order (m).
        - spin_weight: Spin weight of the spherical harmonics (default: -2).
        """
        self.ell = ell  # Degree of spherical harmonic
        self.emm = emm  # Order of spherical harmonic
        self.spin_weight = spin_weight  # Spin weight of spherical harmonics
        
        # Create a grid of theta and phi values
        self.ginfo = UniformGrid()

        # Extract the meshgrid for theta and phi
        self.theta, self.phi = self.ginfo.meshgrid

        # Extend the phi grid to include 2π as the endpoint for a complete azimuthal rotation
        phi_new = np.linspace(0, 2 * np.pi, self.phi.shape[1] + 1, endpoint=True)
        theta_new, phi_new = np.meshgrid(self.theta[:, 0], phi_new, indexing='ij')

        # Update the theta and phi attributes with the newly generated grid
        self.theta = theta_new
        self.phi = phi_new

        # Validate that the reshaped theta and phi grids have the same dimensions
        if self.theta.shape != self.phi.shape:
            raise ValueError("Theta and Phi must have the same shape.")

        # Initialize placeholders for computed values
        self.Y_slm = None  # Spin-weighted spherical harmonics
        self.x = None  # Cartesian x-coordinates
        self.y = None  # Cartesian y-coordinates
        self.z = None  # Cartesian z-coordinates

    def compute_spherical_harmonics(self):
        """
        Computes the spin-weighted spherical harmonics and Cartesian coordinates.
        """
        with tqdm(total=100, desc="Computing Spherical Harmonics", unit="%") as pbar:

            # Compute the spin-weighted spherical harmonics
            self.Y_slm = Yslm_vec(self.spin_weight, self.ell, self.emm, self.theta, self.phi)
    
            # Compute the sine and cosine of theta and phi for Cartesian coordinate calculation
            St = np.sin(self.theta)  # Sine of theta
            Ct = np.cos(self.theta)  # Cosine of theta
            Sp = np.sin(self.phi)    # Sine of phi
            Cp = np.cos(self.phi)    # Cosine of phi
    
            # Compute Cartesian coordinates
            self.x = St * Cp  # x-coordinate
            self.y = St * Sp  # y-coordinate
            self.z = Ct       # z-coordinate
    
            # Compute the magnitude of the spherical harmonics
            self.r0 = np.abs(self.Y_slm)
    
            # Scale the Cartesian coordinates by the magnitude of the spherical harmonics
            self.xr = self.r0 * self.x  # Scaled x-coordinate
            self.yr = self.r0 * self.y  # Scaled y-coordinate
            self.zr = self.r0 * self.z  # Scaled z-coordinate
            pbar.update(50)


    def plot(self, save_fig=False, file_path=None):
        """
        Plots the spin-weighted spherical harmonics as a 3D surface.

        Parameters:
        - save_fig: Boolean, whether to save the figure.
        - file_path: Path to save the figure if save_fig is True.

        Raises:
        - ValueError: If file_path is not provided when save_fig is True.
        """
        # Compute spherical harmonics if not already computed
        if self.Y_slm is None:
            self.compute_spherical_harmonics()
            
        with tqdm(total=100, desc="Generating Plot", unit="%") as pbar:

            # Create a 3D plot
            fig = plt.figure(figsize=(8, 6))
            ax = plt.axes(projection='3d')
    
            # Compute the color dimension based on the real part of the spherical harmonics
            U = np.abs(self.Y_slm.real)
    
            # Create a colormap for the surface
            norm = plt.Normalize(U.min(), U.max())
            cmap = plt.cm.viridis
            pbar.update(40)
            
            # Ensure that the coordinate arrays are 2D for plotting
            if self.x.ndim != 2 or self.y.ndim != 2 or self.z.ndim != 2:
                raise ValueError("The x, y, and z must be 2-dimensional arrays.")
    
            # Plot the 3D surface with the computed spherical harmonics
            surface = ax.plot_surface(
                self.xr, self.yr, self.zr, rstride=1, cstride=1, linewidth=0, 
                antialiased=False, facecolors=cmap(norm(U))
            )
    
            # Add a colorbar for the plot
            cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
            cbar.set_label('Real Part of Y_slm', color='white')  # Label for the colorbar
            cbar.ax.tick_params(colors='white')  # Set tick colors to white
    
            # Set the background color to dark
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
    
            # Adjust the aspect ratio of the plot
            ax.set_box_aspect([1, 1, 1])
    
            # Hide axis lines for a clean appearance
            ax.axis('off')
    
            # Set the title with spherical harmonic parameters
            ax.set_title(f'l={self.ell}, m={self.emm}', color='white', size=20)
            pbar.update(40)
            
            # Save the figure if required
            if save_fig:
                if file_path is None:
                    raise ValueError("File path must be provided if save_fig is True.")
                plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
                print('Image is saved!')
            pbar.update(20)
            
            # Show the plot
            plt.show()
            plt.close()

# The third class SWSHvisr has similar functionality but differs in plotting and slightly in resolution.
# It is used for high-resolution computations with radial changes in Cartesian coordinate scaling.

class SWSHvisr:
    def __init__(self, ell, emm, spin_weight=-2):
        """
        A unified class for visualizing spin-weighted spherical harmonics.

        Parameters:
        - ell: Spherical harmonic degree (l).
        - emm: Spherical harmonic order (m).
        - spin_weight: Spin weight of the spherical harmonics (default: -2).
        - high_res: Boolean, whether to use high-resolution Cartesian scaling.
        """
        self.ell = ell
        self.emm = emm
        self.spin_weight = spin_weight

        # Create a uniform grid for theta and phi
        self.ginfo = UniformGrid(80,80)

        # Initialize grid for theta and phi
        self.theta, self.phi = self._initialize_grid()

        # Attributes to store computed values
        self.Y_slm = None  # Spherical harmonics
        self.r_magnitude = None  # Magnitude for scaling
        self.x = None  # Cartesian x-coordinates
        self.y = None  # Cartesian y-coordinates
        self.z = None  # Cartesian z-coordinates

    def _initialize_grid(self):
        """
        Initialize and update the theta and phi meshgrid to include 2π for better visualization.
        Returns:
        - theta_new: 2D numpy array of theta values.
        - phi_new: 2D numpy array of phi values.
        """
        theta, phi = self.ginfo.meshgrid
        phi_new = np.linspace(0, 2 * np.pi, phi.shape[1] + 1, endpoint=True)
        theta_new, phi_new = np.meshgrid(theta[:, 0], phi_new, indexing='ij')
        return theta_new, phi_new

    def compute_spherical_harmonics(self):
        """
        Compute spin-weighted spherical harmonics and corresponding Cartesian coordinates.
        """
        with tqdm(total=100, desc="Computing Spherical Harmonics", unit="%") as pbar:
            # Compute spherical harmonics
            self.Y_slm = Yslm_vec(self.spin_weight, self.ell, self.emm, self.theta, self.phi).real
            self.r_magnitude = np.abs(self.Y_slm)  # Magnitude of spherical harmonics
            pbar.update(50)

            # Compute Cartesian coordinates
            sin_theta = np.sin(self.theta)
            cos_theta = np.cos(self.theta)
            sin_phi = np.sin(self.phi)
            cos_phi = np.cos(self.phi)

            self.x = sin_theta * cos_phi
            self.y = sin_theta * sin_phi
            self.z = cos_theta

            # Scale Cartesian coordinates for high-resolution visualization
            self.x *= self.Y_slm
            self.y *= self.Y_slm
            self.z *= self.Y_slm

            pbar.update(50)

    def plot(self, save_fig=False, file_path=None):
        """
        Plot the spin-weighted spherical harmonics on a 3D surface.

        Parameters:
        - save_fig: Boolean, whether to save the figure.
        - file_path: Path to save the figure if save_fig is True.
        """
        # Ensure harmonics are computed before plotting
        if self.Y_slm is None:
            self.compute_spherical_harmonics()

        with tqdm(total=100, desc="Generating Plot", unit="%") as pbar:
            fig = plt.figure(figsize=(8, 6))
            ax = plt.axes(projection='3d')

            # Create colormap for the plot
            norm = plt.Normalize(self.r_magnitude.min(), self.r_magnitude.max())
            cmap = plt.cm.viridis
            pbar.update(40)

            # Plot 3D surface
            surface = ax.plot_surface(
                self.x, self.y, self.z, rstride=1, cstride=1, linewidth=0,
                antialiased=False, facecolors=cmap(norm(self.r_magnitude))
            )

            # Add colorbar for magnitude
            cbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), ax=ax, pad=0.1)
            cbar.set_label('Real Part of Y_slm', color='white')
            cbar.ax.tick_params(colors='white')

            # Set background and aspect ratio
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')
            ax.set_box_aspect([1, 1, 1])

            # Hide axes for better visualization
            ax.axis('off')

            # Add title with harmonic indices
            ax.set_title(f'l={self.ell}, m={self.emm}', color='white', size=20)
            pbar.update(40)

            # Save figure if required
            if save_fig:
                if file_path is None:
                    raise ValueError("File path must be provided if save_fig is True.")
                plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
                print('Image is saved!')

            # Display the plot
            plt.show()
            plt.close()
            pbar.update(20)
