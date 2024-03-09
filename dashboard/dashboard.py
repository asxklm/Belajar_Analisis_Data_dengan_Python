import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
# Gantilah 'path/to/visualized_data.csv' dengan path sesuai dengan file CSV Anda
df = pd.read_csv('./dataframe.csv')

# Fungsi untuk menghasilkan visualisasi barang yang banyak terjual
def visualize_top_sold_products(df):
    product_sales = df['product_category_name_english'].value_counts()
    top_product = product_sales.idxmax()
    st.write(f"The product category with the highest sales is: {top_product}")

    fig, ax = plt.subplots(figsize=(10, 6))
    product_sales.head(10).plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Top 10 Most Sold Products')
    ax.set_xlabel('Product')
    ax.set_ylabel('Number of Sales')
    ax.set_xticklabels(product_sales.head(10).index, rotation=45, ha='right')
    st.pyplot(fig)

# Fungsi untuk menghasilkan visualisasi barang dengan keuntungan terbesar
def visualize_most_profitable_products(df):
    df['profit'] = df['price'] - df['freight_value']
    cheap_products = df[df['price'] < df['price'].mean()]
    expensive_products = df[df['price'] >= df['price'].mean()]

    cheap_profit = cheap_products['profit'].mean()
    expensive_profit = expensive_products['profit'].mean()

    st.write("Explanation:")
    st.write(f"The product category with expensive products generates higher average profits than the cheap ones.")

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(['Cheap Products', 'Expensive Products'], [cheap_profit, expensive_profit], color=['skyblue', 'salmon'])
    ax.set_title('Average Profit Comparison')
    ax.set_xlabel('Product Price Range')
    ax.set_ylabel('Average Profit')
    ax.set_ylim(0, max(cheap_profit, expensive_profit) * 1.2)
    st.pyplot(fig)

# Membaca data dari file atau sumber data lainnya
# Misalnya df = pd.read_csv('nama_file.csv')

# Menampilkan judul dan deskripsi
st.title('Product Analysis Dashboard')
st.write("This dashboard presents visualizations of product data including top sold products and most profitable products.")

# Menampilkan visualisasi barang yang banyak terjual
st.header('Top Sold Products')
visualize_top_sold_products(df)

# Menampilkan visualisasi barang dengan keuntungan terbesar
st.header('Most Profitable Products')
visualize_most_profitable_products(df)
