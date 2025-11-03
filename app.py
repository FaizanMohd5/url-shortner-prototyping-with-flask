from flask import Flask, request, jsonify, redirect, abort
import string
import random

app = Flask(__name__)

# In-memory database using a Python dictionary
# Format: { 'short_code': 'long_url' }
url_database = {}

def generate_short_code(length=6):
    """Generate a random alphanumeric short code."""
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(characters) for i in range(length))
        # Ensure the generated code is unique
        if code not in url_database:
            return code

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """Accepts a URL and returns a short code."""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    long_url = data.get('url')

    if not long_url:
        return jsonify({"error": "Missing 'url' field in request body"}), 400
    
    # Simple validation (better validation would check format)
    if not long_url.startswith(('http://', 'https://')):
        long_url = 'https://' + long_url

    short_code = generate_short_code()
    url_database[short_code] = long_url

    return jsonify({
        "original_url": long_url,
        "short_code": short_code,
        "short_url": request.host_url + short_code
    }), 201 # 201 Created status code

@app.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    """Redirects the user from the short code to the original URL."""
    long_url = url_database.get(short_code)
    
    if long_url:
        return redirect(long_url, code=302) # 302 Found/Redirect status code
    else:
        abort(404) # 404 Not Found status code

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
