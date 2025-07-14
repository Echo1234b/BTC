# ₿ Bitcoin Live Analyzer & Predictor

<div align="center">

![Bitcoin](https://img.shields.io/badge/Bitcoin-Analysis-orange?style=for-the-badge&logo=bitcoin)
![Python](https://img.shields.io/badge/Python-3.7+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit)
![ML](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**🚀 Real-time Bitcoin analysis with machine learning predictions**

[🎯 Quick Start](#-quick-start) • [📊 Features](#-features) • [🔧 Installation](#-installation) • [📱 Demo](#-demo) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 **Quick Start**

**For Google Colab (Recommended):**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/bitcoin-live-analyzer/blob/main/examples/Bitcoin_Analyzer_Demo.ipynb)

```python
# 1. Upload files to Colab
# 2. Run setup
exec(open('colab_setup_fixed.py').read())

# 3. Launch app
exec(open('run_tunnel.py').read())
```

**For Local Installation:**
```bash
git clone https://github.com/yourusername/bitcoin-live-analyzer.git
cd bitcoin-live-analyzer
pip install -r requirements.txt
streamlit run btc_live_analyzer_fixed.py
```

## 📊 **Features**

### 🔮 **Machine Learning Predictions**
- **Next candle direction** prediction using ensemble models
- **Gradient Boosting + Random Forest** approach
- **Real-time model retraining** with latest data
- **Accuracy tracking** and confidence scoring

### 📈 **Technical Analysis**
- **17+ Technical Indicators** (with TA-Lib) or basic fallback
- **Moving Averages**: SMA 20/50, EMA 12/26
- **Momentum**: RSI, Stochastic, Williams %R
- **Trend**: MACD, ADX, Bollinger Bands
- **Volume Analysis**: Volume SMA, A/D Line, OBV
- **Candlestick Patterns**: Doji, Hammer, Engulfing

### 🎯 **Professional Dashboard**
- **Real-time Bitcoin data** from Binance API
- **Interactive candlestick charts** with Plotly
- **Auto-refresh** with configurable intervals
- **Bitcoin-themed design** with professional styling
- **Mobile-responsive** interface

### 🔍 **Market Analysis**
- **Trend identification** using moving averages
- **Volume ratio analysis** vs historical averages
- **Support/Resistance levels** from Bollinger Bands
- **Market condition indicators** (overbought/oversold)
- **Volatility metrics** and risk assessment

## 🔧 **Installation**

### **Prerequisites**
- Python 3.7+
- Internet connection for live data
- Modern web browser

### **Option 1: Google Colab (Easiest)**
1. Open the [Colab notebook](https://colab.research.google.com/github/yourusername/bitcoin-live-analyzer/blob/main/examples/Bitcoin_Analyzer_Demo.ipynb)
2. Run the setup cells
3. Access via the provided tunnel URL

### **Option 2: Local Installation**
```bash
# Clone repository
git clone https://github.com/yourusername/bitcoin-live-analyzer.git
cd bitcoin-live-analyzer

# Install dependencies
pip install -r requirements.txt

# Optional: Install TA-Lib for full features
# On Ubuntu/Debian:
sudo apt-get install build-essential
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
cd ..
pip install TA-Lib

# Run application
streamlit run btc_live_analyzer_fixed.py
```

### **Option 3: Docker (Coming Soon)**
```bash
docker run -p 8501:8501 bitcoin-analyzer:latest
```

## 📱 **Demo**

### **Live Dashboard**
![Dashboard Screenshot](https://via.placeholder.com/800x400/1e3c72/ffffff?text=Bitcoin+Live+Dashboard)

### **Prediction System**
![Prediction Screenshot](https://via.placeholder.com/400x300/667eea/ffffff?text=ML+Predictions)

### **Technical Analysis**
![Analysis Screenshot](https://via.placeholder.com/400x300/f7931a/ffffff?text=Technical+Indicators)

## 🛠️ **Technical Specifications**

### **Data Source**
- **API**: Binance REST API (public endpoints)
- **Symbol**: BTC/USDT
- **Timeframe**: 5-minute candles
- **Update Frequency**: Configurable (10-300 seconds)

### **Machine Learning**
- **Models**: Gradient Boosting + Random Forest ensemble
- **Features**: 17+ technical indicators
- **Target**: Next candle direction (binary classification)
- **Training**: 80/20 split with stratification
- **Scaling**: StandardScaler normalization

### **Performance**
- **Memory Usage**: ~200MB
- **CPU Usage**: Low (optimized for real-time)
- **Latency**: <2 seconds for predictions
- **Accuracy**: Typically 55-65% (varies with market conditions)

## 📋 **Requirements**

```
streamlit>=1.31.0
pandas>=2.0.3
numpy>=1.24.3
plotly>=5.17.0
requests>=2.31.0
scikit-learn>=1.3.0
TA-Lib>=0.4.28  # Optional but recommended
joblib>=1.3.2
python-dateutil>=2.8.2
pytz>=2023.3
```

## 🚨 **Important Disclaimers**

- **⚠️ Educational Purpose Only**: This tool is for learning and research
- **📈 Not Financial Advice**: Do not use predictions for actual trading
- **💰 Risk Warning**: Cryptocurrency trading involves substantial risk
- **🎯 No Guarantees**: Predictions are not guaranteed to be accurate

## 🔧 **Troubleshooting**

### **Common Issues**

**TA-Lib Installation Failed**
- ✅ Use `btc_live_analyzer_fixed.py` - handles missing TA-Lib automatically
- ✅ Fallback to basic indicators (still powerful)

**App Won't Start**
- ✅ Check Python version (3.7+ required)
- ✅ Verify all dependencies installed
- ✅ Ensure port 8501 is available

**No Data Loading**
- ✅ Check internet connection
- ✅ Verify Binance API accessibility
- ✅ Try different data limits in sidebar

**Predictions Not Working**
- ✅ Wait for sufficient data (>50 candles)
- ✅ Click "Retrain Model" in sidebar
- ✅ Check model accuracy display

See [Troubleshooting Guide](docs/TROUBLESHOOTING.md) for more solutions.

## 📚 **Documentation**

- 📖 [Installation Guide](docs/COLAB_INSTALLATION_GUIDE.md)
- ⚡ [Quick Start](docs/QUICK_START.md)
- 📁 [File Overview](docs/FILES_SUMMARY.md)
- 🔧 [Troubleshooting](docs/TROUBLESHOOTING.md)

## 🤝 **Contributing**

We welcome contributions! Here's how to help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### **Areas for Contribution**
- 🔮 **New ML models** and prediction algorithms
- 📊 **Additional technical indicators**
- 🎨 **UI/UX improvements**
- 📱 **Mobile optimization**
- 🔧 **Performance enhancements**
- 📚 **Documentation improvements**

## 📊 **Project Stats**

![GitHub stars](https://img.shields.io/github/stars/yourusername/bitcoin-live-analyzer?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/bitcoin-live-analyzer?style=social)
![GitHub issues](https://img.shields.io/github/issues/yourusername/bitcoin-live-analyzer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/yourusername/bitcoin-live-analyzer)

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 **Acknowledgments**

- **Binance** for providing free cryptocurrency data API
- **TA-Lib** for technical analysis indicators
- **Streamlit** for the amazing dashboard framework
- **Plotly** for interactive charts
- **scikit-learn** for machine learning capabilities

## 🔗 **Links**

- 🌐 **Live Demo**: [Try it on Colab](https://colab.research.google.com/)
- 📧 **Contact**: [your.email@example.com](mailto:your.email@example.com)
- 🐦 **Twitter**: [@yourusername](https://twitter.com/yourusername)
- 💼 **LinkedIn**: [Your Name](https://linkedin.com/in/yourname)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ and ☕ for the crypto community

</div>