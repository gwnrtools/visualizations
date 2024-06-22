import os
import numpy as np
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D
from waveformtools.transforms import Yslm_vec
from waveformtools.grids import UniformGrid
import cv2
from tqdm import tqdm
import h5py



class GW_onemode_animator:

    def __init__(self, ell, emm, hdata_path, step, fps, output_dir, video_name):
        self.ell = ell
        self.emm = emm
        self.hdata_path = hdata_path
        self.ginfo = UniformGrid()
        self.theta_grid, self.phi_grid = self.ginfo.meshgrid
        self.output_dir = output_dir
        self.video_name = video_name
        self.fps = fps
        self.step = step

        with h5py.File(self.hdata_path, 'r') as hfile:
            h_data = hfile[f'Y_l{self.ell}_m{self.emm}.dat'][...]

        self.arr_hplus = np.array([a[1] for a in h_data], dtype=float)
        self.arr_hcross = np.array([a[2] for a in h_data], dtype=float)

        self.hplus_t = np.abs(self.arr_hplus[0])
        self.c = np.array(h_data[:, 1], dtype=float) + 1j * np.array(h_data[:, 2], dtype=float)
        self.m2_Y = Yslm_vec(ell=ell, emm=emm, spin_weight=-2, theta_grid=self.theta_grid, phi_grid=self.phi_grid).real
        self.s = np.einsum('i,jk->ijk', self.c, self.m2_Y)

        self.St = np.sin(self.theta_grid)
        self.Ct = np.cos(self.theta_grid)
        self.Sp = np.sin(self.phi_grid)
        self.Cp = np.cos(self.phi_grid)

        self.x = self.St * self.Cp
        self.y = self.St * self.Sp
        self.z = self.Ct

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def create_frames(self):
        print('Images are being created')

        for time_stamp in tqdm(range(1000, len(self.s), self.step)):
            U = self.s[time_stamp].real

            xu = U * self.x
            yu = U * self.y
            zu = U * self.z

            fig = plt.figure(figsize=(10, 8))
            ax = plt.axes(projection='3d')

            fig.patch.set_facecolor('black')
            ax.set_facecolor('black')

            color_dimension = U
            minn, maxx = color_dimension.min(), color_dimension.max()
            norm = plt.Normalize(minn, maxx)

            m = plt.cm.ScalarMappable(norm=norm, cmap='viridis')
            m.set_array([])

            fcolors = m.to_rgba(color_dimension)

            ax.set_title(f'l={self.ell},m={self.emm}', color='white', size=10)
            surf = ax.plot_surface(xu, yu, zu, linewidth=0, antialiased=False, facecolors=fcolors)
            surf.set_cmap('viridis_r')
            ax.axis('off')

            plt.savefig(f'{self.output_dir}/s{self.ell}{self.emm}_{time_stamp:05d}.jpg')
            plt.close(fig)

        print('Images are saved in the output directory')

    def images_to_video(self):
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
        self.create_frames()
        print('Images are being converted to video')
        self.images_to_video()
        print('Your Video is ready')
