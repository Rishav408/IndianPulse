# ⚡ Streamlit Dashboard Guide - IndianPulse

IndianPulse includes an alternative Python-only interactive dashboard built using **Streamlit** and **Plotly**. This interface is ideal for fast data exploration and rapid prototyping.

---

## 🌟 Features

* **11 Key Indicators**: GDP Growth, CPI, GST collections, Unemployment, Forex Reserves, IIP, Repo Rate, Trade Balance, Financial Inclusion Index, Digital Payments, and CLI.
* **Interactive Charting**: Easily toggle between **Line**, **Area**, **Bar**, and **Scatter** plots powered by Plotly.
* **Dynamic Time Filtering**: Quick-filter by All Time, Last 5 Years, Last 3 Years, or Last Year.
* **Advanced Python-based Analytics**:
  * Pearson Correlation Heatmaps.
  * Normalized Multi-Indicator Comparisons (standardizing different units onto a single comparative chart).
  * Rolling Trend Analysis with custom moving average windows.
  * Growth rate calculations and period-over-period percentage change graphs.

---

## 🚀 How to Run

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Launch the app** using the provided script:
   ```bash
   bash scripts/run_streamlit.sh
   ```
   *(Or run directly: `streamlit run app/dashboard.py`)*
3. **Open in browser**: The dashboard will open automatically at `http://localhost:8501`.

---

## 📂 File Architecture

* [app/dashboard.py](file:///d:/College/Secondary/Projects/IndianPulse/app/dashboard.py): Main Streamlit application file (UI widgets, layout, and chart rendering).
* [backend/data_processor.py](file:///d:/College/Secondary/Projects/IndianPulse/backend/data_processor.py): Core data calculation engine.
* [data/](file:///d:/College/Secondary/Projects/IndianPulse/data): Directory containing base indicator CSVs.
* [scripts/run_streamlit.sh](file:///d:/College/Secondary/Projects/IndianPulse/scripts/run_streamlit.sh): Bash launcher script.
