from web3 import Web3
import json

# Conecta ao Anvil
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Endereço a ser impersonado
target_address = "0x0f87243a64FFfaFa91f50Fa5a8ee918430A38fBA"

# Endereço que receberá os ETH
receiver = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

# Impersona a conta
w3.provider.make_request("anvil_impersonateAccount", [target_address])

# Monta transação
tx = {
    'from': target_address,
    'to': receiver,
    'value': w3.to_wei(1000, 'ether'),
    'gas': 21000,
    'maxFeePerGas': w3.to_wei(10, 'gwei'),
    'maxPriorityFeePerGas': w3.to_wei(1.5, 'gwei'),
}

# Envia transação
tx_hash = w3.eth.send_transaction(tx)
print("TX hash:", tx_hash.hex())

# Para de impersonar
w3.provider.make_request("anvil_stopImpersonatingAccount", [target_address])
