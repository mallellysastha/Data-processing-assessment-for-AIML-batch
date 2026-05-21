import numpy as np
import pandas as pd
df = pd.read_csv("students.csv")
math_array = np.array(df['math_score'])
print("Math Score Array:")
print(math_array)
print("Mean:", np.mean(math_array))
print("Median:", np.median(math_array))
print("Maximum:", np.max(math_array))
print("Minimum:", np.min(math_array))
normalized_scores = (math_array - np.min(math_array)) / (np.max(math_array) - np.min(math_array))
print("Normalized Scores:")
print(normalized_scores)
