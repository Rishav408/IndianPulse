# 🇮🇳 IndianPulse — India Economic Dashboard

A modern, full-stack economic data visualization platform for India. Features 11 key economic indicators spanning 15+ years, with interactive charts, multi-country comparison, and correlation analysis.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-black?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

---

## 📁 Project Structure

```
IndianPulse/
├── api_server.py               # 🌐 Flask REST API Server
├── requirements.txt            # 📦 All Python dependencies
├── README.md                   # 📖 This file
│
├── frontend/                   # 🎨 Custom Web Frontend (HTML/CSS/JS)
│   ├── index.html              # Landing page
│   ├── dashboard.html          # Interactive dashboard (Chart.js)
│   ├── analytics.html          # Advanced analytics & correlation
│   ├── comparison.html         # Country vs Country comparison
│   └── data-analysis.svg       # UI asset
│
├── app/                        # ⚡ Streamlit Alternative Dashboard
│   ├── dashboard.py            # Streamlit app entry point
│   └── requirements-dashboard.txt
│
├── backend/                    # 🧠 Data Processing Engine
│   ├── data_processor.py       # Core ETL pipeline (Pandas)
│   └── country_comparison.py   # World Bank API integration
│
├── data/                       # 📊 Unified Data Store
│   ├── *.csv                   # 11 base economic indicator CSVs
│   ├── comparisons/            # Country comparison output CSVs
│   └── country_cache/          # Cached World Bank API responses
│
├── docs/                       # 📚 Documentation
│   ├── ARCHITECTURE.md         # System architecture & data flow
│   ├── COMPARISON_GUIDE.md     # Country comparison API reference
│   ├── STREAMLIT_GUIDE.md      # Streamlit dashboard usage guide
│   └── DVP PROJECT REPORT.docx # Full project report
│
├── scripts/                    # 🚀 Launchers & Utilities
│   ├── start_web_app.sh        # Start Flask Web App (Bash)
│   ├── run_streamlit.sh        # Start Streamlit Dashboard (Bash)
│   └── verify_project.py       # Health check script (Python)
│
└── utils/                      # 🔧 Data Generation Utilities
    ├── generate_csv_data.py    # Generate base indicator CSVs
    └── generate_comparison_data.py  # Generate country comparison CSVs
```

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **pip**

### 1. Clone & Install
```bash
git clone <repository-url>
cd IndianPulse
pip install -r requirements.txt
```

### 2. Generate Data (first time only)
```bash
# Generate the 11 base indicator CSVs
python utils/generate_csv_data.py

# (Optional) Generate country comparison datasets
python utils/generate_comparison_data.py
```

### 3. Launch

**Option A — Web Application (Flask + HTML/JS Dashboard)**
```bash
python api_server.py
# Open: http://localhost:5000
```

**Option B — Streamlit Dashboard (Python-only)**
```bash
streamlit run app/dashboard.py
# Open: http://localhost:8501
```

### 4. Verify Everything is Working
```bash
python scripts/verify_project.py
```

---

## 🌐 Web Application Pages

| URL | Page |
|:----|:-----|
| `http://localhost:5000` | 🏠 Landing Page |
| `http://localhost:5000/dashboard` | 📊 Main Dashboard |
| `http://localhost:5000/analytics` | 📈 Advanced Analytics |
| `http://localhost:5000/comparison.html` | 🌍 Country Comparison |

---

## 📊 Economic Indicators

| Indicator | Frequency | Source | Unit |
|:----------|:----------|:-------|:-----|
| GDP Growth Rate | Quarterly | RBI | % |
| Consumer Price Index | Monthly | MOSPI | Index / % |
| GST Collections | Monthly | CBIC | ₹ Crores |
| Unemployment Rate | Monthly | CMIE | % |
| Foreign Exchange Reserves | Monthly | RBI | USD Billion |
| Index of Industrial Production (IIP) | Monthly | MOSPI | % YoY |
| Repo Rate | Monthly | RBI | % |
| Trade Balance | Monthly | DGCI&S | USD Billion |
| Financial Inclusion Index | Annual | RBI | Index |
| Digital Payment Volume (UPI) | Monthly | NPCI | Million / ₹ Crores |
| Composite Leading Indicator | Quarterly | OECD | Index |

---

## 🛠️ Tech Stack

### Web Frontend
- **HTML5 + CSS3** with Tailwind CSS utility classes
- **Chart.js** — Interactive line, bar, area, and radar charts
- **AOS** — Smooth scroll animations
- **Font Awesome** — Icons

### Backend REST API
- **Flask** — Lightweight Python web framework
- **Flask-CORS** — Cross-origin resource sharing
- **Pandas + NumPy** — Data processing and statistical calculations

### Streamlit Dashboard (Alternative)
- **Streamlit** — Python-first dashboard framework
- **Plotly** — Interactive charting library

---

## 📚 Documentation

| Document | Description |
|:---------|:------------|
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | System architecture, data flow diagrams, and chart types |
| [COMPARISON_GUIDE.md](docs/COMPARISON_GUIDE.md) | Country comparison feature API reference |
| [STREAMLIT_GUIDE.md](docs/STREAMLIT_GUIDE.md) | Streamlit dashboard usage guide |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "Add amazing feature"`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## ⚠️ Disclaimer

This project uses **synthetic/sample data** inspired by real Indian economic indicators (RBI, MOSPI, CBIC, CMIE, NPCI, OECD). Data should not be used for real financial or policy decision-making.

---

**Built with ❤️ for India's economic data visualization**
