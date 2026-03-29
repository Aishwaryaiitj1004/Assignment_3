from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Flower Shop 🌸</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background-color: #fff0f5;
            }
            h1 {
                color: #d63384;
            }
            .card {
                border: 1px solid #ddd;
                padding: 20px;
                margin: 20px;
                display: inline-block;
                border-radius: 10px;
                background-color: white;
                box-shadow: 2px 2px 10px #ccc;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                margin: 10px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .low {
                background-color: green;
                color: white;
            }
            .high {
                background-color: red;
                color: white;
            }
        </style>
    </head>
    <body>
        <h1>🌸 Aishwarya's Flower Shop 🌸</h1>

        <div class="card">
            <h2>🌹 Rose Bouquet</h2>
            <p>Fresh roses for special occasions</p>
        </div>

        <div class="card">
            <h2>🌼 Mixed Flowers</h2>
            <p>Colorful and vibrant mix</p>
        </div>

        <div class="card">
            <h2>🌻 Sunflowers</h2>
            <p>Brighten your day!</p>
        </div>

        <h2>Simulate Orders</h2>

        <button class="low" onclick="orderLow()">Normal Orders (10 users)</button>
        <button class="high" onclick="orderHigh()">FLASH SALE! (1000 users)</button>

        <p id="status"></p>

        <script>
            function orderLow() {
                fetch('/low');
                document.getElementById("status").innerHTML = "✅ Normal traffic (10 users)";
            }

            function orderHigh() {
                fetch('/high');
                document.getElementById("status").innerHTML = "🔥 FLASH SALE! Massive orders incoming...";
            }
        </script>
    </body>
    </html>
    '''

@app.route('/low')
def low():
    return "Normal traffic handled"

@app.route('/high')
def high():
    # simulate heavy load
    os.system("stress --cpu 2 --timeout 20")
    return "High traffic triggered!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)