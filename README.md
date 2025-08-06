# 📊 Supply Chain KPI Monitoring Dashboard

An interactive Streamlit web application to **visualize**, **monitor**, and **predict** key performance indicators (KPIs) critical to effective supply chain management.

🔗 **Live App**: [Click here to view the Dashboard](https://supply-chain-kpi-dashboard-85qu7jgaz5mftqhne5osdx.streamlit.app/)

---

## 🚀 Features

✅ Real-time visualization of key supply chain metrics  
✅ Forecasting of stockout risk using a machine learning model  
✅ User-friendly interface with dropdown-based KPI selection  
✅ Streamlined data input via CSV upload  
✅ Built using Python, Streamlit, Matplotlib, Pandas, and Scikit-learn

---

## 📌 KPIs Included

- Order Quantity  
- Lead Time  
- Demand Forecast Accuracy  
- Inventory Turnover  
- On Time Delivery Rate  
- Stockout Rate  

---

## 🧠 Stockout Prediction

A trained machine learning model (`stockout_model.pkl`) uses input features such as demand accuracy, lead time, and order quantity to **predict the likelihood of a stockout** — helping businesses take proactive action.

---

## 🗂️ How to Use

1. Upload your CSV file containing the KPI data (ensure correct column headers).
2. Choose a KPI from the dropdown to visualize.
3. Navigate to the "Stockout Prediction" tab to test predictions.
4. View results instantly on dynamic plots and tables.

---

## 📁 Folder Structure

📦 supply-chain-kpi-dashboard
┣ 📄 streamlit_app.py
┣ 📄 stockout_model.pkl
┣ 📄 supply_chain_data.csv
┣ 📄 requirements.txt
┗ 📄 README.md


---

## 🔧 Technologies Used

- Python 3.x  
- Streamlit  
- Pandas  
- Matplotlib  
- Scikit-learn  
- NumPy  

---

## 🌐 Live Deployment

The app is deployed on **Streamlit Cloud** and is accessible here:  
👉 [https://supply-chain-kpi-dashboard-85qu7jgaz5mftqhne5osdx.streamlit.app/](https://supply-chain-kpi-dashboard-85qu7jgaz5mftqhne5osdx.streamlit.app/)

---

## 👨‍💻 Author

**Saksham Srivastava**  
🔗 [GitHub](https://github.com/saksham-srivastava37)

---

## 💡 Future Enhancements

- Add user authentication  
- Region/product-level filtering  
- Database integration for persistent storage  
- Advanced forecasting models

---

## 📝 License

This project is open-source and available under the [MIT License](LICENSE).

