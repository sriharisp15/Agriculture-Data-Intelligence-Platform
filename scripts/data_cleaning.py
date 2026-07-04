import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/APY.csv") 

df.columns = df.columns.str.strip()

print("Original Shape:", df.shape)

# Remove rows with missing Crop
df = df.dropna(subset=["Crop"])

# Fill missing Production values with 0
df["Production"] = df["Production"].fillna(0)

print("Cleaned Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv("data/processed/cleaned_agriculture_data.csv", index=False)

print("\nCleaned dataset saved successfully!")