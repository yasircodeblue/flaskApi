from flask import Flask, jsonify
import socket
import uuid

app = Flask(__name__)

def get_mac_address():
    # Get the MAC address of the first network interface
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
    return mac

def get_ip_address():
    # Get the IP address of the machine
    ip = socket.gethostbyname(socket.gethostname())
    return ip

@app.route('/get_user_info', methods=['GET'])
def get_user_info():
    # Get the user's IP address
    user_ip = get_ip_address()

    # Get the hashed MAC address
    hashed_mac = get_mac_address()

    # Prepare the response JSON
    response_data = {
        'ip_address': user_ip,
        'mac_address': hashed_mac
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

