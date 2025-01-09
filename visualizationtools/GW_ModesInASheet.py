from waveformtools.transforms import Yslm_vec
from waveformtools.grids import UniformGrid
from mpl_toolkits.mplot3d import Axes3D
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np
from tqdm import tqdm
import matplotlib
import os
import imageio
import cv2


class Vis_M1S:
    """
    This class visualizes gravitational wave modes and produces them in a single sheet for a given ell range.
    It utilizes Numerical Relativity (NR) data to generate spherical harmonic projections of gravitational waveforms.
    """
    def __init__(self, ell_range, hdata_path, save_fig= False, file_path =None, trnsp=False, fig_size=(56, 56), timestamp = 1000):
        """
        Initializes the ModesInASheet class.

        Parameters:
        - ell_range: List of integers representing the range of \( \ell \) values to plot.
        - hdata_path: Path to the HDF5 file containing spherical harmonic data. The dictionary should contain mode data with keys like 'Y_l{ell}_m{emm}.dat'.
        - save_fig: Boolean to determine whether to save the figure.
        - file_path: Path to save the figure.
        - trnsp: Boolean to determine transparency settings.
        - fig_size: Tuple representing the figure size for the plots.
        - timestamp: timestamp that is to be plotted. intialized as 1000
        """
        self.ell_range = ell_range
        self.hdata = h5py.File(hdata_path, 'r')
        self.ginfo = UniformGrid()  # Initialize a uniform grid with 300x300 points
        self.trnsp = trnsp  # Store transparency flag
        self.theta_grid, self.phi_grid = self.ginfo.meshgrid
        self.spin_weight = -2
        # Initialize updated theta and phi grids for visualization
        self.theta_new, self.phi_new = self._initialize_grid()
        self.timestamp = timestamp

        # Compute 3D Cartesian coordinates for the meshgrid
        self.x = np.sin(self.theta_new) * np.cos(self.phi_new)
        self.y = np.sin(self.theta_new) * np.sin(self.phi_new)
        self.z = np.cos(self.theta_new)
        
        self.fig_size = fig_size
        self.save_fig = save_fig
        self.file_path = file_path

    def _initialize_grid(self):
        """
        Initialize and update the theta and phi meshgrid to include \( 2\pi \) for better visualization.

        Returns:
        - theta_new: 2D numpy array of updated theta values.
        - phi_new: 2D numpy array of updated phi values.
        """
        theta, phi = self.ginfo.meshgrid
        phi_new = np.linspace(0, 2 * np.pi, phi.shape[1] + 1, endpoint=True)  # Extend phi to 2\pi
        theta_new, phi_new = np.meshgrid(theta[:, 0], phi_new, indexing='ij')
        return theta_new, phi_new

    def calculate_alpha(self, ell, trnsp):
        """
        Calculate the alpha (transparency) value based on `ell` and `trnsp`.

        Parameters:
        - ell: Integer \( \ell \) value for the mode.
        - trnsp: Boolean to determine transparency settings.

        Returns:
        - alpha: Float transparency value.
        """
        if not trnsp:
            if ell == 2:
                return 1
            elif ell == 3:
                return 0.25
            elif ell == 4:
                return 0.125
            else:
                return 0.03
                
        else:
            return 1

    def subplot_shape(self):
        # Calculate the total number of subplots needed
        t = []
        for i in range(len(self.ell_range)):
            l = 2 * self.ell_range[i]
            #print (l)
            l_1 = l +1
            #print(l_1)
            t.append(l_1)
        #print(t)
        tot = sum(t)
        
        # Calculate the number of rows and columns for subplots
        num_cols = 3
        num_rows = (tot + num_cols - 1) // num_cols  # This ensures num_rows is ceil(tot / num_cols)

        #print(num_cols, num_rows)
        
        return (num_rows, num_cols)

    def plot_modes(self):
        """
        Plot modes of spherical harmonics.
        """
        
        fig = plt.figure(figsize=self.fig_size)
        sum_plots = 0

        for ell in self.ell_range:
            emm_range = np.arange(-ell, ell + 1)
            for emm in tqdm(emm_range, desc=f'Processing ell={ell}'):
                h_data = self.hdata[f'Y_l{ell}_m{emm}.dat'][...]
                arr_hplus = [a[1] for a in h_data]
                c = h_data[:, 1] + 1j * h_data[:, 2]
                m2_Y = Yslm_vec(ell=ell, emm=emm, spin_weight=-2, theta_grid=self.theta_new, phi_grid=self.phi_new).real
                s = np.einsum('i,jk->ijk', c, m2_Y)
                U = s[self.timestamp].real
                xu = U * self.x
                yu = U * self.y
                zu = U * self.z
                ax = fig.add_subplot(self.subplot_shape()[0], self.subplot_shape()[1], sum_plots + 1, projection='3d')
                fig.patch.set_facecolor('black')
                ax.set_facecolor('black')
                color_dimension = U
                minn, maxx = color_dimension.min(), color_dimension.max()
                norm = plt.Normalize(minn, maxx)
                alpha = self.calculate_alpha(ell, self.trnsp)
                m = plt.cm.ScalarMappable(norm=norm, cmap='viridis')
                m.set_array([])
                fcolors = m.to_rgba(color_dimension, alpha=alpha)
                surf = ax.plot_surface(xu, yu, zu, linewidth=0, antialiased=False, facecolors=fcolors)
                ax.set_title(f'l={ell}, m={emm}', color='white', fontsize=20)
                surf.set_cmap('viridis_r')
                ax.axis('off')
                sum_plots += 1

        plt.tight_layout()
        
        if self.save_fig==True: 
            plt.savefig(self.file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
            print('Image is saved!')
            
        plt.show()








# Class 2: Animator


class Anim_M1S:
    """
    This class visualizes gravitational wave modes by creating animations and saving them as a video.
    It utilizes Numerical Relativity (NR) data to generate spherical harmonic projections of gravitational waveforms.
    """

    def __init__(self, ell_range, hdata_path, time_stamp, fps, start_time= None, last_time=None, fig_size=(56, 56), output_dir='output', video_name='output_video.mp4'):
        """
        Initializes the Animator_ModesInASheet object.
        
        Parameters:
        - ell_range (list): Range of `ell` values to include in the visualization.
        - hdata_path (str): Path to the HDF5 file containing the waveform data.
        - time_stamp (int): Time intervals between frames.
        - fps (int): Frames per second for the output video.
        - start_time (int, optional): Start time for plotting. Defaults to None.
        - last_time (int, optional): Last time for plotting. Defaults to None.
        - fig_size (tuple, optional): Figure size for the plots. Defaults to (56, 56).
        - output_dir (str, optional): Directory to save the output images. Defaults to 'output'.
        - video_name (str, optional): Name of the output video file. Defaults to 'output_video.mp4'.
        """
        self.ell_range = ell_range
        self.hdata_path = hdata_path
        self.hdata = h5py.File(hdata_path, 'r')
        # Create a uniform grid on the sphere
        ginfo = UniformGrid()
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

        self.fig_size = fig_size
        self.output_dir = output_dir
        self.fps = fps
        self.time_stamp = time_stamp
        self.video_name = video_name
        self.last_time = last_time
        self.start_time = start_time

    def subplot_shape(self):
        """
        Determines the layout (rows and columns) for the subplots based on the total number of modes.
        
        Returns:
        - tuple: Number of rows and columns for the subplots.
        """
        t = []
        for ell in self.ell_range:
            l = 2 * ell
            l_1 = l + 1
            t.append(l_1)
        tot = sum(t)
        num_cols = 3
        num_rows = (tot + num_cols - 1) // num_cols
        return (num_rows, num_cols)

    def lastnum(self):
        """
        Reads the waveform data and determines the last time step available in the dataset.
        
        Returns:
        - int: Total number of time steps in the waveform data.
        """
        with h5py.File(self.hdata_path, 'r') as hfile:
            h_data = hfile[f'Y_l{2}_m{2}.dat'][...]
        self.arr_time = np.array([a[0] for a in h_data], dtype=float)
        last = len(self.arr_time)
        return last

    def plot_modes(self):
        """
        Generates spherical harmonic visualizations of gravitational wave modes for each time step.
        - Creates 3D plots for each combination of `ell` and `m` values.
        - Saves the resulting images to the specified output directory.
        
        Uses:
        - h5py to read waveform data.
        - matplotlib for plotting.
        - tqdm for progress tracking.
        """
        
        if self.last_time == None:
            last = self.lastnum()
        else:
            last = self.last_time

        if self.start_time == None:
            start = 1000
        else:
            start = self.start_time
            

        for i in tqdm(range(start, last, self.time_stamp)):
            fig = plt.figure(figsize=self.fig_size)
            sum_plots = 0 
            for ell in self.ell_range:
                emm_range = np.arange(-ell, ell + 1)
                for emm in emm_range:
                    h_data = self.hdata[f'Y_l{ell}_m{emm}.dat'][...]
                    c = h_data[:, 1] + 1j * h_data[:, 2]
                    m2_Y = Yslm_vec(ell=ell, emm=emm, spin_weight=-2, theta_grid=self.theta_new, phi_grid=self.phi_new).real
                    s = np.einsum('i,jk->ijk', c, m2_Y)
                    U = s[i].real
                    xu = U * self.x
                    yu = U * self.y
                    zu = U * self.z
                    ax = fig.add_subplot(self.subplot_shape()[0], self.subplot_shape()[1], sum_plots + 1, projection='3d')
                    fig.patch.set_facecolor('black')
                    ax.set_facecolor('black')
                    color_dimension = U
                    minn, maxx = color_dimension.min(), color_dimension.max()
                    norm = plt.Normalize(minn, maxx)
                    alpha = self.calculate_alpha(ell)
                    m = plt.cm.ScalarMappable(norm=norm, cmap='viridis')
                    m.set_array([])
                    fcolors = m.to_rgba(color_dimension, alpha=alpha)
                    surf = ax.plot_surface(xu, yu, zu, linewidth=0, antialiased=False, facecolors=fcolors)
                    ax.set_title(f'l={ell}, m={emm}', color='white', fontsize=20)
                    surf.set_cmap('viridis_r')
                    ax.axis('off')
                    sum_plots += 1

            plt.tight_layout()

            if self.output_dir:
                if not os.path.exists(self.output_dir):
                    os.makedirs(self.output_dir)
                plt.savefig(f'{self.output_dir}/s{ell}{emm}_{i:05d}.jpg')
                plt.close(fig)

        print('Images are saved in the output directory')


    def calculate_alpha(self, ell):
        """
        Assigns transparency values to plots based on the `ell` value.
        
        Parameters:
        - ell (int): The `ell` value of the spherical harmonic mode.
        
        Returns:
        - float: Transparency value for the mode.
        """
        if ell == 2:
            return 0.9
        elif ell == 3:
            return 0.25
        elif ell == 4:
            return 0.125
        else:
            return 0.03

    def images_to_video(self):
        """
        Converts the generated images into a video.
        - Reads all .jpg images from the output directory.
        - Uses OpenCV to combine them into an MP4 video file.
        
        Outputs:
        - A video file with the specified name and FPS.
        """
        images = [img for img in os.listdir(self.output_dir) if img.endswith(".jpg")]
        images = np.sort(images)
        frame = cv2.imread(os.path.join(self.output_dir, images[0]))
        height, width, layers = frame.shape
        video = cv2.VideoWriter(self.video_name, cv2.VideoWriter_fourcc(*'mp4v'), self.fps, (width, height))

        for image in images:
            video.write(cv2.imread(os.path.join(self.output_dir, image)))

        cv2.destroyAllWindows()
        video.release()

    def run(self):
        """
        Main driver method to execute the animation workflow.
        - Generates and saves 3D plots as images.
        - Converts the images into a video.
        
        Workflow:
        1. Call `plot_modes` to generate images.
        2. Convert images to video using `images_to_video`.
        """
        self.plot_modes()
        print('Images are being converted to video')
        self.images_to_video()
        print('Your Video is ready')