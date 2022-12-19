from web3 import Web3
from solcx import compile_source

account_from = {
    'private_key': '4b740f97a8bb8a94ed07f71f1d658a529667ccb23249a19c00fccc50154e3c3a',
    'address': '0xb6Ab3dF4E3Dc5C02b46e21a266C561856EDbd5DD',
}

account_to = '0xCf52fE8Eb57961E22A42775ec3326E936E69ceF2'


compiled_sol = compile_source(
     '''
    pragma solidity >0.5.0;

     contract Greeter {
         string public greeting;

         constructor() public {
             greeting = 'hai cok';
         }

         function setGreeting(string memory _greeting) public {
             greeting = _greeting;
         }

         function greet() view public returns (string memory) {
             return greeting;
         }
     }
    ''',
    output_values=['abi', 'bin']
)
contract_id, contract_interface = compiled_sol.popitem()
bytecode = contract_interface['bin']
abi = contract_interface['abi']

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/12ced2b8c0224216bbee1b0b3ee4d5d7'))
res = w3.isConnected()
print(res)


Incrementer = w3.eth.contract(abi=abi, bytecode=bytecode)

# 5. Build constructor tx
construct_txn = Incrementer.constructor().buildTransaction(
    {        
        'from': account_from['address'],
        'nonce': w3.eth.get_transaction_count(account_from['address']),
    }
)

# 6. Sign tx with PK
tx_create = w3.eth.account.sign_transaction(construct_txn, account_from['private_key'])

# 7. Send tx and wait for receipt
tx_hash = w3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Contract deployed at address: { tx_receipt.contractAddress }')
