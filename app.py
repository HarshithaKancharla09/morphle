from flask import Flask
import os
from datetime import datetime
import subprocess
import pytz
app = Flask(__name__)
@app.route("/htop")
def htop():
    full_name = "Your Full Name"
    try:
        username = os.getlogin()
    except Exception:
        username = os.environ.get("USER", "unknown")
    ist_tz = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist_tz).strftime("%Y-%m-%d %H:%M:%S.%f")
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"], universal_newlines=True)
    except Exception as e:
        top_output = "Error retrieving top output: " + str(e)
    html_output = f"""
    <html>
      <head>
        <title>/htop Endpoint</title>
      </head>
      <body>
        <pre>
Name: {full_name}
Username: {username}
Server Time (IST): {server_time}

TOP output:
{top_output}
        </pre>
      </body>
    </html>
    """
    return html_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
