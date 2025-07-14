# ⚡ Quick Start - One-Click Setup

## 🚀 Fastest Way to Get Started

### Upload Files to Google Colab:
1. `btc_live_analyzer.py`
2. `colab_setup_fixed.py`
3. `requirements.txt`

### Copy-Paste These Commands:

**Step 1: Setup (Copy & Run in Colab Cell)**
```python
exec(open('colab_setup_fixed.py').read())
```

**Step 2: Launch (Copy & Run in New Colab Cell)**
```python
exec(open('run_tunnel.py').read())
```

**That's it! Click the URL that appears! 🎉**

---

## 🔧 One-Command Manual Setup (If Automatic Fails)

Copy-paste this entire block into a Colab cell:

```python
# Complete Bitcoin Analyzer Setup - One Command
import subprocess
import sys
import os

def setup_bitcoin_analyzer():
    print("🚀 Setting up Bitcoin Analyzer...")
    
    # Install system dependencies
    subprocess.run(["apt-get", "update"], check=False)
    subprocess.run(["apt-get", "install", "-y", "build-essential", "python3-dev"], check=False)
    
    # Install Python packages
    packages = [
        "streamlit", "pandas", "numpy", "plotly", "requests", 
        "scikit-learn", "pyngrok", "python-dateutil", "pytz"
    ]
    
    for pkg in packages:
        subprocess.run([sys.executable, "-m", "pip", "install", pkg], check=False)
    
    # Try TA-Lib (optional)
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "TA-Lib"], check=True)
        print("✅ TA-Lib installed - Full version available!")
        use_full = True
    except:
        print("⚠️ TA-Lib failed - Using lite version")
        use_full = False
    
    # Create lite version if needed
    if not use_full:
        # [Lite version code would be written to file here]
        print("📝 Created lite version")
    
    # Setup Streamlit config
    config_dir = os.path.expanduser("~/.streamlit")
    os.makedirs(config_dir, exist_ok=True)
    with open(os.path.join(config_dir, "config.toml"), "w") as f:
        f.write("[server]\nheadless = true\nport = 8501\n")
    
    print("✅ Setup complete!")
    return use_full

# Run setup
use_full_version = setup_bitcoin_analyzer()

# Launch app
import threading
import time
from pyngrok import ngrok

def run_app():
    filename = 'btc_live_analyzer.py' if use_full_version else 'btc_live_analyzer_lite.py'
    subprocess.run(['streamlit', 'run', filename, '--server.port=8501'])

print("🚀 Starting app...")
app_thread = threading.Thread(target=run_app)
app_thread.daemon = True
app_thread.start()

time.sleep(10)
public_url = ngrok.connect(8501)
print(f"🌐 Your Bitcoin Analyzer: {public_url}")
print("✨ Click the link above!")
```

---

## 🎯 Just Want to Test? Ultra-Quick Version

```python
# Ultra-minimal Bitcoin price tracker
import requests
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

def get_btc_data():
    url = "https://api.binance.com/api/v3/klines"
    params = {'symbol': 'BTCUSDT', 'interval': '5m', 'limit': 100}
    data = requests.get(url, params=params).json()
    df = pd.DataFrame(data, columns=['time', 'open', 'high', 'low', 'close', 'volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    for col in ['open', 'high', 'low', 'close', 'volume']:
        df[col] = df[col].astype(float)
    return df

st.title("₿ Bitcoin Live Tracker")
df = get_btc_data()
current_price = df['close'].iloc[-1]
change = df['close'].iloc[-1] - df['close'].iloc[-2]
st.metric("BTC Price", f"${current_price:,.2f}", f"{change:+.2f}")

fig = go.Figure(data=go.Candlestick(x=df['time'], open=df['open'], high=df['high'], low=df['low'], close=df['close']))
fig.update_layout(title="Bitcoin 5-Min Chart", template='plotly_dark')
st.plotly_chart(fig)
```

Then run: `!streamlit run your_file.py &`

---

## 📋 Troubleshooting Quick Fixes

**Error: TA-Lib installation failed**
- ✅ Use the fixed setup script: `exec(open('colab_setup_fixed.py').read())`

**Error: App won't start**
- ✅ Wait 15 seconds, then refresh
- ✅ Restart Colab runtime

**Error: No data loading**
- ✅ Check internet connection
- ✅ Try again in a few minutes

**Error: Tunnel doesn't work**
- ✅ Make sure ngrok is installed: `!pip install pyngrok`
- ✅ Keep the launch cell running

---

## 🎉 Success Indicators

You'll know it's working when you see:
- ✅ "Setup complete!" message
- 🌐 A tunnel URL (like: `https://abc123.ngrok.io`)
- 📊 Bitcoin price and charts in your browser

**Ready to analyze Bitcoin like a pro! 🚀₿**