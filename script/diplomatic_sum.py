#!python

import pandas as pd
import sys

diplomatic_activities = '../_data/diplomatic_activities.csv'

dip_ac_df = pd.read_csv(diplomatic_activities, header=0, parse_dates = ['date'])

month = int(sys.argv[1])
year = int(sys.argv[2])

df_filtered = dip_ac_df[(dip_ac_df['date'].dt.month == month) \
                        & (dip_ac_df['date'].dt.year == year) ]

df_filtered = df_filtered.sort_values(by='format')

df_filtered['Count'] = df_filtered.groupby('format').cumcount() + 1

df_count = df_filtered.pop('Count')

df_filtered.insert(2,'Count', df_count)

df_filtered.to_csv('../_data/diplomatic_{}_{}.csv'.format(year,month), index=False, date_format='%m/%d/%Y')