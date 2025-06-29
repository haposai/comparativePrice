from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_price_from_ripley(product):
    query = product.replace(" ", "+")
    url = f"https://simple.ripley.com.pe/search/?term={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        item = soup.select_one('.catalog-product-item')
        if not item:
            return "No encontrado"

        title = item.select_one('.catalog-product-name').text.strip()
        price = item.select_one('.catalog-prices .catalog-price').text.strip()
        link = "https://simple.ripley.com.pe" + item.a['href']

        return f"{title} - {price} - <a href='{link}' target='_blank'>Ver</a>"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        product = request.form["product"]
        results["Ripley Perú"] = get_price_from_ripley(product)
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)