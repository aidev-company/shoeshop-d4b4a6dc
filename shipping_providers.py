import requests
from typing import Dict

class ShippingProviders:
    def __init__(self):
        self.providers = ['usps', 'ups', 'fedex']
        self.api_keys = {
            'usps': 'YOUR_USPS_API_KEY',
            'ups': 'YOUR_UPS_API_KEY',
            'fedex': 'YOUR_FEDEX_API_KEY'
        }
    
    def get_estimates(self, order_data: Dict) -> Dict:
        estimates = {}
        for provider in self.providers:
            api_key = self.api_keys[provider]
            response = requests.post(f'https://{provider}.com/estimate', headers={'Authorization': f'Bearer {api_key}'}, json=order_data)
            if response.status_code == 200:
                estimates[provider] = response.json()
            else:
                estimates[provider] = {'error': 'Failed to retrieve estimate'}
        return estimates
    
    def track_update(self, tracking_data: Dict) -> Dict:
        updates = {}
        for provider in self.providers:
            api_key = self.api_keys[provider]
            response = requests.post(f'https://{provider}.com/track', headers={'Authorization': f'Bearer {api_key}'}, json=tracking_data)
            if response.status_code == 200:
                updates[provider] = response.json()
            else:
                updates[provider] = {'error': 'Failed to retrieve tracking update'}
        return updates