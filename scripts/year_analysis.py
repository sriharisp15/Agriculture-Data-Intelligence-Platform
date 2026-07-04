import pandas as pd

df = pd.read_csv("data/processed/cleaned_agriculture_data.csv")

yearly_production = (
    df.groupby("Crop_Year")["Production"]
      .sum()
      .reset_index()
)

print(yearly_production.head())
print("\n")
print(yearly_production.tail())