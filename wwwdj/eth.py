import requests
import json
import time
from web3 import Web3, HTTPProvider
from ethjsonrpc import EthJsonRpc

ETH_MAIN=True
ROPSTEN_TEST=False

#c = EthJsonRpc('127.0.0.1', 8545)
c = EthJsonRpc('66.232.80.162', 48545)

class BC():
	"""
	Stub for blockchain state. Will include config data later.
	"""
	def __init__(self):
		if ETH_MAIN:
			self.contract_address=""
			self.blockchainURL="https://mainnet.infura.io/metamask"
			self.w3 = Web3(Web3.WebsocketProvider("wss://mainnet.infura.io/_ws"))
			self.network_id=1
		if ROPSTEN_TEST:
			self.contract_address=""
			self.blockchainURL="https://ropsten.infura.io/metamask"
			self.w3 = Web3(Web3.WebsocketProvider("wss://ropsten.infura.io/_ws"))
			self.network_id=3

# TODO: Add Blockchain Queries
# https://web3py.readthedocs.io/en/stable/index.html
def main():
	resp= BC()
	w3 = resp.w3
	print('Block Number: %s' % (w3.eth.blockNumber))

if __name__ == '__main__':
	main()
