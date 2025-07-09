# 🧠 Kidney Disease Classification

A deep learning-based project to classify kidney CT scans as either **Normal** or **Tumor**, built using TensorFlow/Keras, Flask, and deployed with MLflow and DVC.

---

## 📁 Project Structure

```
.
├── app.py                         # Flask web app for prediction
├── config                         # Configuration files
├── dvc.yaml                       # DVC pipeline definition
├── dvc.lock                       # DVC stage locks
├── requirements.txt              # Python dependencies
├── src
│   └── cnnClassifier
│       ├── components            # Model building, training, evaluation
│       ├── config                # Data classes for config schema
│       ├── constants             # Path and constants used
│       ├── pipeline              # Pipeline scripts for all stages
│       └── utils                 # Utility functions
├── templates
│   └── index.html                # Frontend HTML form
├── artifacts                     # Model, logs, ingested data
└── static                        # Uploaded images (if any)
```

---

## 🚀 How to Run

### 🔧 1. Setup Environment

```bash
conda create -n kidney310 python=3.8 -y
conda activate kidney310
pip install -r requirements.txt
```

### 📂 2. Prepare Data

Place your **kidney CT scan images** in the format:

```
data/
├── Tumor/
├── Normal/
```

Then, configure paths inside `config/config.yaml`.

---

### ⚙️ 3. Run Pipeline

```bash
python main.py
```

Or use DVC (after `.dvc` is set up):

```bash
dvc repro
```

---

### 🌐 4. Start Web App

```bash
python app.py
```

Then open [http://localhost:8080](http://localhost:8080) in your browser to upload and classify images.

---

## 📊 MLflow Tracking

Model metrics (accuracy/loss) and saved versions are logged to:

```
https://dagshub.com/sushrai1/Kidney-Disease-Classfication.mlflow
```

---

## 🧪 Example Prediction

Upload an image on the UI and get instant prediction:  
**Normal** or **Tumor** with backend probability logged in terminal.

---

## 👨‍💻 Author

**Sushrai Anumala**  
Tier-3 B.Tech AI/ML student at KITS Warangal  
🔗 GitHub: [sushrai1](https://github.com/sushrai1)

---

## 🛠 Tech Stack

- TensorFlow / Keras
- Flask
- DVC
- MLflow (with DAGsHub)
- Python 3.8
- Bootstrap UI

