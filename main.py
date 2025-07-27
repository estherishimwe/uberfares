import pandas as pd

print("📥 Step 1: Load dataset")
# a) Load dataset
df = pd.read_csv('uber.csv')

print("✅ Loaded dataset")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:\n", df.dtypes)

print("\n🩺 Step 1c: Initial data quality check")
print("Missing values per column:\n", df.isnull().sum())
print("\nDescriptive statistics:\n", df.describe(include='all'))

# d) Handle missing values and remove invalid data
print("\n🧹 Step 1d: Clean data")
df_cleaned = df.dropna(subset=['fare_amount', 'pickup_datetime'])
df_cleaned = df_cleaned[df_cleaned['fare_amount'] > 0]

print("New shape after cleaning:", df_cleaned.shape)
print("Missing values after cleaning:\n", df_cleaned.isnull().sum())

# e) Export cleaned dataset
df_cleaned.to_csv('uber_fares_cleaned.csv', index=False)
print("✅ Exported: uber_fares_cleaned.csv")

# 3️⃣ Feature Engineering
print("\n🛠 Step 3: Feature engineering")
# Convert pickup_datetime
df_cleaned['pickup_datetime'] = pd.to_datetime(df_cleaned['pickup_datetime'], errors='coerce')
df_cleaned = df_cleaned.dropna(subset=['pickup_datetime'])

# Add new columns
df_cleaned['hour'] = df_cleaned['pickup_datetime'].dt.hour
df_cleaned['day'] = df_cleaned['pickup_datetime'].dt.day
df_cleaned['month'] = df_cleaned['pickup_datetime'].dt.month
df_cleaned['weekday'] = df_cleaned['pickup_datetime'].dt.weekday

# Peak hours flag
peak_hours = [7,8,9,16,17,18]
df_cleaned['is_peak'] = df_cleaned['hour'].apply(lambda x: 1 if x in peak_hours else 0)

print("✅ Added features: hour, day, month, weekday, is_peak")
print("Columns now:\n", df_cleaned.columns.tolist())

# Save enhanced dataset
df_cleaned.to_csv('uber_fares_enhanced.csv', index=False)
print("✅ Exported: uber_fares_enhanced.csv")

print("\n🎉 DONE! Your cleaned and enhanced datasets are ready for Power BI")