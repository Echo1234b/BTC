# ₿ Bitcoin Live Analyzer & Predictor

A comprehensive real-time Bitcoin analysis and prediction system built for Google Colab with Streamlit interface.

## 🚀 Features

### 📊 Live Data & Visualization
- **Real-time Bitcoin price data** from Binance API
- **Interactive candlestick charts** with technical indicators
- **Professional dark theme** with Bitcoin-themed styling
- **Auto-refresh capability** with configurable intervals

### 🔮 Machine Learning Predictions
- **Next candle direction prediction** using ensemble ML models
- **Gradient Boosting + Random Forest** ensemble approach
- **Feature engineering** with 17+ technical indicators
- **Prediction confidence gauge** with visual feedback

### 📈 Technical Analysis
- **Moving Averages**: SMA 20, SMA 50, EMA 12, EMA 26
- **Momentum Indicators**: RSI, Stochastic, Williams %R
- **Trend Indicators**: MACD, ADX, Bollinger Bands
- **Volume Analysis**: Volume SMA, A/D Line, OBV
- **Candlestick Patterns**: Doji, Hammer, Engulfing

### 🔍 Market Analysis
- **Trend Analysis**: Current market trend identification
- **Volume Analysis**: Volume ratios and patterns
- **Support/Resistance**: Dynamic price levels
- **Volatility Metrics**: Real-time volatility tracking

## 🛠️ Installation & Setup

### Option 1: Quick Setup (Recommended)

1. **Open Google Colab**: [https://colab.research.google.com/](https://colab.research.google.com/)

2. **Upload the files** to your Colab environment:
   - `btc_live_analyzer.py`
   - `colab_setup.py`
   - `requirements.txt`

3. **Run the setup script**:
   ```python
   exec(open('colab_setup.py').read())
   ```

4. **Start the application**:
   ```python
   exec(open('run_tunnel.py').read())
   ```

### Option 2: Manual Installation

1. **Install system dependencies**:
   ```bash
   !apt-get update
   !apt-get install -y build-essential wget
   ```

2. **Install TA-Lib**:
   ```bash
   !wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
   !tar -xzf ta-lib-0.4.0-src.tar.gz
   %cd ta-lib/
   !./configure --prefix=/usr
   !make
   !make install
   %cd ..
   ```

3. **Install Python packages**:
   ```bash
   !pip install streamlit pandas numpy plotly requests scikit-learn TA-Lib joblib python-dateutil pytz pyngrok
   ```

4. **Run the application**:
   ```python
   import subprocess
   import threading
   from pyngrok import ngrok
   
   def run_streamlit():
       subprocess.run(['streamlit', 'run', 'btc_live_analyzer.py', '--server.port=8501'])
   
   streamlit_thread = threading.Thread(target=run_streamlit)
   streamlit_thread.daemon = True
   streamlit_thread.start()
   
   import time
   time.sleep(10)
   
   public_url = ngrok.connect(8501)
   print(f"🌐 Bitcoin Analyzer is running at: {public_url}")
   ```

## 📱 Usage Guide

### 🎯 Main Dashboard
- **Current Price**: Real-time BTC/USDT price with 24h change
- **Volume**: Trading volume metrics
- **Volatility**: Current market volatility

### 📊 Interactive Charts
- **Candlestick Chart**: OHLC data with technical indicators
- **Volume Chart**: Trading volume with color-coded bars
- **RSI Chart**: Relative Strength Index with overbought/oversold levels

### 🔮 Prediction System
- **Prediction Gauge**: Visual confidence meter for next candle direction
- **Model Accuracy**: Live display of prediction model performance
- **Retrain Model**: Button to retrain with latest data

### ⚙️ Configuration Options
- **Auto Refresh**: Toggle automatic data updates
- **Refresh Interval**: Set update frequency (10-300 seconds)
- **Data Points**: Configure historical data amount (100-1000 candles)

### 🔍 Technical Analysis Panel
- **RSI**: Current RSI value with market condition
- **MACD**: MACD line vs signal line comparison
- **Stochastic**: Momentum oscillator readings
- **Trend Analysis**: SMA-based trend identification
- **Volume Analysis**: Volume ratios and patterns
- **Price Levels**: Support/resistance from Bollinger Bands

## 🧠 Machine Learning Model

### 📊 Features Used
The prediction model uses 17 technical indicators:
- Price-based: SMA 20/50, EMA 12/26, Bollinger Bands
- Momentum: RSI, Stochastic K/D, Williams %R
- Trend: MACD, MACD Signal, ADX
- Volume: Volume SMA, A/D Line, OBV
- Volatility: 20-period rolling standard deviation
- Support/Resistance: Dynamic price levels

### 🤖 Model Architecture
- **Ensemble Approach**: Combines Gradient Boosting and Random Forest
- **Feature Scaling**: StandardScaler for normalized inputs
- **Target Variable**: Next candle direction (up/down)
- **Training Split**: 80% training, 20% validation

### 📈 Performance Metrics
- **Accuracy Score**: Percentage of correct predictions
- **Real-time Updates**: Model retrains with new data
- **Confidence Levels**: Probability scores for predictions

## 🎨 User Interface

### 🌟 Professional Design
- **Bitcoin-themed colors**: Orange (#f7931a) and professional gradients
- **Dark theme**: Easy on the eyes for extended use
- **Responsive layout**: Works on different screen sizes
- **Interactive elements**: Hover effects and real-time updates

### 📱 Mobile Friendly
- **Streamlit responsive design**: Adapts to mobile screens
- **Touch-friendly controls**: Easy navigation on tablets/phones
- **Optimized performance**: Efficient data loading and rendering

## 🔧 Technical Specifications

### 📊 Data Source
- **API**: Binance REST API
- **Symbol**: BTC/USDT
- **Timeframe**: 5-minute candles
- **Update Frequency**: Configurable (10-300 seconds)

### 🖥️ System Requirements
- **Python**: 3.7+
- **Memory**: 2GB RAM minimum
- **Internet**: Stable connection for live data
- **Browser**: Modern web browser with JavaScript

### 📦 Dependencies
```
streamlit==1.31.0
pandas==2.0.3
numpy==1.24.3
plotly==5.17.0
requests==2.31.0
scikit-learn==1.3.0
TA-Lib==0.4.28
joblib==1.3.2
python-dateutil==2.8.2
pytz==2023.3
pyngrok (for Colab tunneling)
```

## 🚨 Important Notes

### ⚠️ Disclaimer
- **Educational Purpose**: This tool is for educational and research purposes only
- **Not Financial Advice**: Predictions should not be used for actual trading decisions
- **Risk Warning**: Cryptocurrency trading involves substantial risk of loss
- **Accuracy Limitation**: No prediction model is 100% accurate

### 🔒 Data Privacy
- **No Personal Data**: Application doesn't collect personal information
- **Public API**: Uses publicly available market data
- **Local Processing**: All analysis happens in your Colab environment

### 🌐 Network Requirements
- **Internet Connection**: Required for live data fetching
- **API Access**: Binance API must be accessible
- **Ngrok Tunnel**: Required for Colab web interface

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new technical indicators
- Improving prediction accuracy
- Enhancing the user interface
- Adding new features
- Reporting bugs or issues

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Get Started

Ready to analyze Bitcoin like a pro? Follow the installation guide above and start exploring the cryptocurrency markets with advanced technical analysis and machine learning predictions!

---

**Happy Trading! 🚀₿**