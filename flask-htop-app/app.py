from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask HTOP App! Visit /htop to see system info."

@app.route('/htop')
def htop():
    # Set system username manually
    username = "jafre0912"

    # Get current server time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S")

    # Get top command output
    try:
        top_output = subprocess.check_output("top -bn1 | head -15", shell=True, text=True)
    except Exception as e:
        top_output = f"Error retrieving top output: {str(e)}"

    # Create response
    response = f"""
    <h2>Name: Jafre Alam</h2>
    <h2>User: {username}</h2>
    <h2>Server Time (IST): {formatted_time}</h2>
    <h2>TOP Output:</h2>
    <pre>{top_output}</pre>
    """

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
