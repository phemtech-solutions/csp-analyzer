from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# List of security headers to check for
SECURITY_HEADERS = {
    "Content-Security-Policy": "CSP",
    "Strict-Transport-Security": "HSTS",
    "X-Frame-Options": "Clickjacking Protection",
    "X-Content-Type-Options": "MIME Sniffing",
    "Referrer-Policy": "Referrer Info",
    "Permissions-Policy": "Permissions Control",
    "Access-Control-Allow-Origin": "CORS"
}

@app.route('/analyze', methods=['POST'])
def analyze_csp():
    data = request.get_json()
    url = data.get('url')

    if not url.startswith('http'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        csp = headers.get('Content-Security-Policy', '')

        result = {
            'url': url,
            'csp': csp,
            'findings': []
        }

        # 1. Check for presence of all defined security headers
        for header, description in SECURITY_HEADERS.items():
            if header not in headers:
                result['findings'].append({
                    'issue': f"Missing {description} header ({header})",
                    'status': '❌'
                })

        # 2. Analyze CSP content specifically
        if not csp:
            result['findings'].append({'issue': 'Missing CSP Header', 'status': '❌'})
        else:
            if "unsafe-inline" in csp:
                result['findings'].append({'issue': "Uses 'unsafe-inline'", 'status': '❌'})
            if '*' in csp:
                result['findings'].append({'issue': "Wildcard (*) used", 'status': '⚠️'})
            if 'default-src' not in csp:
                result['findings'].append({'issue': "Missing default-src", 'status': '❌'})

        if not any(f['issue'].startswith("Missing") for f in result['findings']):
            result['findings'].append({'issue': "CSP looks good!", 'status': '✅'})

        # 3. Add scoring and grade
        score = 5
        for f in result['findings']:
            if f['status'] == '❌':
                score -= 2
            elif f['status'] == '⚠️':
                score -= 1

        if score >= 5:
            result['grade'] = 'A'
        elif score >= 3:
            result['grade'] = 'B'
        elif score >= 1:
            result['grade'] = 'C'
        else:
            result['grade'] = 'D'

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
