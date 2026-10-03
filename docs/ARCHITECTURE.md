# IndianPulse - End-to-End Architecture

This document outlines the architecture, components, and data flow of the India Economic Dashboard application.

---

## 🏗️ Architectural Layers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  USER INTERFACE LAYER (frontend/ & app/)                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Option A: Web Frontend]                     [Option B: Streamlit App]     │
│   - HTML5, CSS3 (Tailwind CSS)                 - Native Streamlit           │
│   - Chart.js (interactive graphs)              - Plotly (interactive graphs)│
│   - AOS Scroll animations                      - Python widgets & layouts   │
│                                                                             │
└──────────────────────────────┬───────────────────────────────┬──────────────┘
                               │                               │
                      HTTP REST requests             Direct Python Imports
                               ▼                               │
┌──────────────────────────────┴───────────────────────────────┐               
│  API LAYER (api_server.py)                                   │               
├──────────────────────────────────────────────────────────────┤               
│                                                              │               
│  Flask REST API serving:                                     │               
│   - /api/indicators, /api/data/<id>, /api/statistics/<id>    │               
│   - /api/correlation, /api/comparison/<id>                   │               
│                                                              │               
└──────────────────────────────┬───────────────────────────────┘               
                               │                               │
                               ▼                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  DATA PROCESSING LAYER (backend/data_processor.py & country_comparison.py)  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  EconomicDataProcessor & CountryComparison classes using Pandas and NumPy   │
│  for data transformation, normalization, correlation & caching.             │
│                                                                             │
└──────────────────────────────┬──────────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  DATA STORAGE LAYER (data/)                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  - 11 CSV files for base economic indicators                                │
│  - data/comparisons/ containing country comparison CSVs                      │
│  - data/country_cache/ containing cached World Bank API JSON/CSVs            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🔄 Data Flow Example: Loading Correlation Matrix

1. **User Interaction**: User opens the Analytics page on the Web Frontend.
2. **Event Trigger**: The browser fires `DOMContentLoaded`, running the JavaScript event handler.
3. **API Request**: The script triggers `loadCorrelationMatrix()`, sending an HTTP request: `fetch('/api/correlation')`.
4. **API Routing**: `api_server.py` captures the request and executes `processor.get_correlation_matrix()`.
5. **Data Engine**: The backend processor merges all 11 CSV datasets on their matching `Date` index and computes the Pearson correlation matrix using `pandas.DataFrame.corr()`.
6. **API Response**: The server returns a JSON object containing indicator names and correlation values: `{ "indicators": [...], "matrix": [[...]] }`.
7. **UI Rendering**: The frontend JavaScript parses the JSON, maps the values into colors, dynamically builds the HTML table, and renders it in the `#correlation-matrix` container.

---

## 📈 Visualizations and Calculations

### Chart Types Used

| Chart Type | Used For | Implementation |
| :--- | :--- | :--- |
| **Line Chart** | Multi-Indicator Comparison, trends over time. | Chart.js / Plotly |
| **Area Chart** | Cumulative values over time (e.g. GDP, GST). | Chart.js / Plotly |
| **Horizontal Bar** | Growth Trends, sorted comparison values. | Chart.js / Plotly |
| **Doughnut / Pie** | Distribution metrics. | Chart.js |
| **Radar Chart** | Multi-indicator country comparisons. | Chart.js |
| **Heatmap Table** | Correlation Matrix visualization. | HTML + CSS / Plotly |

### Core Mathematical Calculations

* **Z-Score Normalization** (for comparing different units like GDP % and Forex Reserves USD):
  $$z = \frac{x - \mu}{\sigma}$$
  *Where $x$ is the value, $\mu$ is the mean, and $\sigma$ is the standard deviation.*
* **Period-over-Period Growth Rate**:
  $$\text{growth} = \frac{\text{latest} - \text{first}}{\text{first}} \times 100$$
* **Pearson Correlation Coefficient**: Used to measure linear correlation between different economic metrics, ranging from $-1$ (perfect negative correlation) to $+1$ (perfect positive correlation).

---

## ⚡ Performance Optimizations

1. **Parallel Execution**: Web frontend loads dashboard resources concurrently using `Promise.all()` to resolve separate API queries without blocking.
2. **Chart Recycling**: Before drawing a new canvas, existing Chart.js instances are destroyed to prevent memory leaks and overlapping canvas glitches.
3. **Aggressive Caching**: World Bank API responses are cached in `data/country_cache/` to speed up country comparisons and prevent rate-limiting.
4. **Data Aggregation**: Multiple records per date are resolved efficiently on the backend using Pandas aggregation functions rather than JavaScript parsing loops.
