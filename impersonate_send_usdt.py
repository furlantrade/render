from web3 import Web3
import json

# Conecta ao Anvil
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Endereço da conta rica em USDT (ou outro token ERC20)
impersonated_address = "0xF977814e90dA44bFA03b6295A0616a897441aceC"

# Endereço do contrato USDT
usdt_contract_address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"

# ABI mínima do ERC20
erc20_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_to", "type": "address"},
            {"name": "_value", "type": "uint256"},
        ],
        "name": "transfer",
        "outputs": [{"name": "", "type": "bool"}],
        "type": "function",
    }
]

# Inicializa contrato
usdt = w3.eth.contract(address=usdt_contract_address, abi=erc20_abi)

# Destinatário (por exemplo, conta #0 do anvil)
receiver = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"

# Impersona conta
w3.provider.make_request("anvil_impersonateAccount", [impersonated_address])

# Monta transação de transferência de USDT
tx = usdt.functions.transfer(receiver, 10_000_000).build_transaction({
    'from': impersonated_address,
    'gas': 100_000,
    'maxFeePerGas': w3.to_wei(10, 'gwei'),
    'maxPriorityFeePerGas': w3.to_wei(1.5, 'gwei'),
    'nonce': w3.eth.get_transaction_count(impersonated_address),
    'chainId': 1
})

# Envia transação
tx_hash = w3.eth.send_transaction(tx)
print("TX hash:", tx_hash.hex())

# Para de impersonar
w3.provider.make_request("anvil_stopImpersonatingAccount", [impersonated_address])
