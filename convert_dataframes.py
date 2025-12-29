import pandas as pd
import json

# Example: Create your dataframes (replace with your actual data)
df1 = pd.DataFrame({
    'id': range(1, 21),
    'name': [f'Person {i}' for i in range(1, 21)],
    'role': [f'Role {i}' for i in range(1, 21)],
    'department': [f'Dept {i % 5}' for i in range(1, 21)]
})

df2 = pd.DataFrame({
    'id': range(1, 21),
    'product': [f'Product {i}' for i in range(1, 21)],
    'price': [i * 10 for i in range(1, 21)],
    'category': [f'Category {i % 3}' for i in range(1, 21)]
})

df3 = pd.DataFrame({
    'id': range(1, 21),
    'city': [f'City {i}' for i in range(1, 21)],
    'population': [1000000 + i * 100000 for i in range(1, 21)],
    'country': [f'Country {i % 5}' for i in range(1, 21)]
})

df4 = pd.DataFrame({
    'id': range(1, 21),
    'book': [f'Book {i}' for i in range(1, 21)],
    'author': [f'Author {i}' for i in range(1, 21)],
    'year': [1900 + i * 5 for i in range(1, 21)]
})

# Convert dataframes to JSON format
data = {
    'dataframe1': df1.to_dict(orient='records'),
    'dataframe2': df2.to_dict(orient='records'),
    'dataframe3': df3.to_dict(orient='records'),
    'dataframe4': df4.to_dict(orient='records')
}

# Save to JSON file
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Data successfully converted to data.json")
print(f"   - DataFrame 1: {len(df1)} rows")
print(f"   - DataFrame 2: {len(df2)} rows")
print(f"   - DataFrame 3: {len(df3)} rows")
print(f"   - DataFrame 4: {len(df4)} rows")

# Optional: Preview the JSON structure
print("\n📄 Sample of the JSON structure:")
print(json.dumps({k: v[:2] for k, v in data.items()}, indent=2)[:500] + "...")
