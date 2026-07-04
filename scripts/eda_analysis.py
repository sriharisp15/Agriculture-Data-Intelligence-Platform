import pandas as pd

df = pd.read_csv("data/processed/cleaned_agriculture_data.csv")

print("===== DATASET OVERVIEW =====")
print("Total Records:", len(df))
print("Total States:", df["State"].nunique())
print("Total Crops:", df["Crop"].nunique())
print("Total Seasons:", df["Season"].nunique())

print("\n===== TOTAL PRODUCTION =====")
print(df["Production"].sum())

print("\n===== TOTAL AREA =====")
print(df["Area"].sum())

print("\n===== TOP 10 CROPS BY PRODUCTION =====")
print(
    df.groupby("Crop")["Production"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\n===== TOP 10 STATES BY PRODUCTION =====")
print(
    df.groupby("State")["Production"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)