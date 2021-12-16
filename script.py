from typing import Callable
from web3 import Web3
import requests
import os
from dotenv import load_dotenv

load_dotenv()

w3 = Web3(Web3.EthereumTesterProvider())

def loop_input_validation(prompt: str, validator: Callable[[str], bool], message: str):
    while True:
        value = input(prompt)
        if not validator(value):
            print(message)
            continue
        return value

target_contract = loop_input_validation("Input contract address: ", Web3.isAddress, "Invalid contract address")
print("Contract:", target_contract)

# def check_float(val):
#     try:
#         float(val)
#         return True;
#     except:
#         return False;

# mint_price = loop_input_validation("Input mint price (in eth): ", check_float, "Invalid mint price")
# mint_price = float(mint_price)
# print("Mint price:", mint_price)
# mint_price_wei = Web3.toWei(mint_price, 'ether')

# gas_limit = loop_input_validation("Input gas limit (in eth): ", check_float, "Invalid gase limit")
# gas_limit = float(gas_limit)
# print("Gas limit:", gas_limit)
# gas_limit_wei = Web3.toWei(gas_limit, 'ether')

# print(w3.eth.accounts)
# print(w3.eth.gas_price)
# print(w3.eth.max_priority_fee)

etherscan_api_key = os.environ["ETHERSCAN_API_KEY"]
request_string = f"https://api.etherscan.io/api?module=contract&action=getabi&address={target_contract}&apikey={etherscan_api_key}"
print(request_string)
# response = requests.get(f"https://api.etherscan.io/api?module=contract&action=getabi&address={target_contract}&apikey={etherscan_api_key}")
# print(response)

# print("Input wallet address")
# wallet = input()


# to consider:
# wallet connection and private key signing
# current gas price monitoring

# contract interaction: contract address and abi required