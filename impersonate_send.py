from web3 import Web3
import sys

target = sys.argv[1]
amount = sys.argv[2]

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Impersona a conta
w3.provider.make_request("anvil_impersonateAccount", [target])
print(f"Impersonando: {target}")

tx = {
    'from': target,
    'to': w3.eth.accounts[0],
    'value': w3.to_wei(int(amount), 'ether'),
    'gas': 21000,
    'gasPrice': w3.to_wei('1', 'gwei'),
}

tx_hash = w3.eth.send_transaction(tx)
print(f"Enviado {amount} ETH: {tx_hash.hex()}")