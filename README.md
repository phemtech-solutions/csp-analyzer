# 🔐 CSP Analyzer

CSP Analyzer is a web-based tool that checks for the presence and quality of **Content-Security-Policy (CSP)** and other important HTTP security headers on any website. It identifies missing or risky configurations and assigns a security grade from **A to D**.

---

## 🚀 Live Demo

🌐 **Try it Live:** [https://phemtech-solutions.github.io/csp-analyzer/](https://phemtech-solutions.github.io/csp-analyzer/)

> Enter any website URL to view its CSP headers, get detailed feedback, and receive a security grade from A–D.

---

## 🚀 Features

- ✅ Detects missing or weak HTTP security headers:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
  - `Access-Control-Allow-Origin`
- ✅ Analyzes CSP for:
  - `unsafe-inline` usage
  - Wildcard `*` usage
  - Missing `default-src`
- ✅ Assigns a letter-based security grade (A–D)
- ✅ Shows detailed findings with emoji indicators: ✅ ⚠️ ❌
- ✅ Fully offline-capable (runs locally on your machine)

---

## 🧰 Tech Stack

| Layer      | Technology            |
|------------|------------------------|
| Frontend   | HTML, CSS, JavaScript  |
| Backend    | Python (Flask)         |
| Deployment | Localhost              |

---

## 💻 Installation Guide (Run Locally)

### ✅ Requirements

- Python 3 installed
- Git installed (or download ZIP)
- Browser (Chrome, Firefox, etc.)

---

### 🔧 Backend Setup (Flask API)

```bash
# 1. Clone the repository
git clone https://github.com/phemtech-solutions/csp-analyzer.git
cd csp-analyzer

# 2. Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Start the Flask server
python app.py
```

🟢 The server will run at: `http://127.0.0.1:10000`

---

### 🖥️ Frontend Setup (Local)

```bash
# 1. Open this file in your browser:
docs/index.html

# 2. In the file, make sure the fetch API in the JavaScript section uses the local backend:

# Change this:
fetch('https://csp-analyzer.onrender.com/analyze', {

# To this:
fetch('http://127.0.0.1:10000/analyze', {

# 3. Save the file and reload it in your browser.
# 4. Enter a domain like "example.com" and click SCAN.
```

---

## 🧠 How It Works

1. You input a URL (e.g. `facebook.com`)
2. The frontend sends the URL to the backend via POST
3. Flask fetches the headers from the target website
4. Security headers are checked for presence and quality
5. A grade is assigned based on the results
6. The frontend displays findings and the grade

---

## 📊 Grading System

| Issue                     | Symbol | Deduction |
|--------------------------|--------|-----------|
| Missing Header           | ❌     | -1        |
| Wildcard `*` in CSP      | ⚠️     | -1        |
| `unsafe-inline` in CSP   | ❌     | -1        |
| Missing `default-src`    | ❌     | -1        |

### Final Score → Grade

| Score Range | Grade |
|-------------|--------|
| 4.5 – 5.0   | A      |
| 3.5 – 4.4   | B      |
| 2.0 – 3.4   | C      |
| Below 2.0  | D      |

---

## 💡 Future Enhancements

- Show full HTTP response headers
- Recommend secure CSP configurations
- Export results to CSV or JSON
- Add CLI version of the tool
- Visual dashboard for multiple scans

---

## 👨‍💻 Author

**Ajijola Oluwafemi Blessing**  
Cybersecurity | Software | IT | Research

- GitHub: [phemtech-solutions](https://github.com/oluwafemiab/ajijola.github.io)  
- LinkedIn: [https://www.linkedin.com/in/ajijola-oluwafemi-ba839712a/)

