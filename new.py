from web3 import Web3
import json
from decouple import config



# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/12ced2b8c0224216bbee1b0b3ee4d5d7'))
res = w3.isConnected()
#print(res)

latest_block = w3.eth.get_block('latest')

#print(latest_block)

check_sum = w3.toChecksumAddress('0xb6Ab3dF4E3Dc5C02b46e21a266C561856EDbd5DD')
balance = w3.eth.get_balance(check_sum)
#print(balance)

ether_value  = w3.fromWei(balance, 'ether')
print("NILAI")
print(ether_value)


trans = w3.eth.get_transaction('0x51d5bd6509ce344b7bd41f9fbf5e81378361c8ce7c2104a2eb4c394721e12fe7')
# trans = w3.eth.get_transaction('0xa89a3424b6ccfc0fa5933ded7c520b84d627065707f892dcd0440bd55a176020')
transJson = Web3.toJSON(trans)
print(transJson)
datanya = str(transJson)
# print(datanya.find('0xAff3E5c0594b9255020B328d0fc2c8B138872C6F'))
ubahLagi = json.loads(transJson)
nomorBlok = ubahLagi["blockNumber"]
print("NOMOR BLOK")
print(nomorBlok)
