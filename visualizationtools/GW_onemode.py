from waveformtools.transforms import Yslm_vec
from waveformtools.grids import UniformGrid
from mpl_toolkits.mplot3d import Axes3D
import h5py
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from tqdm import tqdm
import os
import imageio
import cv2


# Visualising one mode for a given time stamp of GW data in hdata format

class gw1m_vis:
    def __init__(self, hdata, ell, emm, timestamp = 1000):
        """
        Initialize the SphericalModePlotter with mode data and parameters.

        Parameters:
        - hdata: Dictionary containing spherical harmonic mode data.
        - ell: Integer, degree of the spherical harmonic.
        - emm: Integer, order of the spherical harmonic.
        - timestamp: timestamp that is to be plotted. intialized as 1000
        """
        self.hdata = hdata
        self.ell = ell
        self.emm = emm
        self.timestamp = timestamp

        # Create a uniform grid on the sphere
        ginfo = UniformGrid(80,80)
        self.theta_grid, self.phi_grid = ginfo.meshgrid

        # Extend the phi grid to cover the full 2\pi range
        phi_new = np.linspace(0, 2 * np.pi, self.phi_grid.shape[1] + 1, endpoint=True)
        self.theta_new, self.phi_new = np.meshgrid(self.theta_grid[:, 0], phi_new, indexing='ij')

        # Compute Cartesian coordinates for the spherical surface
        self.St = np.sin(self.theta_new)
        self.Ct = np.cos(self.theta_new)
        self.Sp = np.sin(self.phi_new)
        self.Cp = np.cos(self.phi_new)

        self.x = self.St * self.Cp
        self.y = self.St * self.Sp
        self.z = self.Ct

    def compute_mode_amplitudes(self, ell, emm):
        """
        Compute the mode amplitudes and spherical harmonics for a specific ell and emm.
    
        Parameters:
        - ell: Integer, degree of the spherical harmonic.
        - emm: Integer, order of the spherical harmonic.
    
        Returns:
        - U: 3D array, mode amplitude grid.
        """
        # Extract mode data for the specified ell and emm
        h_data = self.hdata[f'Y_l{ell}_m{emm}.dat'][...]
        c = h_data[:, 1] + 1j * h_data[:, 2]  # Complex mode coefficients
    
        # Generate spin-weighted spherical harmonics for the given ell and emm
        m2_Y = Yslm_vec(spin_weight=-2, ell=self.ell, emm= self.emm, 
                        theta_grid=self.theta_new, phi_grid=self.phi_new).real
    
        # Compute the 3D grid of mode amplitudes
        s = np.einsum('i,jk->ijk', c, m2_Y)
        U = s[self.timestamp].real
        return U

    def plot(self, save_fig=False, file_path=None, cmap='viridis', alpha_scale=1):
        """
        Plot the spherical surface with the given mode amplitudes.
    
        Parameters:
        - save_fig: Boolean to determine whether to save the figure.
        - file_path: Path to save the figure.
        - cmap: String, colormap to use for the surface.
        - alpha_scale: Float, scale factor for surface transparency.
        """
        
        U = self.compute_mode_amplitudes(self.ell, self.emm)
    
        # Scale Cartesian coordinates by the mode amplitudes
        xu = U * self.x
        yu = U * self.y
        zu = U * self.z
    
        # Normalize the mode amplitudes for color mapping
        color_dimension = U
        minn, maxx = color_dimension.min(), color_dimension.max()
        norm = matplotlib.colors.Normalize(minn, maxx)
    
        # Create a colormap mapper
        m = plt.cm.ScalarMappable(norm=norm, cmap=cmap)
        m.set_array([])
        fcolors = m.to_rgba(color_dimension)
    
        # Create a 3D plot
        fig = plt.figure(figsize=(10, 8))
        ax = plt.axes(projection='3d')
    
        # Set background colors to dark
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
    
        # Plot the surface
        surf = ax.plot_surface(xu, yu, zu, linewidth=0, antialiased=False, facecolors=fcolors, alpha= 1)
        surf.set_cmap(cmap)
    
        # Turn off the axis and grid for a clean look
        ax.axis('off')


        if save_fig==True: 
            plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
            print('Image is saved!')

        plt.show()


# second class: Animating one mode from hdata_path

