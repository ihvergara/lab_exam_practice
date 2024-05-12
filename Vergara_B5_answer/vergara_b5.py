#VERGARA, IVYANN ROMIJN H. 
# 5. Display the average count for Pomacentrus adelus. (5 points)

import pandas as pd
# Open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename, skip_blank_lines=True).dropna()

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

count = df.groupby('Scientific Name')['Count'].mean()
new_df= pd.DataFrame({"Scientific Name": ["Pomacentrus adelus"], "Average count": count["Pomacentrus adelus"]})

# Save the filtered data to a CSV file
new_df.to_csv('b5_output.csv', index=False)

print("Saved a new file.")