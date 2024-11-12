from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Gather system details
    name = "Amrit Raj"  # Replace with your full name
    username = getpass.getuser()  # Get the current user's username
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %Z')
    top_output = subprocess.getoutput("top -b -n 1")

    # HTML to display with basic styling
    return f"""
    <html>
        <head>
            <title>System Information</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #4CAF50; }}
                pre {{ background-color: #f4f4f4; padding: 10px; border: 1px solid #ddd; }}
                p {{ font-size: 18px; }}
            </style>
        </head>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {ist_time}</p>
            <pre><strong>Top Output:</strong><br>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
