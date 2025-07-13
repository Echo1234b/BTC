# 🚀 Google Colab Installation Guide

## Quick Setup Instructions

### 1. Upload Files to Colab
Upload these files to your Google Colab environment:
- `btc_live_analyzer.py`
- `colab_setup.py`
- `requirements.txt`

### 2. Install Dependencies
Run this in a Colab cell:
```python
# Setup Bitcoin Analyzer
exec(open('colab_setup.py').read())
```

### 3. Launch Application
Run this in a new Colab cell:
```python
# Launch the application
exec(open('run_tunnel.py').read())
```

### 4. Access Your App
- Click the tunnel URL that appears
- Your Bitcoin analyzer is now live!

## Manual Installation (Alternative)

If the automatic setup doesn't work, use these manual steps:

### Install System Dependencies
```bash
!apt-get update
!apt-get install -y build-essential wget
```

### Install TA-Lib
```bash
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzf ta-lib-0.4.0-src.tar.gz
%cd ta-lib/
!./configure --prefix=/usr
!make
!make install
%cd ..
```

### Install Python Packages
```bash
!pip install streamlit pandas numpy plotly requests scikit-learn TA-Lib joblib python-dateutil pytz pyngrok
```

### Create and Run App
```python
import subprocess
import threading
import time
from pyngrok import ngrok

def run_streamlit():
    subprocess.run(['streamlit', 'run', 'btc_live_analyzer.py', '--server.port=8501'])

streamlit_thread = threading.Thread(target=run_streamlit)
streamlit_thread.daemon = True
streamlit_thread.start()

time.sleep(10)

public_url = ngrok.connect(8501)
print(f"🌐 Bitcoin Analyzer: {public_url}")
```

## Features You'll Get

- 📊 **Real-time Bitcoin data** from Binance
- 🔮 **ML predictions** for next candle direction
- 📈 **Technical indicators** (RSI, MACD, Bollinger Bands)
- 🎯 **Professional dashboard** with auto-refresh
- 🔍 **Market analysis** with trend identification

## Important Notes

- Keep the tunnel cell running to maintain connection
- App updates automatically every 60 seconds (configurable)
- Use retrain model button to update predictions
- Educational purpose only - not financial advice

## Troubleshooting

**If setup fails:**
1. Restart Colab runtime
2. Try manual installation steps
3. Check internet connection

**If app doesn't load:**
1. Wait 10-15 seconds after launch
2. Refresh the tunnel URL
3. Check that all files are uploaded

**If predictions don't work:**
1. Click "Retrain Model" in sidebar
2. Ensure enough data is available
3. Check model accuracy display

## Ready to Start!

Your Bitcoin Live Analyzer is now ready to provide real-time market analysis and predictions. Enjoy exploring the cryptocurrency markets with professional-grade tools!

🚀 Happy Trading! ₿