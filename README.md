# 🎯 Intern Performance Prediction — Machine Learning Prjecct

A machine learning project designed to predict the performance of interns by analyzing their work patterns, feedback from mentors, and engagement levels.
This helps HR teams and supervisors identify top-performing interns early and personalize mentorship for better growth.


---

## 📌 Objective

To build a supervised machine learning model that:

- Classifies interns as "High Performer" or "Not High Performer"
- Highlights the main factors influencing performance, such as attendance, task completion rate, and mentor feedback
- Offers a simple and interactive **Streamlit** web app for predictions


---

## 📊 Dataset Overview

The dataset includes synthetic yet realistic intern performance records with the following features:

| Column | Description |
|--------|-------------|
| `intern_id` | Unique ID |
| `department` | Intern's department (e.g., Tech, HR) |
| `interaction_level` | Level of mentor interaction |
| `attendance_rate` | % attendance |
| `task_completion_rate` | Completed tasks vs. assigned |
| `avg_feedback_score` | Mentor feedback (scale 1–5) |
| `hours_per_week` | Weekly time investment |
| `final_assessment_score` | Evaluation score (0–100) |
| `performance_label` | Target variable: High / Not High |

---

## 🧹 Preprocessing

- Handled missing values using forward fill (`fillna`)
- Encoded categorical features:
  - `LabelEncoder` in `train_model_with_encoders.ipynb`
  - `One-Hot Encoding` in `train_model_onehot.ipynb`
- Feature Scaling with `StandardScaler`

---

## 🧠 Model Training

### Models Used:
- Logistic Regression
- Random Forest Classifier
- (Optional) XGBoost

### Features Used:
- Attendance, feedback, department, hours per week, and task ratios

### Target:
- `performance_label` (High vs. Not High)

### Evaluation Metrics:
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix
- Feature Importance Chart

---

## 📈 Feature Importance (Sample Output)

- **Mentor Feedback Score** 🟢  
- **Task Completion Rate** 🔵  
- **Attendance Rate** 🟣  
- **Engagement Level** 🔴  

These insights help mentors focus on what drives intern performance.

---

## 👨‍💻 Author

**HamadAli939**  
_Data Analyst Intern @ [Internee.pk](https://www.internee.pk/)_  
---

## Acknowledgment

This project is part of my internship at **[Internee.pk](https://www.internee.pk/)** — aiming to bridge the gap between learning and real-world data projects.


