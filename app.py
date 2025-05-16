from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_csp():
    data = request.get_json()
    url = data.get('url')

    if not url.startswith('http'):
        url = 'https://' + url

    try:
        response = requests.get(url, timeout=5)
        csp = response.headers.get('Content-Security-Policy', '')

        result = {
            'url': url,
            'csp': csp,
            'findings': []
        }

        if not csp:
            result['findings'].append({'issue': 'Missing CSP Header', 'status': '❌'})
        else:
            if "'unsafe-inline'" in csp:
                result['findings'].append({'issue': "Uses 'unsafe-inline'", 'status': '❌'})
            if '*' in csp:
                result['findings'].append({'issue': "Wildcard (*) used", 'status': '⚠️'})
            if 'default-src' not in csp:
                result['findings'].append({'issue': "Missing default-src", 'status': '❌'})
            if not result['findings']:
                result['findings'].append({'issue': "CSP looks good!", 'status': '✅'})

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
