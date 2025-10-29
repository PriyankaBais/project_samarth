# 🚀 Project Samarth

"Project Samarth" is an intelligent Q&A system prototype designed to source live data from India's `data.gov.in` portal.

This system is built within a **single Python file**. It finds, cleans, and merges disparate government datasets (like agriculture and climate) in real-time to answer complex questions.



---

## 🏗️ System Architecture

This project operates as a simple server:
1.  A **Flask web server** (backend) serves a web page.
2.  **JavaScript** on that web page (frontend) calls an API endpoint (`/ask`) on the *same* server.
3.  This API call triggers the **Pandas** logic in the backend, which fetches, cleans, and processes the live data.



---

## ✨ Features

* **Single File**: The entire application (backend, frontend, and logic) is in one `app_single.py` file.
* **Live Data Sourcing**: Connects directly to live CSV files from `data.gov.in`, not a stale copy.
* **Data Synthesis**: Merges two different datasets (agricultural production and climate data) using `pandas`.
* **Real-World Data Cleaning**: Handles the true messiness of government data, such as bad formatting and server blocking.
* **Traceability**: As required, every answer cites the exact source URLs it was derived from.

---

## 💻 Tech Stack

* **Backend**: **Python 3**
    * **Flask**: To host both the API and the frontend.
    * **Pandas**: For all data cleaning, transformation (`melt`), and merging.
    * **Requests**: To fetch data as a browser to avoid `504` (server block) errors.
* **Frontend**: **Vanilla HTML, CSS, & JavaScript**
    * Embedded as a string within the Python file and served by Flask.

---

## 🚀 How to Run

### 1. Prerequisites
* Python 3.8+
* `pip` (Python package installer)

### 2. Setup and Run

1.  **Save the File:** Save the complete code as `app.py`.

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    # Create a 'venv' folder
    python -m venv venv
    
    # Activate it
    # On Windows:
    .\venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Packages:**
    You only need a few libraries.
    ```bash
    pip install Flask pandas requests Flask-CORS
    ```

4.  **Run the Server:**
    ```bash
    python app_single.py
    ```

5.  **View the App:**
    Open your web browser and go to `http://127.0.0.1:5000`. Your app will be running there!

6.  **Ask a Question:**
    Type this question into the box and press "Ask":
    `Compare rainfall and crop production.`

---

## 🧠 Key Challenges and Solutions

The real challenge of this project was not building the API, but "taming" the data.

1.  **Challenge: HTTP `504 Gateway Time-out` Error**
    * **What happened:** The `data.gov.in` server was blocking automated scripts (like `pandas`) from downloading files.
    * **Solution:** Used the `requests` library to send a `User-Agent` header. This "disguised" the script as a normal web browser, bypassing the server's block.

2.  **Challenge: Messy CSV Format (`Tokenizer Error`)**
    * **What happened:** The real CSV files had several lines of titles and blank space at the top, which crashed `pandas`.
    * **Solution:** Used the `skiprows=3` parameter in `pandas.read_csv()` to tell it to ignore the first 3 junk lines and start reading from the actual data header.

3.  **Challenge: Inconsistent State Names**
    * **What happened:** The "State" column was spelled differently in the two files (e.g., `STATE ` vs. `State/UTs`) and the names themselves were inconsistent.
    * **Solution:** Renamed the columns in both files and used `.str.strip().str.upper()` to standardize all state names (e.g., to `ANDHRA PRADESH`) so they could be merged correctly.
