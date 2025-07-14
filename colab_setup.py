"""
Bitcoin Live Analyzer & Predictor - Google Colab Setup Script

This script sets up the environment and runs the Bitcoin analyzer in Google Colab.
"""

import subprocess
import sys
import os

def install_packages():
    """Install required packages for the Bitcoin analyzer"""
    
    print("🔧 Installing system dependencies...")
    
    # Install TA-Lib dependencies
    subprocess.run([
        "apt-get", "update"
    ], check=True)
    
    subprocess.run([
        "apt-get", "install", "-y", "build-essential", "wget"
    ], check=True)
    
    # Download and install TA-Lib from source
    print("📥 Installing TA-Lib...")
    subprocess.run([
        "wget", "http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz"
    ], check=True)
    
    subprocess.run([
        "tar", "-xzf", "ta-lib-0.4.0-src.tar.gz"
    ], check=True)
    
    os.chdir("ta-lib/")
    subprocess.run(["./configure", "--prefix=/usr"], check=True)
    subprocess.run(["make"], check=True)
    subprocess.run(["make", "install"], check=True)
    os.chdir("..")
    
    # Install Python packages
    print("📦 Installing Python packages...")
    subprocess.run([
        sys.executable, "-m", "pip", "install", "--upgrade", "pip"
    ], check=True)
    
    packages = [
        "streamlit==1.31.0",
        "pandas==2.0.3",
        "numpy==1.24.3",
        "plotly==5.17.0",
        "requests==2.31.0",
        "scikit-learn==1.3.0",
        "TA-Lib==0.4.28",
        "joblib==1.3.2",
        "python-dateutil==2.8.2",
        "pytz==2023.3"
    ]
    
    for package in packages:
        subprocess.run([
            sys.executable, "-m", "pip", "install", package
        ], check=True)
    
    print("✅ All packages installed successfully!")

def setup_streamlit():
    """Set up Streamlit configuration for Colab"""
    
    print("⚙️ Setting up Streamlit configuration...")
    
    # Create Streamlit config directory
    config_dir = os.path.expanduser("~/.streamlit")
    os.makedirs(config_dir, exist_ok=True)
    
    # Create config file
    config_content = """
[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
"""
    
    with open(os.path.join(config_dir, "config.toml"), "w") as f:
        f.write(config_content)
    
    print("✅ Streamlit configuration complete!")

def run_app():
    """Run the Bitcoin analyzer app"""
    
    print("🚀 Starting Bitcoin Live Analyzer & Predictor...")
    print("📊 The app will be available at the tunnel URL provided below.")
    print("🔄 The app includes auto-refresh and real-time predictions.")
    print("⚡ Features:")
    print("   - Live Bitcoin price data from Binance")
    print("   - Technical indicators (RSI, MACD, Bollinger Bands, etc.)")
    print("   - Machine learning predictions for next candle direction")
    print("   - Professional dashboard with interactive charts")
    print("   - Real-time market analysis")
    
    # Install pyngrok for tunneling
    subprocess.run([
        sys.executable, "-m", "pip", "install", "pyngrok"
    ], check=True)
    
    # Create tunnel setup script
    tunnel_script = """
import subprocess
import time
from pyngrok import ngrok

# Start Streamlit in background
import threading
def run_streamlit():
    subprocess.run(['streamlit', 'run', 'btc_live_analyzer.py', '--server.port=8501'])

streamlit_thread = threading.Thread(target=run_streamlit)
streamlit_thread.daemon = True
streamlit_thread.start()

# Wait for Streamlit to start
time.sleep(10)

# Create tunnel
public_url = ngrok.connect(8501)
print(f"🌐 Bitcoin Analyzer is running at: {public_url}")
print("✨ Click the link above to access your Bitcoin Live Analyzer!")
print("🔔 Note: Keep this cell running to maintain the connection.")

# Keep the tunnel alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("🛑 Stopping the application...")
    ngrok.disconnect(public_url)
"""
    
    with open("run_tunnel.py", "w") as f:
        f.write(tunnel_script)
    
    print("\n🎯 To run the app, execute the following in a new cell:")
    print("exec(open('run_tunnel.py').read())")

if __name__ == "__main__":
    print("🚀 Bitcoin Live Analyzer & Predictor - Colab Setup")
    print("=" * 50)
    
    try:
        install_packages()
        setup_streamlit()
        run_app()
        
        print("\n✅ Setup complete!")
        print("🎉 Your Bitcoin analyzer is ready to use!")
        
    except Exception as e:
        print(f"❌ Error during setup: {str(e)}")
        print("🔧 Please check your internet connection and try again.")