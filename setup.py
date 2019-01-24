#from codes.python import simple_heartbeat_segmentation as shs
from codes.python import load_database,ECG_denoising
from codes.python import QRS_detector
import numpy as np
from scipy.signal import resample
import operator
from numpy import array
import sys
import csv
import os
import matplotlib.pyplot as plt
import wfdb
from wfdb import processing, plot
from codes.python import heartbeat_segmentation as shs


#mitdb = load_mitdb.load_mitdb()

mit100 = load_database.load_patient_record("mitdb","100")
mit100.set_segmented_beats_r_pos()



r_pos = np.array(DB1.patient_records[2].segmented_R_pos)

wfdb.plot_items(signal=DB1.patient_records[2].MLII, ann_samp=[r_pos])

time100 = np.array(mit100.segmented_beat_time)
beats100 = np.array(mit100.segmented_beat_1)
beat_index = np.array(mit100.segmented_beat_index)

wfdb.plot_items(signal=mit100.segmented_beat_1[0])

load_database.display_signal(mit100.segmented_beat_1[2])

 




patient_list_1 = ["101","106","108","109","112","114","115","116","118","119","122","124","201","203","205","207","208","209","215","220","223","230"]
patient_list_2 = ["100","103","105","111","113","117","121","123","200","202","210","212","213","214","219","221","222","228","231","232","233","234"]
DB1 = load_database.create_ecg_database("mitdb",patient_list_1)
DB2 = load_database.create_ecg_database("mitdb",patient_list_2)

 

DB1list = list()

beats_lens = list()
time_lens = list()
class_lens = list()

mit207 = None

for patient in DB1.patient_records:
        
        for i in range(0,len(patient.segmented_beat_time)):
                row = list()
                row.extend(patient.segmented_beat_time[i])
                time_lens.append(len(patient.segmented_beat_time[i]))
                row.extend(patient.segmented_beat_1[i])
                beats_lens.append(len(patient.segmented_beat_1[i]))
                #if (len(patient.segmented_beat_1[i]) == 347):
                        #print(patient.filename)
                        #print(i)
                        #mit207 = patient
                row.extend(patient.segmented_beat_class[i])
                class_lens.append(len(patient.segmented_beat_class[i]))
                DB1list.append(row)

DBn1 = np.array(DB1list)

"""
wfdb.plot_items(signal=mit207.MLII)
load_database.display_signal(beat=mit207.segmented_beat_1[2382])


mit207 = load_database.load_patient_record("mitdb","207")
mit207.set_segmented_beats_r_pos(filtered=False)
len(mit207.segmented_beat_1[2381])
len(mit207.segmented_beat_1[2381])
len(mit207.segmented_beat_1[2383])
mit207.segmented_R_pos[2382]
len(mit207.MLII)
len(mit207.segmented_beat_1)
false_beat = shs.segment(mit207.MLII,mit207.segmented_R_pos[2382],180,180,35)

649799- 649652

DBn1 = np.array(DB1list)

for i in range(0, len(beats_lens)-1):
        if(beats_lens[i] != beats_lens[i+1] ):
                print("this index is different" + str(i))

beats_lens[35831]

for i in range(0, len(time_lens)-1):
        if(time_lens[i] != time_lens[i+1] ):
                print("this index is different" + str(i))

"""

DB2list = list()

for patient in DB2.patient_records:
        
        for i in range(0,len(patient.segmented_beat_time)):
                row = list()
                row.extend(patient.segmented_beat_time[i])
                row.extend(patient.segmented_beat_1[i])
                row.extend(patient.segmented_beat_class[i])
                DB2list.append(row)

DBn2 = np.array(DB2list)





#row = np.array(row, dtype=object)
#row = np.array(row)
        #print(row.shape)
        
       # np.stack((DB1np, row), axis=0)
        #np.stack((DB1np, patient.segmented_beat_1), axis=-1)
        #np.stack((DB1np, patient.segmented_beat_2), axis=-1)





#segmenting record 100
"""  
load_mitdb.display_signal_in_seconds(mit100,mit100.MLII,3)
filter_ecg = ECG_denoising.ECG_FIR_filter()
mit100.filtered_MLII = ECG_denoising.denoising_signal_FIR(mit100.MLII,filter_ecg)
mit100.filtered_V1 = ECG_denoising.denoising_signal_FIR(mit100.V1,filter_ecg)
mit100.segmented_beat_1, mit100.segmented_class_ID, mit100.segmented_beat_class, mit100.segmented_R_pos, mit100.segmented_valid_R, mit100.segmented_original_R  = shs.segment_beat(mit100.filtered_MLII, mit100.time, mit100.annotations, 90, 90)
#np100R = np.concatenate((mit100.segmented_original_R,mit100.segmented_R_pos,mit100.segmented_valid_R ))

MLII = np.array(mit100.MLII)
np100_MLII = np.array(mit100.segmented_beat_1)

np100R = np.array(mit100.segmented_original_R)
np_r_poses = np.array(mit100.segmented_R_pos)
np_valid_r = np.array(mit100.segmented_valid_R)
#np100R = np.append(np100R, np_r_poses, axis=1)
np100R = np.column_stack((np100R, np_r_poses))
np100R = np.column_stack((np100R, np_valid_r))
"""

#checking highest peaks in record 100


"""
count = 0
for i in range(0,len(np100R)):
    ori_R =np100R[i,1]
    seg_R = np100R[i,3]
    if(ori_R <= seg_R):
        count = count+ 1

percent = (len(np100R)/count) * 100
"""
#resampling code
"""
Resampled_MLII = []

def resample_signal(fs):
        factor = 360.0 / fs
        num_samples = int(round(factor * len(mit100.MLII)))
        Resampled_MLII = resample(mit100.MLII, num_samples)

factor = 360.0 / 200
num_samples = int(round(factor * len(mit100.MLII)))
Resampled_MLII = resample(mit100.MLII, num_samples)

index, value = max(enumerate(MLII), key=operator.itemgetter(1))

"""











