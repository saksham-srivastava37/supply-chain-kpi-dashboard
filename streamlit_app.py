import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

# Load the trained model
with open("stockout_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("📦 Supply Chain KPI Monitoring & Stockout Prediction Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("Upload your supply chain data CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Raw Data")
    st.write(data.head())

    # Create two columns for layout
    col1, col2 = st.columns(2)

    # KPI Visualization (Left Column)
    with col1:
        st.subheader("📈 KPIs Overview")
        kpi_option = st.selectbox("Select a KPI to visualize:", [
            "Order Quantity", "On Time Delivery Rate", "Demand Forecast Accuracy", 
            "Stockout Rate", "Lead Time", "Inventory Turnover"
        ])

        if kpi_option in data.columns:
            fig, ax = plt.subplots(figsize=(6, 3))  # smaller chart size
            sns.lineplot(data=data, x=data.columns[0], y=kpi_option, ax=ax)
            plt.xticks(rotation=45)
            st.pyplot(fig)
        else:
            st.warning(f"Column '{kpi_option}' not found in data.")

    # Stockout Prediction (Right Column)
    with col2:
        st.subheader("🤖 Stockout Prediction")
        required_columns = ['Order Quantity', 'Lead Time', 'Demand Forecast Accuracy', 'Inventory Turnover']

        missing_cols = [col for col in required_columns if col not in data.columns]
        if missing_cols:
            st.error(f"The following required columns are missing in your uploaded file: {missing_cols}")
        else:
            # Prediction
            X = data[required_columns]
            predictions = model.predict(X)
            data['Stockout Prediction'] = predictions

            st.success("✅ Predictions added successfully!")

            # Show bar chart of stockout prediction results
            st.write("### 📉 Stockout Prediction Distribution")
            fig2, ax2 = plt.subplots(figsize=(4, 3))
            sns.countplot(x='Stockout Prediction', data=data, ax=ax2)
            ax2.set_xticklabels(['No Stockout', 'Stockout'])
            st.pyplot(fig2)

    # Full table below columns
    st.subheader("🧾 Data with Stockout Predictions")
    st.write(data)

    # Download button
    csv = data.to_csv(index=False).encode('utf-8')
    st.download_button(
        "📥 Download CSV with Predictions",
        data=csv,
        file_name='predicted_data.csv',
        mime='text/csv'
    )

else:
    st.info("Please upload a CSV file to begin.")
