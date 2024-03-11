import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data
# Gantilah 'path/to/visualized_data.csv' dengan path sesuai dengan file CSV Anda
df = pd.read_csv('./dataframe.csv')
df_geo = pd.read_csv('./geolocation.csv')

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

# Fungsi untuk menghasilkan visualisasi persebaran barang
def visualize_product_distribution_map(df_geo):
    st.write("Product Sales Distribution Map")
    fig = px.scatter_mapbox(df_geo.drop_duplicates(subset='customer_unique_id'), 
                            lat="geolocation_lat", lon="geolocation_lng", 
                            hover_name="geolocation_city", hover_data=["geolocation_state"],
                            zoom=3, height=600)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig)

# Menampilkan judul dan deskripsi
st.title('Product Analysis Dashboard')
st.write("This dashboard presents visualizations of product data including top sold products and products distribution maps.")

# Menampilkan visualisasi barang yang banyak terjual
st.header('Top Sold Products')
visualize_top_sold_products(df)
st.write("The best-selling product is cama_mesa_banho or bed_bath_table")

# Menampilkan visualisasi barang dengan keuntungan terbesar
st.header('Products Distribution Maps')
visualize_product_distribution_map(df_geo)
st.write("The distribution of products is dominated by Brazil, especially in the southeast and south regions, with the highest concentration in the capital city.")
