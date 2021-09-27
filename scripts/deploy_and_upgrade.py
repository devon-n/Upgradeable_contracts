from scripts.helpful_scripts import get_account, encode_function_data, upgrade
from brownie import Box, network, ProxyAdmin, TransparentUpgradeableProxy, Contract, BoxV2

def main():
    # Deploy
    account = get_account()
    print(f'Deploying to {network.show_active()}')
    box = Box.deploy({'from': account})
    proxy_admin = ProxyAdmin.deploy({'from':account})
    initializer = box.store, 1
    box_encoded_initializer_function = encode_function_data()

    # Deploy Proxy
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {'from':account, 'gas_limit': 1000000}
    )
    print(f'Proxy deployed to {proxy}, you can now upgrade to v2!')
    proxy_box = Contract.from_abi('Box', proxy.address, Box.abi)

    # Use Proxy
    proxy_box.store(100, {'from':account})
    print(proxy_box.retrieve())

    # Box V2 Deploy
    box_v2 = BoxV2.deploy({'from':account})

    # Upgrade Contract
    upgrade_transaction = upgrade(account, proxy, box_v2.address, proxy_admin_contract=proxy_admin)
    upgrade_transaction.wait(1)
    print('Proxy has been upgraded!')
    
    # User proxy
    proxy_box = Contract.from_abi('BoxV2', proxy.address, BoxV2.abi)
    proxy_box.increment({'from': account})
    print(proxy_box.retrieve())