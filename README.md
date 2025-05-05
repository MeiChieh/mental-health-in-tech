# 🧠 Mental Health in Tech Industry Analysis

## 📊 Overview

This project performs an exploratory data analysis (EDA) on survey data about mental health in the technology industry. The analysis provides insights into mental health trends, workplace practices, and employee experiences across different tech companies.

## 📚 Dataset

The analysis uses the [Mental Health in Tech Survey Dataset](https://www.kaggle.com/datasets/anth7310/mental-health-in-the-tech-industry/data) from Kaggle, which includes:

- Survey responses from tech industry professionals
- Mental health history and current status
- Workplace environment information
- Company policies and practices
- Remote work arrangements

## 📗 Analysis Notebook

[project.ipynb](https://github.com/MeiChieh/mental-health-in-tech/blob/main/project.ipynb)

## ⭐ Key Findings

### 1. Survey Participant Demographics

- Age group distribution
- Gender representation
- Geographic distribution
- Company size variations
- Self-employment status
- Remote work arrangements

### 2. Mental Health Insights from the Survey

1. Most people are more comfortable discussing mental health issue with their direct supervisors than with colleagues, irrespective of their demographic characteristics. And they believe that the discussion of MH with employers won't have negative impact on their career.
2. Male are the most optimistic gender group about mental health discussion in work place despite of their little knowledge of mental health related benefits.
3. Binary people are open to discuss mental health with peers (colleagues) but not so much with supervisors and employers. They are the rare group that feel very pessimistic about the consequence of the disussion.
4. People working in companies with more than 1000 people are the least comfortable discussing mental health with either colleagues or supervisors, and higher proportion of them also feel the discussion would impact their career.
5. Through the progression of the year, higher percentage of people are openly identified with mental health issues in the work place, but also more of them feel the disclosure has impact on their career.
6. Comparing current and previous jobs, people are more satisfied with the effort the current company placed on mental and physical health for all three years. However, companies always place much more emphasis on physical health.
7. Remote work subgroup in this survey have shown the highest level of open, relaxed and optimistic sentiment when it comes to mental health issue with coworkers, supervisor, and taking of sick leaves.

## 📁 Project Structure

```
├── project.ipynb          # Main analysis notebook
├── mental_health.sqlite   # SQLite database containing the survey data
├── requirements.txt       # Python package requirements
├── Pipfile               # Pipenv dependencies
├── Pipfile.lock          # Pipenv lock file
├── helpers/              # Helper functions and utilities
│   ├── helper_function.py # Custom helper functions
│   ├── stopwords.txt     # Stopwords for text analysis
│   └── __init__.py       # Package initialization
└── README.md             # Project documentation
```

## 🛠️ Technologies Used

- Python
- SQLite
- Data Analysis Libraries
- Visualization Tools

## 🚀 Setup and Installation

1. Clone the repository
2. Access the analysis notebook:
   - [Analysis Notebook 📚](https://github.com/TuringCollegeSubmissions/mchien-DA.1/blob/master/project.ipynb)

## 💡 Usage

The main analysis can be found in `project.ipynb`. The notebook includes:

- Data loading and preprocessing
- Exploratory data analysis
- Visualization of mental health trends
- Statistical analysis
- Subgroup comparisons

## 🔄 Future Improvements

1. Expand analysis to include more recent survey data
2. Implement sentiment analysis on open-ended responses
3. Develop predictive models for mental health risk factors
4. Create interactive visualizations
5. Add comparative analysis with other industries

## 📦 Dependencies

Key dependencies include:

- Python data analysis libraries
- SQLite for data storage
- Visualization libraries

For a complete list of dependencies, see the project notebook.
