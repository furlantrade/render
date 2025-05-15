from web3 import Web3
import sys

target = sys.argv[1]
USDT_ADDRESS = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
ABI = [{
    "constant": False,
    "inputs": [
        {"name": "_to", "type": "address"},
        {"name": "_value", "type": "uint256"}
    ],
    "name": "transfer",
    "outputs": [{"name": "", "type": "bool"}],
    "type": "function"
}]

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Impersona a conta
w3.provider.make_request("anvil_impersonateAccount", [target])
print(f"Impersonando: {target}")

usdt = w3.eth.contract(address=USDT_ADDRESS, abi=ABI)

tx = usdt.functions.transfer(w3.eth.accounts[0], 10000000).build_transaction({
    'from': target,
    'gas': 100000,
    'gasPrice': w3.to_wei('1', 'gwei'),
    'nonce': w3.eth.get_transaction_count(target),
})

signed_tx = w3.eth.account.sign_transaction(tx, private_key="0x00")
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("USDT enviado:", tx_hash.hex())