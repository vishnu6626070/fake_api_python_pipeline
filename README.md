# 🚀 Fake Store API – End-to-End ETL Data Engineering Pipeline

**A Python-based Data Engineering project that extracts product and user data from a Fake Store API, transforms the raw data, and loads it into a SQLite database using an automated ETL pipeline.**

---

## 👨‍💻 Author

**A. Vishnuvardhan Reddy**  
B.Tech – Computer Science and Data Science  
Aditya University

---

## 📌 Project Overview

This project demonstrates the implementation of an end-to-end **ETL (Extract, Transform, Load) pipeline** using Python.

The pipeline collects product and user information from a Fake Store API, performs data transformation and processing, and stores the cleaned data in a SQLite database.

It also includes automated logging, exception handling, execution-time tracking, and database verification to ensure reliable pipeline execution.

The primary objective is to understand and implement real-world Data Engineering concepts through a practical project.

## 🎯 Project Objectives

- Extract product and user data from a REST API.
- Transform raw API responses into structured datasets.
- Perform data processing before database insertion.
- Load transformed datasets into a SQLite database.
- Verify successfully loaded database records.
- Implement logging and exception handling.
- Monitor pipeline execution time and processing status.
- Build a modular and maintainable ETL architecture.

## 🏗️ ETL Architecture

```text
       FAKE STORE API
              |
              ▼
       ┌─────────────┐
       │   EXTRACT   │
       │             │
       │ Products    │
       │ Users       │
       └──────┬──────┘
              |
              ▼
       ┌─────────────┐
       │  TRANSFORM  │
       │             │
       │ Data Cleaning│
       │ Processing  │
       │ Structuring │
       └──────┬──────┘
              |
              ▼
       ┌─────────────┐
       │    LOAD     │
       │             │
       │ SQLite DB   │
       └──────┬──────┘
              |
              ▼
       ┌─────────────┐
       │   VERIFY    │
       │             │
       │ DB Records  │
       │ Validation  │
       └──────┬──────┘
              |
              ▼
       PIPELINE SUCCESS
```

## ⚙️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| REST API | Data extraction |
| Pandas | Data transformation and processing |
| SQLite | Database storage |
| Logging | Pipeline monitoring |
| Pathlib | File and directory management |
| Datetime | Execution-time tracking |

## 📂 Project Structure

```text
Fake-API-ETL-Pipeline/
│
├── ETL/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── logs/
│   └── pipeline.log
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🔄 Pipeline Workflow

### 1. Extract

- Connects to the Fake Store API.
- Retrieves product information.
- Retrieves user information.
- Collects raw data for further processing.

### 2. Transform

- Processes extracted product data.
- Processes extracted user data.
- Converts raw data into structured datasets.
- Prepares transformed data for database storage.

### 3. Load

- Loads transformed product data into SQLite.
- Loads transformed user data into SQLite.
- Stores the processed datasets for further analysis.

### 4. Verify

- Verifies database records after loading.
- Checks the successful execution of the loading process.

### 5. Logging and Monitoring

The project implements Python's logging module to monitor pipeline execution.

It captures:
- Pipeline starting and completion status.
- Individual ETL stage execution.
- Number of products processed.
- Number of users processed.
- Total execution time.
- Errors and exceptions.

Logs are stored in `logs/pipeline.log`.

## 🛠️ Installation and Execution

**Prerequisites**

- Python 3.10 or above
- Git
- Internet connection for API access

**Step 1: Clone the repository**

```bash
git clone https://github.com/vishnu6626070/fake_api_python_pipeline
```

**Step 2: Navigate to the project directory**

```bash
cd Fake-API-ETL-Pipeline
```

**Step 3: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 4: Run the ETL pipeline**

```bash
python main.py
```

## 📊 Expected Output

After successful execution, the pipeline displays logs similar to:

```text
============================================================
Fake Store ETL pipeline started
============================================================

STEP 1: Extracting data
STEP 2: Transforming data
STEP 3: Loading data into SQLite
STEP 4: Verifying database records

============================================================
ETL PIPELINE COMPLETED SUCCESSFULLY

Products processed: 20
Users processed: 10
Execution time: 8.86 seconds

============================================================
```

*Actual record counts and execution time depend on the API response and runtime environment.*

## 💡 Key Data Engineering Concepts Demonstrated

- ETL Pipeline Development
- REST API Data Extraction
- Data Transformation
- Structured Data Processing
- SQLite Database Integration
- Modular Python Architecture
- Logging and Monitoring
- Exception Handling
- Database Verification
- Pipeline Execution Monitoring

## 🚀 Future Enhancements

- Implement incremental data loading.
- Introduce automated pipeline scheduling.
- Add data quality checks and validation rules.
- Implement retry mechanisms for API failures.
- Integrate PostgreSQL for scalable database storage.
- Add Docker support for containerization.
- Implement automated pipeline monitoring.
- Build a dashboard to visualize pipeline execution and data statistics.

## 🎓 Learning Outcome

This project provides practical experience in developing a modular ETL pipeline and understanding how data moves from external APIs into structured databases.

It demonstrates the foundational skills required for Data Engineering roles, including API integration, data processing, database management, pipeline orchestration concepts, and monitoring.

---

**Developed by A. Vishnuvardhan Reddy**  
B.Tech – Computer Science and Data Science  
Aditya University

*Building practical Data Engineering solutions through continuous learning and implementation.*
