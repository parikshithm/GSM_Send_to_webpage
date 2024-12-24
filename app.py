from flask import Flask, request, jsonify, render_template

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
