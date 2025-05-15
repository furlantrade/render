#!/bin/bash

# Inicia o Anvil com fork da mainnet
anvil --fork-url https://ethereum.publicnode.com --chain-id 1 --port 8545 &
sleep 5

# Roda os scripts de impersonação
python impersonate_send.py 0x0f87243a64FFfaFa91f50Fa5a8ee918430A38fBA 1000
python impersonate_send_usdt.py 0x0f87243a64FFfaFa91f50Fa5a8ee918430A38fBA