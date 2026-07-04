import pandas as pd

df = pd.read_csv("data/processed/cleaned_agriculture_data.csv")

print("===== KPI METRICS =====")

print(f"Total States: {df['State'].nunique()}")
print(f"Total Crops: {df['Crop'].nunique()}")
print(f"Total Seasons: {df['Season'].nunique()}")

print(f"Total Production: {df['Production'].sum():,.0f}")
print(f"Total Area: {df['Area'].sum():,.0f}")

print(f"Average Yield: {df['Yield'].mean():.2f}")