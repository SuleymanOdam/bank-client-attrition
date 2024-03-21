import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Set page configuration (only once at the beginning)
st.set_page_config(page_title="Bank_churners", page_icon=':chart:')

# Load data
data_folder = "data"  # Adjust this folder name if needed
file_path = os.path.join(data_folder, "bankchurners.csv")
df = pd.read_csv(file_path, encoding='utf-8')

# Display data
st.title(':chart: Outflow Dashboard Bank_churners')
st.write("Просмотр данных:")
st.write(df)
st.write("График распределения отток:")

# Add charts or other visualizations here
# Histogram
hist_values = np.histogram(df['avg_open_to_buy'], bins=20, range=(0, 100))[0]
st.bar_chart(hist_values)

# Bar chart
plt.figure(figsize=(8, 6))
plt.bar(df['months_inactive_12_mon'], df['contacts_count_12_mon'], color='skyblue')
plt.xlabel('Months Inactive (Last 12 Months)')
plt.ylabel('Contact Counts')
plt.title('Contact Counts vs. Months Inactive')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Run the app
if __name__ == "__main__":
    st.write("Dashboard Streamlit app is running!")