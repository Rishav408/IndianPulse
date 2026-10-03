# 🌍 Country Comparison Guide - IndianPulse

The Country Comparison feature allows you to compare India's economic performance with major world economies including China, USA, UK, Japan, Germany, Brazil, Russia, South Africa, and Australia.

---

## 🚀 Key Features

1. **Multi-Country Comparison**: Compare India with up to 10 major economies simultaneously over a 15+ year time horizon (2010-2024).
2. **Key Indicators**: 
   * **GDP Growth**: Annual GDP growth rate (%)
   * **Inflation**: Consumer price inflation (%)
   * **Unemployment**: Total unemployment rate (%)
   * **Trade**: Trade as % of GDP (%)
   * **Exports**: Exports as % of GDP (%)
   * **Imports**: Imports as % of GDP (%)
   * **FDI**: Foreign Direct Investment (USD)
   * **GDP per Capita**: GDP per capita (Current US$)
3. **Advanced Visualizations**:
   * **Trend Line Charts**: Multi-line historical trends.
   * **Bar Charts**: Sorted latest-value comparison.
   * **Radar Spider Charts**: Relative performance across all indicators.
   * **Dynamic Rankings**: Global rankings by indicator (highlighting India's rank).

---

## 📡 API Endpoints

### 1. Get Available Countries
```http
GET /api/comparison/countries
```
Returns a list of all available countries with their codes, names, flags, and color hexes.

### 2. Get Comparison Data
```http
GET /api/comparison/{indicator}?countries=IND,CHN,USA&start_year=2010&end_year=2024
```
**Parameters:**
* `indicator`: One of `gdp_growth`, `inflation`, `unemployment`, `trade_gdp`, `exports`, `imports`, `fdi`, `gdp_per_capita`.
* `countries`: Comma-separated country codes (default: `IND,CHN,USA,GBR,JPN,DEU`).
* `start_year` & `end_year`: Year range parameters.

### 3. Get Relative Comparison (India = 100)
```http
GET /api/comparison/relative/{indicator}?base=IND&countries=CHN,USA
```

### 4. Get Multi-Indicator Comparison (Radar Charts)
```http
GET /api/comparison/multi-indicator?countries=IND,CHN,USA,GBR,JPN
```

---

## 📊 Data Cache and Generation

### World Bank API Integration
The module automatically attempts to fetch real-time data from the World Bank API, caching it locally in `data/country_cache/` to speed up performance and bypass rate limits.

### Synthetic Data Fallback
If the World Bank API is unreachable, or if you run the manual generator, a fallback synthetic data generator is available. To generate this offline data:
```bash
python3 utils/generate_comparison_data.py
```
This writes comparison CSV files directly to `data/comparisons/` for offline/fallback usage.
