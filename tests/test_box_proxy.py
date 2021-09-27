from scripts.helpful_scripts import get_account, encode_function_data
from brownie import Box, ProxyAdmin, TransparentUpgradeableProxy, Contract


def test_proxy_delegates_calls():
    account = get_account() # Get account
    box = Box.deploy({'from': account}) # Deploy box contract
    proxy_admin = ProxyAdmin.deploy({'from': account}) # Deploy proxy admin contract
    box_encoded_initializer_function = encode_function_data() 
    proxy = TransparentUpgradeableProxy.deploy( # Deploy upgradeable proxy
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {'from': account, 'gas_limit':1000000}
    )
    proxy_box = Contract.from_abi('Box', proxy.address, Box.abi) # get contract from abi
    assert proxy_box.retrieve() == 0 # Assert the value hasn't changed
    proxy_box.store(1, {'from': account}) # Change value
    assert proxy_box.retrieve() == 1 # Assert the value changed