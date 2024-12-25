from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Variable to store data (simulating GSM communication)
gsm_data = ""

# Route to serve the HTML page and handle query parameters
@app.route('/')
def index():
    # Get the "data" parameter from the URL
    data_from_url = request.args.get('data', '')  # Default to an empty string if no data is provided
    print(f"Data received via URL: {data_from_url}")  # Debug log for Render Logs
    return render_template('index.html', url_data=data_from_url)

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
    print(f"Data received from web page: {data}")  # Log the received data in Render Logs
    return jsonify({"status": "success", "message": "Data sent to GSM successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
