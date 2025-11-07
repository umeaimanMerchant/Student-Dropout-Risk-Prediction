# Predicting Student Dropout in Higher Education

In the evolving landscape of higher education, institutions face increasing pressure to improve student retention and academic success. Dropout rates not only reflect individual struggles but also indicate systemic challenges such as financial hardship, academic mismatch, or lack of institutional support.

This project leverages **data-driven techniques** to uncover the hidden patterns behind student dropout and build predictive models to identify at-risk students early.

---

## Project Overview

The dataset represents a comprehensive record of students from a higher education institution — including demographics, socioeconomic background, academic performance, and enrollment behavior.

The primary objective is to **predict student dropout** using machine learning, providing actionable insights to educators and administrators for timely interventions.

---

## Project Workflow

### 1. Data Understanding & Preparation
- Explored the dataset to understand its structure and attributes.  
- Handled missing values and inconsistent entries.  
- Encoded categorical variables and standardized numeric features.  
- Ensured data quality and reliability for further analysis.

### 2. Exploratory Analysis & Feature Engineering
- Investigated patterns such as:
  - Dropout rates by program or department.  
  - Impact of attendance type, grades, and financial support.  
  - Correlation between demographic and academic factors.
- Engineered meaningful features to improve model accuracy.

### 3. Machine Learning Modeling
- Implemented and evaluated multiple classifiers:
  - **Random Forest**
  - **Logistic Regression**
  - **Support Vector Machine (SVM)**
- Assessed model performance using:
  - **Accuracy**
  - **Precision**
  - **F1-Score**
- Selected the best-performing model for deployment.

### 4. Interactive Deployment
- Built a **Streamlit web application** to enable real-time dropout risk predictions.  
- Users can input student attributes and instantly view:
  - Dropout probability (risk score)  
  - Model-driven insights for academic advisors and administrators  

### 5. Storytelling & Reporting
- Created a comprehensive report summarizing:
  - Data insights and visualization findings  using Tableau
  - Model comparison and evaluation metrics  
  - Key takeaways and actionable recommendations

---

## Tech Stack

| Category | Tools / Libraries |
|-----------|-------------------|
| **Programming** | Python |
| **Data Storage** | Duckdb, Microsoft SQL |
| **Data Handling** | Pandas, NumPy |
| **Modeling** | scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Web App** | Streamlit |
| **Model Storage** | Pickle |

---

## How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-dropout-prediction.git
   cd student-dropout-prediction
    ````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the model training script**

   ```bash
   python train_model.py
   ```

4. **Launch the Streamlit app**

   ```bash
   streamlit run app.py
   ```

---

## Expected Outcomes

* Accurate classification of students as:

  * **Graduate (0)**
  * **Dropout (1)**
* Identification of key predictors of dropout.
* Visual and interactive reporting through dashboards and the Streamlit interface.

---

## Model Performance

**Best Model:** `LogisticRegression`  
**Performance Metrics:**
```python
{'accuracy': 0.9201101928374655, 'precision': 0.9207543940014337, 'f1': 0.9193411475853628}
```


---

## Tableau Visualizations

1. Dropout Distribution by Course

<img width="1440" height="608" alt="image" src="https://github.com/user-attachments/assets/613520da-2a40-45cc-81d8-2748eaef95f5" />


2. Dropout Distribution by Gender

<img width="1440" height="608" alt="image" src="https://github.com/user-attachments/assets/ad63bbb9-9149-4312-958a-f440616ccd24" />

3. Dropout Distribution by Age

<img width="1440" height="608" alt="image" src="https://github.com/user-attachments/assets/94d597cd-e97e-4ef3-bba4-4809fd624669" />

4. Socioeconomic Impact Analysis	

<img width="1440" height="608" alt="image" src="https://github.com/user-attachments/assets/30e06432-31fe-4100-a8aa-49c58d900cec" />

<img width="1440" height="608" alt="image" src="https://github.com/user-attachments/assets/a9149c96-ef6a-4d64-b46f-2a1a5390c27f" />


---

## Streamlit App

<img width="1447" height="780" alt="image" src="https://github.com/user-attachments/assets/7833a485-960e-466b-a8c1-08a60aeea8c9" />

<img width="1447" height="780" alt="image" src="https://github.com/user-attachments/assets/fda0dfa2-3eb6-4dd3-aeff-6b08e454f5cd" />

## Future Enhancements

* Incorporate deep learning models for improved accuracy.
* Integrate explainable AI (SHAP, LIME) to interpret predictions.
* Expand dataset with real-time academic and behavioral metrics.


