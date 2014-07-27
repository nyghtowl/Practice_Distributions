'''
Distirbution Review

'''

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn


def create_matrix(filename):
    with open(filename) as f:
        data = csv.reader(f)
        body = []
        for idx, row in enumerate(data):
            if idx == 0: # header
                header = row
            else:
                # We know this is brute force but moving on to plots - would like to try mask eventually
                if "?" in row[0] or "?" in row[1] or "?" in row[3] or "?" in row[4] or "?" in row[7]:
                    pass
                else:
                    body.append(row)
    return header, np.array(body)

# TO DO: Add legend to up left corner
def plot_ages(plot_pt, location_data):
    fig, axes = plt.subplots(2,2, figsize=(12,12))
    ax = [axes[0][0],axes[0][1],axes[1][0],axes[1][1]]
    idx = 0
    for location, data in location_data.iteritems():
        ages = (data[plot_pt]).astype(np.float)
        # hex color
        ax[idx].hist(ages, bins=(max(ages)-min(ages)), color='#006633')
        ax[idx].set_title(location)
        ax[idx].set_ylabel("Count")
        ax[idx].set_xlabel("Age")
        ax[idx].set_xlim([25, 80])
        idx += 1

# TO DO group by heart rate vs cholesterol
def plot_heart_cholesterol(plot_pts, location_data):
    sex, ch, hr = plot_pts
    fig, axes = plt.subplots(4,1, figsize=(12,36))
    # axes = plt.axes() # contains on one
    f_chol_list, m_chol_list, f_hr_list, m_hr_list = [],[],[],[]

    gender_by_condition = {}

    for location, data in location_data.iteritems():    
        # Build sub matrix
        sub_matrix = np.zeros(shape=(len(data[sex]),3))
        sub_matrix[:,0] = data[sex]
        sub_matrix[:,1] = data[ch]
        sub_matrix[:,2] = data[hr]
        
        # Split out data
        female_data = sub_matrix[sub_matrix[:,0] == 0]
        male_data = sub_matrix[sub_matrix[:,0] == 1]
    
        gender_by_condition[location] = [(female_data[:,1]).astype(np.float),(male_data[:,1]).astype(np.float), (female_data[:,2]).astype(np.float), (male_data[:,2]).astype(np.float)]

    for i, (location, gend_cond) in enumerate(gender_by_condition.iteritems()):
        title = location.split('/')[1]
        axes[i].boxplot(gend_cond)
        axes[i].set_title(title.capitalize())
        axes[i].set_xticklabels(['female cholesterol', 'male cholesterol','female heart rate','male heart rate'])

    bb = axes[0].get_bbox_patch()
    bb.set_boxstyle("rarrow", pad=0.6)


# Spring required that we read in the doc and create a data structure before we learned pandas. Build dict of dict to retain labels.
def main():
    file_list = ['./data/cleveland_heart.csv','./data/hungarian_heart.csv', './data/switzerland_heart.csv', './data/long_beach.csv']
    data_matrices, location_names = [], []

    for f in file_list:
        location_name = f.replace('.csv', '').replace('./', '')
        location_names.append(location_name)
        header, data = create_matrix(f)
        data_matrices.append({ header[i]: data[:,i] for i in range(len(header))})

    location_data = dict(zip(location_names, data_matrices))

    return location_data


if __name__ == '__main__':
    main()