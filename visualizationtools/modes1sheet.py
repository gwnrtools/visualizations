from waveformtools.transforms import Yslm_vec
from waveformtools.grids import UniformGrid
from mpl_toolkits.mplot3d import Axes3D
import h5py
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

class ModesInASheet:
    def __init__(self, ell_range, hdata_path, fig_size=(56, 56)):
        self.ell_range = ell_range
        self.hdata = h5py.File(hdata_path, 'r')
        self.ginfo = UniformGrid(500,500)
        self.theta_grid, self.phi_grid = self.ginfo.meshgrid
        self.x = np.sin(self.theta_grid) * np.cos(self.phi_grid)
        self.y = np.sin(self.theta_grid) * np.sin(self.phi_grid)
        self.z = np.cos(self.theta_grid)
        self.fig_size = fig_size

    def subplot_shape(self):
        # Calculate the total number of subplots needed
        t = []
        for i in range(len(self.ell_range)):
            l = 2 * self.ell_range[i]  # Corrected 'self.ell_range[i]' instead of 'slef.ell_range[i]'
            l_1 = l + 1
            t.append(l_1)
            
        # Total number of subplots
        tot = sum(t)
    
        # Calculate the number of rows and columns for subplots
        num_cols = 3
        num_rows = (tot + num_cols - 1) // num_cols  # Ensure num_rows is ceil(tot / num_cols)
    
        return (num_rows, num_cols)

    def plot_modes(self, save_fig=False, file_path=None):
        fig = plt.figure(figsize=self.fig_size)
        sum_plots = 0

        for ell in self.ell_range:
            emm_range = np.arange(-ell, ell + 1)
            for emm in tqdm(emm_range, desc=f'Processing ell={ell}'):
                h_data = self.hdata[f'Y_l{ell}_m{emm}.dat'][...]
                arr_hplus = [a[1] for a in h_data]
                c = h_data[:, 1] + 1j * h_data[:, 2]
                m2_Y = Yslm_vec(ell=ell, emm=emm, spin_weight=-2, theta_grid=self.theta_grid, phi_grid=self.phi_grid).real
                s = np.einsum('i,jk->ijk', c, m2_Y)
                U = s[0].real
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
        
        if save_fig==True: 
            plt.savefig(file_path, bbox_inches='tight', facecolor=fig.get_facecolor())
            print('Image is saved!')
            
        plt.show()

    def calculate_alpha(self, ell):
        if ell == 2:
            return 0.9
        elif ell == 3:
            return 0.25
        elif ell == 4:
            return 0.125
        else:
            return 0.1