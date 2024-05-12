#VERGARA, IVYANN ROMIJN H. 
# 6. Create a new file that has the same contents but with a new column called “HRID” where the value is the concatenation of location, site, and replicate (separated by a dash; replace any occurrence of a comma with a dash).  For example, the value of HRID for the first row is: Calatagan-Batangas-BuntongGasang-2.    (5 points)

import pandas as pd

# Open file
filename = 'Ivyann Romijn Vergara - Exam_Table.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(filename, skip_blank_lines=True).dropna()

# Read the CSV file into a DataFrame
df = pd.read_csv(filename)

df["HRID"] = df["Location"].str.replace(",", "-").str.replace(" ", "") + "-" + df["Site"] + "-" + df["Replicate"].astype(str)


# Save the modified data to a new CSV file
df.to_csv('b6_output.csv', index=False)

print("Saved a new file")