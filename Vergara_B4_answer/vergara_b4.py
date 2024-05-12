#VERGARA, IVYANN ROMIJN H. 
# 4. Get all unique scientific names and corresponding average estimated size (cm) and save to a new file. (3 points)

import pandas as pd

# open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

df = pd.read_csv(filename, skip_blank_lines=True).dropna()

# get scientfic names
one_df = unique_names = df['Scientific Name'].unique()  

# Group by scientific name and calculate average estimated size
two_df = df.groupby('Scientific Name')['Size Est (cm)'].mean()

# Combine unique names and average sizes into a DataFrame
output_df = pd.DataFrame({'Scientific Names': one_df, 'Size Est (cm)': two_df})

# Save the data to a new CSV file
output_df.to_csv('./b4_output.csv', index=False)

print("Saved a new file.")