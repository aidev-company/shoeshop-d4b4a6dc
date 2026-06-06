import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from shipping_providers import ShippingProviders

app = Flask(__name__)
CORS(app)

shipping_providers = ShippingProviders()

@app.route('/shipping-estimates', methods=['POST'])
def get_shipping_estimates():
    order_data = request.get_json()
    estimates = shipping_providers.get_estimates(order_data)
    return jsonify(estimates)

@app.route('/track-shipping', methods=['POST'])
def track_shipping():
    tracking_data = request.get_json()
    updates = shipping_providers.track_update(tracking_data)
    return jsonify(updates)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)