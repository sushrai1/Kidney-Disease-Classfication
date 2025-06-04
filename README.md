## 🩺 Kidney Disease Classification - MLflow & DVC

### 🚀 Setup Instructions (Completed Steps)

```bash
# 1. Clone the repository
git clone https://github.com/sushrai1/Kidney-Disease-Classfication.git
cd Kidney-Disease-Classfication

# 2. Create and activate conda environment
conda create -n kidney310 python=3.10 -y
conda activate kidney310

# 3. Install project requirements
pip install -r requirements.txt
```
Absolutely! Here’s the entire section all in one go, ready for you to copy-paste into your README:

## Workflows

1. Update `config.yaml`  
2. Update `secrets.yaml`  
3. [Optional] Update `params.yaml`  
4. Update the entity configurations  
5. Update the configuration manager in `src/config`  
6. Update the components  
7. Update the pipeline  
8. Update `main.py`  
9. Update `dvc.yaml`  

---

## How to Run?

### STEPS:

1. **Clone the repository**

```bash
git clone https://github.com/sushrai1/Kidney-Disease-Classfication.git

⸻

Data Ingestion & MLflow Logging Workflow
	1.	Data Ingestion
	•	Load raw dataset
	•	Basic preprocessing (handle missing values)
	•	Save processed dataset
	2.	MLflow Logging
	•	Start MLflow run
	•	Log parameters (number of rows, columns)
	•	Log processed dataset as artifact
	•	End MLflow run
	3.	Run pipeline
	•	Execute python data_ingestion.py to perform above steps
	4.	Visualization
	•	Use MLflow UI to track and inspect runs

⸻

This setup ensures reproducibility and traceability of your data processing pipeline before model training.
