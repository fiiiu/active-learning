
import platform

if platform.system()=='Darwin':
	directory='/Users/alejo/Neuro/ActiveLearning/'
elif platform.system()=='Linux':
	#directory='/home/alejo/Run/active-learning/'
    directory='/home/alejo/Neuro/ActiveLearning/'

output_directory=directory+'Output/'

n_kids=31#31#5#5#1#29 #31 total, use 40
#truncate=75
#n_r_theo=1#5
n_r_random=20#20#20#0#50

epsilon=1e-3
