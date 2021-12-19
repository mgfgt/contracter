from typing import Callable
from web3 import Web3
import requests
import os
from dotenv import load_dotenv
from utils import *

load_dotenv()

w3 = Web3(Web3.WebsocketProvider(os.environ["INFURA_URL"]))

is_connected = w3.isConnected()
if (is_connected != True):
    print("Issue connecting to blockchain. Make sure you are using your node's websocket url")
    quit()

target_contract = loop_input_validation("Input contract address: ", Web3.isAddress, "Invalid contract address")
print("Contract:", target_contract)
checksum_target_contract = w3.toChecksumAddress(target_contract)

print("Fetching contract ABI from etherscan...")
etherscan_api_key = os.environ["ETHERSCAN_API_KEY"]
response = requests.get(f"https://api.etherscan.io/api?module=contract&action=getabi&address={target_contract}&apikey={etherscan_api_key}")
abi = response.json()['result']
print("Contract ABI successfully fetched")
contract = w3.eth.contract(checksum_target_contract, abi=abi)

mint_price = loop_input_validation("Input mint price (in eth): ", check_float, "Invalid mint price")
mint_price = float(mint_price)
print("Mint price:", mint_price)
mint_price_wei = Web3.toWei(mint_price, 'ether')

# current_gas = w3.eth.gas_price
# current_gas_eth = w3.fromWei(current_gas, 'eth')
# print("Current gas: ", current_gas_eth, "eth")
# gas_limit = loop_input_validation(f"Input gas limit (in eth): ", check_float, "Invalid gas limit")
# gas_limit = float(gas_limit)
# print("Gas limit:", gas_limit)
# gas_limit_wei = Web3.toWei(gas_limit, 'ether')

# current_max_priority_fee = w3.eth.max_priority_fee
# current_max_priority_fee_eth = w3.fromWei(current_max_priority_fee, "eth")
# print("Current max priority fee: ", current_max_priority_fee_eth, "eth")
# use_max_priority = loop_input_validation("Use max priority? y/n: ", check_yes_or_no, "Invalid input. Type 'y' or 'n'")
# max_priority_gas_limt = use_max_priority == "y" 

wallet = os.environ['WALLET_ADDRESS']
checksum_wallet = w3.toChecksumAddress(wallet)

transaction = {
    "from": checksum_wallet,
    # "to": checksum_target_contract,
    "value": mint_price_wei,
    # "maxFeePerGas": gas_limit_wei,
    # "maxPriorityFeePerGas": use_max_priority,
    # "data": abi
}

# print(contract.all_functions())
mint = contract.functions.mint
# print(mint(4000, wallet).estimateGas(transaction))


# to consider:
# wallet connection and private key signing
# current gas price monitoring

# contract interaction: contract address and abi required


# get wallet address--
# sign wallet
# get contract
# get contract mint function (?)
# get mint price
# get max gas price

# attempt transactions, execute if within max gas price
# attempting a transaction - ping for transaction, check gas on transaction, if unnacceptable loop, if not execute transaction and close script
# to expand further, after a successful transaction it could execute XX many more