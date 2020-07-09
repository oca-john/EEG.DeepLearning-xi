# mne.python.loading.data

import os
import numpy as np
import mne

# mne-python库支持直接读取各种格式的数据文件，支持众多EEG数据采集设备
# 主要包括设置数据文件夹，原始数据读取到文件句柄，通过句柄传递给变量
sample_data_folder = mne.datasets.sample.data_path()                      # 数据文件夹
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',  # 数据读到句柄
                                    'sample_audvis_filt-0-40_raw.fif')
raw = mne.io.read_raw_fif(sample_data_raw_file)                           # 句柄传给变量
# 未知如下的嵌套方式的文件读取是否可行：
# raw = mne.io.read_raw_fif(os.path.join(mne.datasets.sample.data_path(),'MEG','sample','sample_audvis_filt-0-40_raw.fif'))

