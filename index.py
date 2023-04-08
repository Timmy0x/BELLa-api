import json
from web3 import Web3

class bella:
    def __init__(self, infura_key, contract_address="0x774af2094da02af3ce8695f566ba9d7cd421718d"):
      self.abi = [{ "inputs": [ { "internalType": "string", "name": "text", "type": "string" } ], "name": "add_text", "outputs": [], "stateMutability": "nonpayable", "type": "function" }, { "inputs": [], "stateMutability": "nonpayable", "type": "constructor" }, { "inputs": [ { "internalType": "string", "name": "prompt", "type": "string" }, { "internalType": "uint256", "name": "length", "type": "uint256" } ], "name": "generate_text", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "", "type": "string" }, { "internalType": "string", "name": "", "type": "string" } ], "name": "model", "outputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "owner", "outputs": [ { "internalType": "address", "name": "", "type": "address" } ], "stateMutability": "view", "type": "function" }, { "inputs": [], "name": "show_words", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "view", "type": "function" }, { "inputs": [ { "internalType": "string", "name": "text", "type": "string" } ], "name": "tokenize_text", "outputs": [ { "internalType": "string[]", "name": "", "type": "string[]" } ], "stateMutability": "pure", "type": "function" }, { "inputs": [ { "internalType": "uint256", "name": "", "type": "uint256" } ], "name": "words", "outputs": [ { "internalType": "string", "name": "", "type": "string" } ], "stateMutability": "view", "type": "function" }]
      self.provider = "https://polygon-mainnet.infura.io/v3/" + infura_key
      self.web3 = Web3(Web3.HTTPProvider(provider))
      self.contract_address = Web3.toChecksumAddress(contract_address)
      self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)
        
    def generate_text(self, prompt, length):
        prompt = str(prompt)
        length = int(length)
        try:
            result = self.contract.functions.generate_text(prompt, length).call()
            return result
        except:
            return "returned error, check for invalid input"