class gw1m_anim:
    """
    A class to create an animation for a specific mode of gravitational waves.

    Attributes:
        ell (int): The gravitational wave mode's multipole moment (ell).
        emm (int): The gravitational wave mode's azimuthal quantum number (m).
        hdata_path (str): Path to the HDF5 file containing the gravitational wave data.
        output_dir (str): Directory where frames and the video will be saved.
        video_name (str): Name of the output video file.
        fps (int): Frames per second for the output video.
        step (int): Step size for iterating over time stamps.
    """

    def __init__(self, ell, emm, hdata_path, step, fps, output_dir, video_name):
        """
        Initializes the GW_onemode_animator class with the required parameters.
        """
        self.ell = ell  # Mode number for ell
        self.emm = emm  # Mode number for m
        self.hdata_path = hdata_path  # Path to HDF5 file containing GW data
        
        # Create a uniform grid for spherical coordinates
        self.ginfo = UniformGrid(80, 80)
        self.theta_grid, self.phi_grid = self.ginfo.meshgrid
        
        # Extend the phi grid to cover the full 2π range
        phi_new = np.linspace(0, 2 * np.pi, self.phi_grid.shape[1] + 1, endpoint=True)
        self.theta_new, self.phi_new = np.meshgrid(self.theta_grid[:, 0], phi_new, indexing='ij')

        # Calculate Cartesian coordinates for the spherical surface
        self.St = np.sin(self.theta_new)
        self.Ct = np.cos(self.theta_new)
        self.Sp = np.sin(self.phi_new)
        self.Cp = np.cos(self.phi_new)
        self.x = self.St * self.Cp  # x-coordinates
        self.y = self.St * self.Sp  # y-coordinates
        self.z = self.Ct  # z-coordinates

        self.output_dir = output_dir  # Directory to save frames and video
        self.video_name = video_name  # Name of the output video
        self.fps = fps  # Frames per second for the video
        self.step = step  # Step size for time stamps

        # Read hplus and hcross data from the HDF5 file
        with h5py.File(self.hdata_path, 'r') as hfile:
            h_data = hfile[f'Y_l{self.ell}_m{self.emm}.dat'][...]
        
        self.arr_hplus = np.array([a[1] for a in h_data], dtype=float)
        self.arr_hcross = np.array([a[2] for a in h_data], dtype=float)

        self.hplus_t = np.abs(self.arr_hplus[0])  # Initial hplus value
        self.c = np.array(h_data[:, 1], dtype=float) + 1j * np.array(h_data[:, 2], dtype=float)  # Complex wave data
        self.m2_Y = Yslm_vec(-2, ell, emm, self.theta_new, self.phi_new).real  # Spin-weighted spherical harmonics
        self.s = np.einsum('i,jk->ijk', self.c, self.m2_Y)  # Combine harmonics and wave data

        # Ensure the output directory exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_frames(self):
        """
        Creates individual frame images for the animation.
        """
        print('Images are being created')
        for time_stamp in tqdm(range(1000, len(self.s), self.step)):  # Iterate over time stamps
            U = self.s[time_stamp].real  # Extract the real part of the data for the current time step

            # Scale the Cartesian coordinates by the data
            xu = U * self.x
            yu = U * self.y
            zu = U * self.z

            # Plot the data on a 3D surface
            fig = plt.figure(figsize=(10, 8))
            ax = plt.axes(projection='3d')
            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')

            color_dimension = U  # Data for color mapping
            minn, maxx = color_dimension.min(), color_dimension.max()
            norm = plt.Normalize(minn, maxx)

            m = plt.cm.ScalarMappable(norm=norm, cmap='viridis')  # Color map
            m.set_array([])
            fcolors = m.to_rgba(color_dimension)  # Map colors to the data

            ax.set_title(f'l={self.ell},m={self.emm}', color='white', size=10)
            surf = ax.plot_surface(xu, yu, zu, linewidth=0, antialiased=False, facecolors=fcolors)
            surf.set_cmap('viridis_r')
            ax.axis('off')

            # Save the frame as an image
            plt.savefig(f'{self.output_dir}/s{self.ell}{self.emm}_{time_stamp:05d}.jpg')
            plt.close(fig)

        print('Images are saved in the output directory')

    def images_to_video(self):
        """
        Converts the generated frame images into a video.
        """
        images = [img for img in os.listdir(self.output_dir) if img.endswith(".jpg")]
        images = np.sort(images)  # Sort images by filename
        frame = cv2.imread(os.path.join(self.output_dir, images[0]))  # Read the first frame
        height, width, layers = frame.shape

        # Initialize the video writer
        video = cv2.VideoWriter(self.video_name, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (width, height))
        for image in images:
            video.write(cv2.imread(os.path.join(self.output_dir, image)))  # Write each frame to the video

        cv2.destroyAllWindows()
        video.release()  # Release the video writer

    def run(self):
        """
        Executes the animation pipeline: create frames and convert to video.
        """
        self.create_frames()
        print('Images are being converted to video')
        self.images_to_video()
        print('Your Video is ready')

