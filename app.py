from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Gather system details
    name = "Amrit Raj"  # Replace with your full name
    username = os.getlogin()
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %Z')
    top_output = subprocess.getoutput("top -b -n 1")

    # HTML to display
    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre><strong>Top Output:</strong><br>{top_output}</pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
