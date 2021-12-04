# multicall
To test the multi call with ChainLink ETH/USD data feed contract

Set your PRIVATE_KEY and WEB3_INFURA_PROJECT_ID into .env file and run below to test the script:

brownie run scripts/multicall.py --network mainnet

As the data feed is read operation, no transaction fee will incur from the caller.
