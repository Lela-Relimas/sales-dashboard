import pandas as pd
import streamlit as st
import plotly.express as px

# Título
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
st.title("📊 Dashboard de Vendas - E-commerce")

# Carregar os dados
df = pd.read_csv("data/purchases_clean.csv")
df['date'] = pd.to_datetime(df['date'])

# Sidebar - Filtros
st.sidebar.header("Filtros")
start_date = st.sidebar.date_input("Data inicial", df['date'].min())
end_date = st.sidebar.date_input("Data final", df['date'].max())

# Aplicar filtro
df = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# === Receita por dia ===
st.subheader("📅 Receita por Dia")
sales_by_date = df.groupby('date')['price'].sum().reset_index()
fig1 = px.line(sales_by_date, x='date', y='price', labels={'price': 'Receita'}, title="Receita Total por Dia")
st.plotly_chart(fig1, use_container_width=True)

# === Categorias mais vendidas ===
st.subheader("🏷️ Top 10 Categorias Vendidas")
top_categories = df['category_code'].value_counts().nlargest(10).reset_index()
top_categories.columns = ['Categoria', 'Total de Vendas']
fig2 = px.bar(top_categories, x='Total de Vendas', y='Categoria', orientation='h', title="Top 10 Categorias")
st.plotly_chart(fig2, use_container_width=True)

# === Receita por dia da semana ===
st.subheader("📆 Receita por Dia da Semana")
df['day_of_week'] = pd.to_datetime(df['date']).dt.day_name()
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=days_order, ordered=True)
day_sales = df.groupby('day_of_week')['price'].sum().reset_index()
fig3 = px.bar(day_sales, x='day_of_week', y='price', labels={'price': 'Receita', 'day_of_week': 'Dia da Semana'},
              title="Receita por Dia da Semana")
st.plotly_chart(fig3, use_container_width=True)

# === Top marcas ===
st.subheader("🏢 Marcas com Mais Vendas")
top_brands = df['brand'].value_counts().nlargest(5).reset_index()
top_brands.columns = ['Marca', 'Total']
fig4 = px.bar(top_brands, x='Marca', y='Total', title="Top 5 Marcas")
st.plotly_chart(fig4, use_container_width=True)
