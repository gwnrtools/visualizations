class Animator_ModesInASheet:
    def __init__(self, ell_range, hdata_path, time_stamp, fps, start_time= None, last_time=None, fig_size=(56, 56), output_dir='output', video_name='output_video.mp4'):
        self.ell_range = ell_range
        self.hdata_path = hdata_path
        self.hdata = h5py.File(hdata_path, 'r')
        self.ginfo = UniformGrid()
        self.theta_grid, self.phi_grid = self.ginfo.meshgrid
        self.x = np.sin(self.theta_grid) * np.cos(self.phi_grid)
        self.y = np.sin(self.theta_grid) * np.sin(self.phi_grid)
        self.z = np.cos(self.theta_grid)
        self.fig_size = fig_size
        self.output_dir = output_dir
        self.fps = fps
        self.time_stamp = time_stamp
        self.video_name = video_name
        self.last_time = last_time
        self.start_time = start_time

    def subplot_shape(self):
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
        with h5py.File(self.hdata_path, 'r') as hfile:
            h_data = hfile[f'Y_l{2}_m{2}.dat'][...]
        self.arr_time = np.array([a[0] for a in h_data], dtype=float)
        last = len(self.arr_time)
        return last

    def plot_modes(self):
        
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
                    m2_Y = Yslm_vec(ell=ell, emm=emm, spin_weight=-2, theta_grid=self.theta_grid, phi_grid=self.phi_grid).real
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
        if ell == 2:
            return 0.9
        elif ell == 3:
            return 0.25
        elif ell == 4:
            return 0.125
        else:
            return 0.1

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
        self.plot_modes()
        print('Images are being converted to video')
        self.images_to_video()
        print('Your Video is ready')

