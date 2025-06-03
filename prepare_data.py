import pandas as pd

# Leitura do CSV original
df = pd.read_csv("data/2019-Oct.csv")

# Conversão de data
df['event_time'] = pd.to_datetime(df['event_time'])
df['date'] = df['event_time'].dt.date
df['hour'] = df['event_time'].dt.hour
df['day_of_week'] = df['event_time'].dt.day_name()

# Filtro apenas de compras
df_purchases = df[df['event_type'] == 'purchase'].copy()

# Exporta a base limpa
df_purchases.to_csv("data/purchases_clean.csv", index=False)

# Feedback visual
print(f"Base tratada salva com {len(df_purchases)} registros de compras.")
