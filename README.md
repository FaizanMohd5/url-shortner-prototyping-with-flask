# URL Shortener Flask API

This is a simple URL shortener API built using **Flask**. The app allows users to shorten long URLs into shorter, more manageable links. It also supports redirection to the original URLs when visiting the shortened link.

## Features

* **Shorten a URL**: Submit a URL and get a shortened version.
* **Redirect to the Original URL**: Access the original URL by visiting the shortened URL.
* **Handles Invalid Input**: Provides clear error messages for missing or incorrect data.

## Endpoints

### 1. **POST /api/shorten**

This endpoint accepts a URL and returns a shortened version of the URL.

#### Request

* **URL**: `/api/shorten`
* **Method**: `POST`
* **Content-Type**: `application/json`
* **Body**:

```json
{
  "url": "https://example.com"
}
```

#### Response

* **Status Code**: `201 Created`
* **Body**:

```json
{
  "original_url": "https://example.com",
  "short_code": "aB1cD2",
  "short_url": "http://127.0.0.1:5000/aB1cD2"
}
```

---

### 2. **GET /:short_code**

This endpoint redirects users to the original URL using the short code.

#### Request

* **URL**: `/aB1cD2` (where `aB1cD2` is an example short code)
* **Method**: `GET`

#### Response

* **Status Code**: `302 Found` (Redirect)
* **Location Header**: Redirects to the original URL, e.g., `https://example.com`

---

## How to Test Using `curl`

To test the API using `curl`, follow the commands below.

### 1. Shorten a URL

```bash
curl -X POST http://127.0.0.1:5000/api/shorten \
     -H "Content-Type: application/json" \
     -d '{"url": "https://example.com"}'
```

#### Expected Response

```json
{
  "original_url": "https://example.com",
  "short_code": "aB1cD2", 
  "short_url": "http://127.0.0.1:5000/aB1cD2"
}
```

---

### 2. Shorten URL with Missing `url` Field

```bash
curl -X POST http://127.0.0.1:5000/api/shorten \
     -H "Content-Type: application/json" \
     -d '{}'
```

#### Expected Response

```json
{
  "error": "Missing 'url' field in request body"
}
```

---

### 3. Shorten URL with Invalid URL Format

```bash
curl -X POST http://127.0.0.1:5000/api/shorten \
     -H "Content-Type: application/json" \
     -d '{"url": "example.com"}'
```

#### Expected Response

```json
{
  "original_url": "https://example.com",
  "short_code": "1x2Y3Z",
  "short_url": "http://127.0.0.1:5000/1x2Y3Z"
}
```

---

### 4. Redirect to Original URL

Using the short code from the previous step (`aB1cD2`), you can test the redirection:

```bash
curl -i http://127.0.0.1:5000/aB1cD2
```

#### Expected Response

```text
HTTP/1.1 302 Found
Content-Type: text/html; charset=utf-8
Location: https://example.com
Content-Length: 215
Date: Sat, 03 Nov 2025 12:00:00 GMT
Server: Werkzeug/2.0.1 Python/3.9.5

<html>
  <body>
    <a href="https://example.com">Redirecting...</a>
  </body>
</html>
```

---

### 5. Access a Non-Existent Short Code

```bash
curl -i http://127.0.0.1:5000/nonexistent_code
```

#### Expected Response

```text
HTTP/1.1 404 Not Found
Content-Type: application/json
Content-Length: 27
Date: Sat, 03 Nov 2025 12:00:00 GMT
Server: Werkzeug/2.0.1 Python/3.9.5

{
  "error": "Not Found"
}
```

---

### 6. Request an Invalid Endpoint

```bash
curl -i http://127.0.0.1:5000/invalid_endpoint
```

#### Expected Response

```text
HTTP/1.1 404 Not Found
Content-Type: application/json
Content-Length: 27
Date: Sat, 03 Nov 2025 12:00:00 GMT
Server: Werkzeug/2.0.1 Python/3.9.5

{
  "error": "Not Found"
}
```

---

## How to Run the App Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

The app will be running at `http://127.0.0.1:5000`.

---

## Why I did this?
Flask really shines when you want to quickly spin up an API with minimal code. The way it abstracts out functions, decorators, and classes makes development so much smoother—it’s perfect for rapid prototyping. You can go from idea to working API in no time! It’s fast, easy to test with Postman, curl or any client, and integrates seamlessly with frontend apps. Plus, deployment is a breeze. It’s just a really fun, efficient way to prototype APIs quickly!