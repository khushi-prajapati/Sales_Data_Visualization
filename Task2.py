import pandas as pd

# 1️⃣ Load dataset
df = pd.read_csv(r"Tasks\Task2\SuperStoreOrders.csv")

print("Initial Shape:", df.shape)

# 2️⃣ Convert date columns (safe mixed-format handling)
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], dayfirst=True, errors='coerce')

# Remove rows where dates failed to convert
df = df.dropna(subset=['order_date', 'ship_date'])

# 3️⃣ Remove duplicates
df = df.drop_duplicates()

# 4️⃣ Remove remaining null values
df = df.dropna()

# 5️⃣ Standardize text columns
text_cols = ['customer_name', 'segment', 'state', 'country',
             'market', 'region', 'category', 'sub_category',
             'product_name', 'order_priority']

for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.lower()

# 6️⃣ Create Delivery Days column
df['delivery_days'] = (df['ship_date'] - df['order_date']).dt.days

# 7️⃣ Create Profit Status column
df['profit_status'] = df['profit'].apply(lambda x: 'profit' if x > 0 else 'loss')

# 8️⃣ Extract Year & Month
df['year'] = df['order_date'].dt.year
df['month'] = df['order_date'].dt.month_name()

print("Final Shape:", df.shape)

# 9️⃣ Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)

print("✅ Cleaning Completed Successfully!")