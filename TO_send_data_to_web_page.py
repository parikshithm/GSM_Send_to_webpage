from flask import Flask, request, jsonify, render_template
import threading
import requests
import time

app = Flask(__name__)

# Variable to store data (simulating GSM communication)
gsm_data = ""

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # Ensure the HTML file is in a "templates" folder

# Endpoint to fetch real-time data (used by the webpage)
@app.route('/get-gsm-data', methods=['GET'])
def get_gsm_data():
    global gsm_data
    return jsonify({"data": gsm_data}), 200  # Send the latest GSM data as JSON

# Endpoint to receive data from the webpage and simulate sending it to the GSM module
@app.route('/send-gsm-data', methods=['POST'])
def send_gsm_data():
    global gsm_data
    # Get the data from the POST request
    data = request.json.get('data', '')
    gsm_data = data  # Update the global variable to simulate sending to the GSM module
    print(f"Data received from web page: {data}")  # Log the received data in the terminal
    return jsonify({"status": "success", "message": "Data sent to GSM successfully"}), 200

# Function to send data to Flask dynamically using user input
def send_data_to_flask():
    url = "http://127.0.0.1:5000/send-gsm-data"
    while True:
        data = input("Enter data to send to Flask: ")  # Prompt user for input
        response = requests.post(url, json={"data": data})
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print("Failed to send data!")

# Function to start the Flask server in a separate thread
def run_flask():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

# Main script
if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Start the user input loop in the main thread
    send_data_to_flask()
