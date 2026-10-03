import sys
import os
import importlib

def main():
    print("=" * 60)
    print("INDIANPULSE PROJECT HEALTH CHECK")
    print("=" * 60)
    
    all_ok = True
    
    # 1. Python Version
    print("\n[1] Checking Python Version...")
    print(f"    Python {sys.version.split()[0]} - OK")
    
    # 2. Dependencies
    print("\n[2] Checking Core Dependencies (required for Flask Web App)...")
    core_deps = ["flask", "flask_cors", "pandas", "numpy", "requests"]
    for dep in core_deps:
        try:
            importlib.import_module(dep)
            print(f"    - {dep:<12}: Installed")
        except ImportError:
            print(f"    - {dep:<12}: MISSING")
            all_ok = False

    print("\n[2b] Checking Optional Dependencies (required for Streamlit Dashboard)...")
    optional_deps = ["streamlit", "plotly"]
    for dep in optional_deps:
        try:
            importlib.import_module(dep)
            print(f"    - {dep:<12}: Installed")
        except ImportError:
            print(f"    - {dep:<12}: Not installed (optional - needed only for Streamlit app)")
            
    # 3. Data Directory
    print("\n[3] Checking Data Directory...")
    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    if not os.path.exists(data_dir):
        print(f"    - data/ directory not found at {data_dir} - FAILED")
        all_ok = False
    else:
        csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
        print(f"    - Found {len(csv_files)} CSV files in data/")
        if len(csv_files) == 11:
            print("    - All 11 base data files present - OK")
        else:
            print("    - Expected 11 base data files - FAILED")
            all_ok = False
            
    # 4. Backend Data Processor
    print("\n[4] Checking Data Processor Module...")
    try:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
        from backend.data_processor import EconomicDataProcessor
        processor = EconomicDataProcessor()
        if len(processor.datasets) == 11:
            print("    - Successfully loaded 11 datasets - OK")
            for name, df in processor.datasets.items():
                print(f"      * {name:<20}: {len(df)} rows")
        else:
            print(f"    - Expected 11 datasets, got {len(processor.datasets)} - FAILED")
            all_ok = False
    except Exception as e:
        print(f"    - Data processor failed to load: {e} - FAILED")
        all_ok = False
        
    # 5. Country Comparison
    print("\n[5] Checking Country Comparison Module...")
    try:
        from backend.country_comparison import CountryComparison
        comparator = CountryComparison()
        data = comparator.get_comparison_data('gdp_growth', ['IND', 'CHN', 'USA'])
        if 'countries' in data and len(data['countries']) > 0:
            print("    - Country comparison loaded data successfully - OK")
        else:
            print("    - Failed to retrieve comparison data - FAILED")
            all_ok = False
    except Exception as e:
        print(f"    - Country comparison failed to load: {e} - FAILED")
        all_ok = False
        
    # 6. Web Frontend Files
    print("\n[6] Checking Web Frontend Assets...")
    frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend"))
    frontend_files = ["index.html", "dashboard.html", "analytics.html", "comparison.html"]
    for file in frontend_files:
        path = os.path.join(frontend_dir, file)
        if os.path.exists(path):
            print(f"    - frontend/{file:<15}: Found - OK")
        else:
            print(f"    - frontend/{file:<15}: MISSING - FAILED")
            all_ok = False
            
    # Summary
    print("\n" + "=" * 60)
    if all_ok:
        print("RESULT: ALL HEALTH CHECKS PASSED!")
        print("=" * 60)
        print("\nTo start the Flask Web Application:")
        print("   python api_server.py")
        print("\nTo start the Streamlit Dashboard:")
        print("   streamlit run app/dashboard.py")
    else:
        print("RESULT: SOME HEALTH CHECKS FAILED")
        print("=" * 60)
        print("Please check the missing dependencies or files listed above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
