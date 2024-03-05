import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
# Gantilah 'path/to/visualized_data.csv' dengan path sesuai dengan file CSV Anda
data = pd.read_csv('./dataframe.csv')

# Create a Streamlit app
def main():
    # Add a title to the app
    st.title("E-Commerce Data Dashboard")

    # Display the data
    st.subheader("Visualized Data")
    st.write(data)

    # Visualize the data
    st.subheader("Visualizations")

    # Example visualization: Bar plot of total payment value per product
    st.subheader("Bar Plot of Total Payment Value per Product")
    product_payment = data.groupby('product_id')['payment_value'].sum().sort_values(ascending=False).head(10)
    fig, ax = plt.subplots()
    product_payment.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

if __name__ == "__main__":
    main()
