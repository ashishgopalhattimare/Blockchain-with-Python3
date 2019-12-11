import json
from web3 import Web3


def readFromFile(path):
	filex = open(path, 'r')
	
	data = filex.read().strip()
	filex.close()
	
	return data


if __name__ == '__main__':

	url = "http://127.0.0.1:7545"
	web3 = Web3(Web3.HTTPProvider(url))
	
	abi = json.loads(readFromFile('abi.txt'))
	contractAddress = readFromFile('address.txt')
	
	contract = web3.eth.contract(address = contractAddress, abi = abi)
	
	if web3.isConnected() == True and len(contractAddress) != 0:
	
		print("|| Welcome To the Network ||", end = '\n\n')
		
		print("Supplier Address : ", end = '')
		supplier = input().strip()
		
		print("Customer Address : ", end = '')
		customer = input().strip()
		
		print("Data : ", end = '')
		data = input().strip()
		
		web3.eth.defaultAccount = customer
		
		tx_hash = contract.functions.addContract(supplier, customer, data).transact()
		tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
		
		print("Contract : {}".format(tx_receipt.contractAddress))

		#print(contract.functions.greet().call())
		
	else:
		print('URL not Found')
