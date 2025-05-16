# 🔐 CSP Analyzer

A web-based tool that analyzes the **Content-Security-Policy (CSP)** and other HTTP security headers of any website. It helps identify missing or risky directives and assigns a security grade (A–D) based on header presence and policy strength.

---

## 🚀 Features

- Checks for standard security headers like:
  - `Content-Security-Policy`
  - `Strict-Transport-Security`
  - `X-Frame-Options`
  - `X-Content-Type-Options`
  - `Referrer-Policy`
  - `Permissions-Policy`
  - `Access-Control-Allow-Origin`
- Highlights missing or weak CSP rules (`unsafe-inline`, wildcard `*`, missing `default-src`)
- Assigns a letter-based security grade (A, B, C, D)
- Hosted frontend (GitHub Pages) and backend (Render) deployment

---

## 🌐 Live Demo

- **Frontend:** [GitHub Pages](https://phemtech-solutions.github.io/csp-analyzer/)
- **Backend:** [Render API](https://csp-analyzer.onrender.com/analyze)

---

## 🛠️ Tech Stack

- **Frontend:** HTML, JavaScript (Vanilla)
- **Backend:** Python (Flask), hosted on [Render](https://render.com)
- **DevOps:** Git, GitHub Pages, GitHub Actions

---

## 🧠 How It Works

1. You enter a website URL.
2. It sends a POST request to the Flask backend.
3. The backend:
   - Fetches response headers from the URL.
   - Extracts the CSP (if any).
   - Validates presence of key security headers.
   - Analyzes risky patterns in the CSP.
   - Assigns a grade and returns results.
4. The frontend displays all info neatly with grades and emojis.

---

## 📈 Grade Criteria

| Issue                     | Impact     | Score Penalty |
|--------------------------|------------|----------------|
| Missing Security Header  | ❌ High     | -1             |
| Wildcard `*` in CSP      | ⚠️ Medium   | -1             |
| `unsafe-inline` in CSP   | ❌ High     | -1             |
| Missing `default-src`    | ❌ High     | -1             |

---

## 💡 Future Improvements

- Scan entire response headers in more detail
- Add CSP improvement recommendations
- Export results or reports (CSV/JSON)

---

## 👨‍💻 Author

**Ajijola Oluwafemi Blessing**  
[LinkedIn](https://www.linkedin.com/in/ajijola-oluwafemi-ba839712a/) • [GitHub](https://github.com/oluwafemiab/ajijola.github.io)
