from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Root Route is Working</h1>"


@app.route('/htop')
def htop():
    # Getting the server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Getting the top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Constructing the HTML response
    html_content = f"""
    <html>
    <body>
        <h1>Name:karthik</h1>
        <h2>Username: {os.getenv("USER")}</h2>
        <h3>Server Time (IST): {server_time}</h3>
        <pre>Top output:\n\n{top_output}</pre>
    </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
