# water-quality-detection-system
AI-powered Smart Water Quality Detection Dashboard with Maharashtra Map Visualization, ML Predictions, and Interactive Analytics built using Streamlit.

# 💧 Water Quality Detection System

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Machine Learning](https://img.shields.io/badge/ML-Enabled-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered web application that analyzes water quality using machine learning and provides real-time insights through an interactive dashboard and Maharashtra map visualization.

---

## 🚀 Overview

The **Water Quality Detection System** is designed to evaluate whether water is safe for consumption based on various chemical parameters.

This project combines:

* 🧠 Machine Learning
* 📊 Data Visualization
* 🌍 Location-based Analysis

to deliver smart and interactive results.

---

## ✨ Key Features

* 🔬 AI-based prediction (Safe / Moderate / Contaminated)
* 📊 Interactive dashboard with trend analysis
* 🌍 Maharashtra map with real-time markers
* 📈 Gauge meter (speedometer-style visualization)
* 💡 Smart suggestions for improving water quality
* 💾 Data storage for history tracking

---

## 🧠 Machine Learning

* Dataset: **Kaggle Water Potability Dataset**
* Model Type: **Supervised Classification Model**
* Preprocessing: **StandardScaler**
* Prediction Type: **Probability-based classification**

The model analyzes chemical properties of water and predicts its potability using trained data.

---

## 🛠 Tech Stack

| Category         | Tools Used           |
| ---------------- | -------------------- |
| Frontend         | Streamlit, HTML, CSS |
| Backend          | Python               |
| Machine Learning | Scikit-learn         |
| Data Handling    | Pandas, NumPy        |
| Visualization    | Plotly, Folium       |
| Model Handling   | Joblib               |

---

## 📦 Requirements

### 💻 System Requirements

* Python 3.9 or higher
* pip (Python package manager)

---

### 📚 Python Libraries

```txt
streamlit
pandas
numpy
scikit-learn
joblib
plotly
folium
streamlit-folium
```

### 🔍 Library Usage

* **streamlit** → Web UI & dashboard
* **pandas / numpy** → Data processing
* **scikit-learn** → Machine learning model
* **joblib** → Model loading
* **plotly** → Charts & gauge meter
* **folium** → Map visualization
* **streamlit-folium** → Map integration

---

## 📂 Project Structure

```
WATER-PROJECT2.0/
│
├── app.py
├── model.py
├── utils.py
├── styles.css
│
├── pages/
│   ├── 1_Analysis.py
│   ├── 2_Dashboard.py
│   ├── 3_Map.py
│
├── data/
│   └── history.csv
│
├── water_model.pkl
├── scaler.pkl
├── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📊 How It Works

1. User enters water parameters

2. Data is scaled using StandardScaler

3. ML model predicts water quality probability

4. Output is displayed as:

   * Result (Safe / Moderate / Contaminated)
   * Confidence score
   * Gauge meter visualization

5. Data is stored for:

   * Trend analysis
   * Dashboard graphs
   * Map visualization

---

## 🌍 Map Visualization

* 🟢 Green → Safe
* 🟠 Orange → Moderate
* 🔴 Red → Contaminated

Each marker represents a city in Maharashtra with real-time results.

---

## 🔮 Future Enhancements

* 📄 PDF Report generation
* 🤖 Time-series prediction
* 🌐 Cloud deployment
* 📱 Mobile UI optimization

---

## 📜 License

This project is licensed under the MIT License.

---

## 👩‍💻 Author

**Bhakti Mate**
Second Year Engineering Student (AIDS)
NMIET

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
