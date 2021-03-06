# EEG.Soft.List

## Python-based Tools
1. MNE库，`sudo zypper in python3-mne`, or`pip install mne`安装。  

## Matlab-based tools
1. EEGLab，官网下载，解压后从Matlab中调用EEGLab中的函数即可。  
2. Fidldtrip，暂无深入了解。  
3. Brainstorm，暂无深入了解。  

> One of the most important when using a software is usage and community. If the community is large and the software is popular, it is a safer choice as you can be certain a lot of problems people encounter have been solved - it also means that the code is probably more stable and has less bugs. As of late 2019/early 2020, 56% of the citations of the papers below go to EEGLAB, then 25% go to Fieldtrip and 19% got to Brainstorm, and various versions of MNE. Note that EEGLAB and Fieldtrip are intertwined where Fieldtrip users can write EEGLAB plugins by adding simple wrappers on their Fieldtrip code. So the pair EEGLAB+Fieldtrip comprises 81% of the citations and it is continuing to grow, with the Matlab-based tools (which include Brainstorm) gathering about 90% of all citations. This is a strong argument for using Matlab based tools - and in particular EEGLAB - instead of Python based tools at this stage (i.e. MNE). Note that MNE was given an unfair advantage in this analysis since 2 papers (instead of 1 for the other tools) were included (and it is reasonable to assume that a portion of papers cited both articles thus artificially inflating MNE numbers).

> Below is an analysis of papers referencing EEGLAB, FieldTrip, MNE, MNE-Python, and Brainstorm since 2004. Data was obtained Web of Science. The citation per year correspond to the following 5 papers:

>> EEGLAB: Delorme, A. and Makeig, S., 2004. EEGLAB: an open source toolbox for analysis of single-trial EEG dynamics including independent component analysis. Journal of neuroscience methods, 134(1), pp.9-21
>> Fieldtrip: Oostenveld, R., Fries, P., Maris, E., Schoffelen, JM (2011). FieldTrip: Open Source Software for Advanced Analysis of MEG, EEG, and Invasive Electrophysiological Data. Computational Intelligence and Neuroscience, Volume 2011 (2011)
>> MNE 1: A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, L. Parkkonen, M. Hämäläinen, MNE software for processing MEG and EEG data, NeuroImage, Volume 86, 1 February 2014, Pages 446-460, ISSN 1053-8119,
>> MNE Python: A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, R. Goj, M. Jas, T. Brooks, L. Parkkonen, M. Hämäläinen, MEG and EEG data analysis with MNE-Python, Frontiers in Neuroscience, Volume 7, 2013, ISSN 1662-453X
>> Brainstorm: Tadel, F., Baillet, S., Mosher, J.C., Pantazis, D. and Leahy, R.M., 2011. Brainstorm: a user-friendly application for MEG/EEG analysis. Computational intelligence and neuroscience, 2011, p.8.
