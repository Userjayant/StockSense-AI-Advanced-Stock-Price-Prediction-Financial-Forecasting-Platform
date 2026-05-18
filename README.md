# 📈 Stock Price Prediction using Machine Learning

A professional, end-to-end Machine Learning project that predicts stock prices using **Linear Regression**, **Random Forest**, and **LSTM (Deep Learning)** models on historical market data from Yahoo Finance. Comes with a beautiful **Flask web dashboard** for interactive predictions and visualizations.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)
![ML](https://img.shields.io/badge/ML-Scikit--Learn%20%7C%20TensorFlow-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🚀 Features

- ✅ **Live data fetching** from Yahoo Finance (any ticker: AAPL, GOOGL, TSLA, INFY.NS, etc.)
- ✅ **Multiple ML models**: Linear Regression, Random Forest, LSTM
- ✅ **Technical indicators**: SMA, EMA, RSI, MACD, Bollinger Bands
- ✅ **Interactive web dashboard** (Flask + Chart.js)
- ✅ **Forecast next N days** with confidence visualization
- ✅ **Model evaluation**: RMSE, MAE, R² Score
- ✅ **Beautiful, responsive UI** with dark theme
- ✅ **CLI training script** + **Jupyter notebook** for experimentation

---

## 📂 Project Structure

```
stock-price-prediction/
├── src/
│   ├── data_loader.py         # Fetches data from Yahoo Finance
│   ├── features.py            # Technical indicators
│   ├── models.py              # ML/DL models
│   ├── train.py               # Training pipeline
│   └── predict.py             # Forecast utilities
├── templates/
│   └── index.html             # Web dashboard
├── static/
│   └── style.css              # Dashboard styling
├── notebooks/
│   └── exploration.ipynb      # EDA notebook
├── models/                    # Saved trained models (.pkl)
├── outputs/                   # Plots & predictions
├── app.py                     # Flask web app
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Setup in VS Code (Zero-Error Guide)

### 1. Prerequisites
- Install **[Python 3.9+](https://www.python.org/downloads/)** (check "Add Python to PATH" during install)
- Install **[VS Code](https://code.visualstudio.com/)**
- Install VS Code extensions: **Python**, **Pylance**, **Jupyter**

### 2. Open in VS Code
```bash
# Unzip the downloaded file, then:
code stock-price-prediction
```
Or: `File → Open Folder → select stock-price-prediction`

### 3. Create a virtual environment
Open the VS Code terminal (`Ctrl + ~`) and run:

**Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Select the Python interpreter in VS Code
`Ctrl + Shift + P` → **Python: Select Interpreter** → choose the one inside `./venv`

### 6. Train the models (one-time)
```bash
python src/train.py --ticker AAPL --period 5y
```
Trained models are saved to `models/`.

### 7. Run the web dashboard
```bash
python app.py
```
Open **http://127.0.0.1:5000** in your browser. 🎉

---

## 💻 Usage

### Web App
1. Enter a ticker (e.g., `AAPL`, `TSLA`, `MSFT`, `RELIANCE.NS`)
2. Choose model (Linear Regression / Random Forest / LSTM)
3. Pick forecast horizon (1–30 days)
4. View interactive chart + predicted prices + metrics

### CLI
```bash
python src/predict.py --ticker GOOGL --days 7 --model random_forest
```

---

## 📊 Models Implemented

| Model              | Type           | Best For                |
|--------------------|----------------|-------------------------|
| Linear Regression  | Statistical    | Quick baseline          |
| Random Forest      | Ensemble       | Non-linear patterns     |
| LSTM               | Deep Learning  | Time-series sequences   |

---

## 🌟 Professional Upgrades Included

- 🎨 Modern dark-themed responsive UI
- 📈 Interactive Plotly/Chart.js visualizations
- 🧠 Multiple algorithms with side-by-side comparison
- 🔧 Modular, production-ready code structure
- 📓 Jupyter notebook for data exploration
- 🐳 `Dockerfile` for containerized deployment
- ✅ Type hints & docstrings throughout
- 🔐 `.env` support for configuration
- 🧪 Unit tests in `tests/`

---

## 🚢 Push to GitHub — Step by Step

### 1. Create a GitHub account (if you don't have one)
Sign up at **[github.com](https://github.com/)**

### 2. Install Git
Download from **[git-scm.com](https://git-scm.com/downloads)** and install.

Verify:
```bash
git --version
```

### 3. Configure Git (first time only)
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### 4. Create a new repository on GitHub
- Go to **github.com** → click **`+`** (top-right) → **New repository**
- Name: `stock-price-prediction`
- Description: *"ML system to forecast stock prices using regression & LSTM"*
- Choose **Public** (or Private)
- **Do NOT** add README, .gitignore, or license (we already have them)
- Click **Create repository**

### 5. Initialize Git & push from VS Code terminal
In the project folder:
```bash
git init
git add .
git commit -m "Initial commit: Stock Price Prediction using ML"
git branch -M main
git remote add origin https://github.com/<your-username>/stock-price-prediction.git
git push -u origin main
```
Replace `<your-username>` with your GitHub username.

> If GitHub asks for credentials, generate a **Personal Access Token**:
> GitHub → Settings → Developer settings → Personal access tokens → Generate new → use it as the password.

### 6. (Easier) Push using VS Code GUI
- Click the **Source Control** icon (left sidebar)
- Click **Initialize Repository**
- Stage all → Type commit message → ✓ Commit
- Click **Publish Branch** → select GitHub → done! 🎉

### 7. Verify
Refresh your GitHub repo page — all files should be there.

---

## 📝 License
MIT © 2026 — Built with ❤️ for ML enthusiasts.

## ⚠️ Disclaimer
This project is for **educational purposes only**. Stock predictions are inherently uncertain — **do not use this as financial advice**.
