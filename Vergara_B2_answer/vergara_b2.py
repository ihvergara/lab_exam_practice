import pandas as pd

# Open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename, skip_blank_lines=True).dropna()

# Extract only rows where Genus starts with “St” (case insensitive) and save to a new file. (3 points)
new_df = df[df["Genus"].str.match("st", case=False)]

# Save the filtered data to a CSV file
new_df.to_csv('b2_output.csv', index=False)

print("Saved a new file.")

