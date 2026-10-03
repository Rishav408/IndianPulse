# IndianPulse — India Economic Dashboard

An open-source platform for exploring 11 key Indian economic indicators over 15+ years, with interactive charts, cross-country comparison via the World Bank API, and correlation analytics.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.3%2B-black?logo=flask)](https://flask.palletsprojects.com/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28%2B-red?logo=streamlit)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/pandas-2.0%2B-150458?logo=pandas)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)

> **Note on data:** this project ships with synthetic/sample CSVs inspired by RBI, MOSPI, CBIC, CMIE, NPCI and OECD series for demo and education. Do not use for financial or policy decisions.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Data and Indicators](#data-and-indicators)
- [Testing and Health Check](#testing-and-health-check)
- [Documentation](#documentation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **11 indicators:** GDP growth, CPI/inflation, GST, unemployment, forex reserves, IIP, repo rate, trade balance, financial inclusion, digital payments (UPI), composite leading indicator.
- **Two frontends, one backend:**
  - Flask + HTML/CSS/JS (`frontend/`) with Chart.js dashboards, analytics and country-comparison pages.
  - Streamlit + Plotly alternative (`app/dashboard.py`) for a pure-Python workflow.
- **REST API** for indicators, filtered time series, statistics, correlation matrix and summary (`api_server.py`).
- **Country comparison** against 10 major economies (IND, CHN, USA, GBR, JPN, DEU, BRA, RUS, ZAF, AUS) using World Bank indicators with local CSV caching (`backend/country_comparison.py`).
- **Reproducible data layer:** checked-in CSVs in `data/` plus generators in `utils/` and verification in `scripts/verify_project.py`.

## Tech Stack

| Layer | Technologies |
| ----- | ------------ |
| Frontend (web) | HTML5, CSS3 + Tailwind CSS, JavaScript, Chart.js, AOS, Font Awesome |
| Frontend (alt) | Streamlit, Plotly |
| Backend API | Flask, Flask-CORS, Pandas, NumPy, Requests |
| Analysis | SciPy, Statsmodels, Matplotlib, Seaborn |
| Data sources | Local CSVs, World Bank v2 API (cached to `data/country_cache/`) |

See `requirements.txt` and `app/requirements-dashboard.txt` for version floors. Python 3.10+ is required.

## Project Structure

```text
IndianPulse/
├── api_server.py              # Flask REST API + static frontend server
├── requirements.txt           # Shared Python dependencies
├── .gitignore                 # Python, venv, editor ignores
├── frontend/                  # Web UI served by Flask
│   ├── index.html             # Landing page (GET /)
│   ├── dashboard.html         # Main dashboard (GET /dashboard)
│   ├── analytics.html         # Correlation / advanced analytics (GET /analytics.html)
│   ├── comparison.html        # Country comparison (GET /comparison.html)
│   └── data-analysis.svg
├── app/
│   ├── dashboard.py           # Streamlit dashboard (streamlit run app/dashboard.py)
│   └── requirements-dashboard.txt
├── backend/
│   ├── data_processor.py      # EconomicDataProcessor: loads 11 CSVs, stats, correlation
│   └── country_comparison.py  # CountryComparison: World Bank fetch + cache + rankings
├── data/
│   ├── *.csv                  # 11 base indicator tables
│   ├── comparisons/           # Pre-generated India-vs-world tables
│   └── country_cache/         # World Bank API response cache
├── utils/
│   ├── generate_csv_data.py         # Regenerate base indicator CSVs
│   └── generate_comparison_data.py  # Regenerate comparison CSVs
├── scripts/
│   ├── start_web_app.sh       # Launch Flask app
│   ├── run_streamlit.sh       # Launch Streamlit app
│   └── verify_project.py      # Dependency + data + module health check
└── docs/
    ├── ARCHITECTURE.md
    ├── COMPARISON_GUIDE.md
    ├── STREAMLIT_GUIDE.md
    └── DVP PROJECT REPORT.docx
```

## Getting Started

### Prerequisites

- Python 3.10+
- `pip` and (recommended) `venv`
- Git + a modern browser

### Installation

```bash
git clone https://github.com/Rishav408/IndianPulse.git
cd IndianPulse

# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
```

First-time data setup (regenerates the sample CSVs if needed):

```bash
python utils/generate_csv_data.py
python utils/generate_comparison_data.py  # optional
```

Verify the install:

```bash
python scripts/verify_project.py
```

You should see `RESULT: ALL HEALTH CHECKS PASSED!` with 11 datasets and 4 frontend files found.

## Usage

### Option A — Flask web app

```bash
python api_server.py
```

Open:

- `http://localhost:5000/` — landing page
- `http://localhost:5000/dashboard` — main dashboard
- `http://localhost:5000/analytics.html` — analytics and correlation
- `http://localhost:5000/comparison.html` — country comparison

Or via script:

```bash
bash scripts/start_web_app.sh
```

### Option B — Streamlit dashboard

```bash
streamlit run app/dashboard.py
# http://localhost:8501
```

Or via script:

```bash
bash scripts/run_streamlit.sh
```

## API Reference

Base URL (local): `http://localhost:5000`

### Core data

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/indicators` | List 11 supported indicators with units and categories |
| GET | `/api/data/<indicator>` | Time series for `gdp`, `cpi`, `gst`, `unemployment`, `forex`, `iip`, `repo_rate`, `trade`, `financial_inclusion`, `digital_payment`, `cli` |
| GET | `/api/statistics/<indicator>` | Mean, median, std, min/max, latest, growth rate |
| GET | `/api/correlation` | Correlation matrix across core indicators |
| GET | `/api/summary` | Latest value, change and growth per indicator |
| GET | `/api/health` | `status`, loaded `datasets` count, `timestamp` |

Filtered example:

```bash
curl "http://localhost:5000/api/data/cpi?start_date=2020-01-01&end_date=2024-12-31&region=Urban"
curl "http://localhost:5000/api/data/unemployment?state=Maharashtra"
curl "http://localhost:5000/api/statistics/gdp"
```

### Country comparison

Supported `indicator` keys: `gdp_growth`, `gdp_per_capita`, `inflation`, `unemployment`, `exports`, `imports`, `fdi`, `trade_gdp`.

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | `/api/comparison/countries` | 10 comparable countries with code, flag and color |
| GET | `/api/comparison/<indicator>?countries=IND,CHN,USA&start_year=2010&end_year=2024` | Time series + rankings, India position included |
| GET | `/api/comparison/relative/<indicator>?base=IND&countries=CHN,USA,GBR` | India-baselined (100) relative comparison |
| GET | `/api/comparison/multi-indicator?countries=IND,CHN,USA` | Multi-indicator snapshot for radar charts |
| GET | `/api/comparison/rankings/<indicator>` | Rankings only + India position |
| GET | `/api/comparison/export` | Regenerate `data/comparisons/` exports |

Example:

```bash
curl "http://localhost:5000/api/comparison/gdp_growth?countries=IND,CHN,USA,DEU&start_year=2015&end_year=2024"
```

Full request/response shapes are documented in [`docs/COMPARISON_GUIDE.md`](docs/COMPARISON_GUIDE.md) and the system flow in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

## Data and Indicators

| Indicator (`/api/data/<id>`) | Frequency | Source (inspired) | Notes / filters |
| ----------------------------- | --------- | ----------------- | --------------- |
| `gdp` — GDP Growth Rate | Quarterly | RBI | `Quarter`, `%` |
| `cpi` — Consumer Price Index | Monthly | MOSPI | `?region=Urban\|Rural`, CPI + inflation % |
| `gst` — GST Collections | Monthly | CBIC | ₹ Crores |
| `unemployment` — Unemployment Rate | Monthly | CMIE | `?state=`, `%` |
| `forex` — Forex Reserves | Monthly | RBI | USD Billion |
| `iip` — Index of Industrial Production | Monthly | MOSPI | % YoY |
| `repo_rate` — Repo Rate | Monthly | RBI | `%` |
| `trade` — Trade Balance | Monthly | DGCI&S | Exports / imports / balance, USD Billion |
| `financial_inclusion` — Financial Inclusion Index | Annual | RBI | Index |
| `digital_payment` — Digital Payment Volume | Monthly | NPCI | Volume (Mn), value (₹ Cr), `Payment_Mode` |
| `cli` — Composite Leading Indicator | Quarterly | OECD | `Quarter`, index |

Country-comparison values are fetched from the World Bank v2 API and cached under `data/country_cache/<INDICATOR>_<COUNTRIES>_<YEARS>.csv` to avoid repeated network calls.

## Testing and Health Check

```bash
python scripts/verify_project.py
```

Checks:

1. Python version and core (`flask`, `flask_cors`, `pandas`, `numpy`, `requests`) vs optional (`streamlit`, `plotly`) deps.
2. 11 CSVs present in `data/`.
3. `EconomicDataProcessor` loads 11 datasets.
4. `CountryComparison.get_comparison_data('gdp_growth', ...)` returns data.
5. All 4 `frontend/*.html` files exist.

There is no automated test suite yet — contributions adding `pytest` coverage for `backend/` and API smoke tests are welcome (see Roadmap).

## Documentation

- [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) — layers, REST contracts and data-flow diagrams.
- [`docs/COMPARISON_GUIDE.md`](docs/COMPARISON_GUIDE.md) — country-comparison API reference.
- [`docs/STREAMLIT_GUIDE.md`](docs/STREAMLIT_GUIDE.md) — Streamlit usage.
- [`docs/DVP PROJECT REPORT.docx`](docs/DVP%20PROJECT%20REPORT.docx) — full academic project report.

## Roadmap

- [ ] Pin dependencies (`requirements.lock`), add `Dockerfile` and CI (`pytest` + `ruff`).
- [ ] Replace `debug=True` dev server with Gunicorn config and scoped CORS + rate limits.
- [ ] Add forecasting (ARIMA/Prophet) and PDF/PNG export endpoints.
- [ ] Add live ingestion for RBI/MOSPI series with data validation and `last_updated` metadata.
- [ ] Consolidate frontend charting and add saved views, i18n and PWA support.

## Contributing

Contributions are welcome! Please:

1. Fork the repo and create a branch: `git checkout -b feature/<short-name>`
2. Set up the environment and run `python scripts/verify_project.py`
3. Make focused commits with [Conventional Commits](https://www.conventionalcommits.org/) messages
4. Open a pull request describing behavior, screenshots for UI changes, and verification steps

Good first issues: adding `pytest` tests, tightening API validation/pagination, improving mobile layout.

## License

This project is released under the MIT License — see [`LICENSE`](LICENSE) for details. If `LICENSE` is missing in your checkout, please open an issue.

## Acknowledgements

- Data inspiration: RBI, MOSPI, CBIC, CMIE, DGCI&S, NPCI, OECD and the World Bank API.
- Built with Flask, Streamlit, Pandas, Plotly and Chart.js.
