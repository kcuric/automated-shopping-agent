from agent.configuration import configuration

import requests
import json

def check_for_open_orders():
  response = requests.get(
    f'{configuration.SERVER_URL}{configuration.ENDPOINT}',
    params={'assigned': False, 'completed': False}
  )
  if(response.text):
    order_id = json.loads(response.text)
  else:
    order_id = {}
  return order_id

def assign_order(id):
  data = {
    'filter': {'_id': id},
    'data': {
      'agentName': configuration.XMPP_USERNAME, 
      'assigned': True
    }
  }
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  response = requests.put(
    f'{configuration.SERVER_URL}{configuration.ENDPOINT}',
    data=json.dumps(data),
    headers=headers
  ) 

def complete_order(id, transaction):
  data = {
    'filter': {'_id': id},
    'data': transaction
  }
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  response = requests.put(
    f'{configuration.SERVER_URL}{configuration.ENDPOINT}',
    data=json.dumps(data),
    headers=headers
  ) 
