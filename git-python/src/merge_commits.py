import glob
import pandas as pd

frames = []
for path in glob.glob("jupyter/commits-*.csv"):
    df = pd.read_csv(path)
    frames.append(df)

result = pd.concat(frames, ignore_index=True)
result.to_csv("jupyter/commits.csv")
