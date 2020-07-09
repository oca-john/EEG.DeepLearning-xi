# mne.python.loading.data

import os
import numpy as np
import mne

# 1. Loading data
# mne-python库支持直接读取各种格式的数据文件，支持众多EEG数据采集设备
# 主要包括设置数据文件夹，原始数据读取到文件句柄，通过句柄传递给变量
sample_data_folder = mne.datasets.sample.data_path()                      # 数据文件夹
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',  # 数据读到句柄
                                    'sample_audvis_filt-0-40_raw.fif')
raw = mne.io.read_raw_fif(sample_data_raw_file)                           # 句柄传给变量
# 未知如下的嵌套方式的文件读取是否可行：
# raw = mne.io.read_raw_fif(os.path.join(mne.datasets.sample.data_path(),'MEG','sample','sample_audvis_filt-0-40_raw.fif'))
# 查看原始数据
print(raw)
# 查看原始数据的信息（采集过程中设备和采样率等信息）
print(raw.info)

# raw对象本身带有一些内建的方法
raw.plot_psd(fmax=50)                 # 绘制50Hz以下的信号
raw.plot(duration=5, n_channels=30)   # 交互式的绘图方式，可以滚动、缩放、不良通道标记、注释

# 2. Preprocessing
# 包含很多信号预处理方法（麦克斯韦滤波，信号空间投影，独立分量分析，滤波，下采样）
# 此案例将展示独立成分分析（ICA）清理数据
# set up and fit the ICA
ica = mne.preprocessing.ICA(n_components=20, random_state=97, max_iter=800)
ica.fit(raw)
ica.exclude = [1, 2]                  # details on how we picked these are omitted here
ica.plot_properties(raw, picks=ica.exclude)

orig_raw = raw.copy()
raw.load_data()
ica.apply(raw)

# show some frontal channels to clearly illustrate the artifact removal
chs = ['MEG 0111', 'MEG 0121', 'MEG 0131', 'MEG 0211', 'MEG 0221', 'MEG 0231',
       'MEG 0311', 'MEG 0321', 'MEG 0331', 'MEG 1511', 'MEG 1521', 'MEG 1531',
       'EEG 001', 'EEG 002', 'EEG 003', 'EEG 004', 'EEG 005', 'EEG 006',
       'EEG 007', 'EEG 008']
chan_idxs = [raw.ch_names.index(ch) for ch in chs]
orig_raw.plot(order=chan_idxs, start=12, duration=4)
raw.plot(order=chan_idxs, start=12, duration=4)

