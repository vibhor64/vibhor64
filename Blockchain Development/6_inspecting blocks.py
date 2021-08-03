from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY_GOES_HERE"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.eth.blockNumber)
print(web3.eth.getBlock('latest'))
latest = web3.eth.blockNumber
for i in range(0, 10):
  print(web3.eth.getBlock(latest - i))

hash = '0x66b3fd79a49dafe44507763e9b6739aa0810de2c15590ac22b5e2f0a3f502073'
print(web3.eth.getTransactionByBlock(hash, 2))
