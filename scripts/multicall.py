from brownie import Contract, interface, multicall

ETH_USD_FEED_ADDRESS = "0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419"
UNISWAP_MULTICALL2 = "0x5BA1e12693Dc8F9c48aAD8770482f4739bEeD696"

def main():
    price_feed = Contract.from_abi(
        "feed", 
        ETH_USD_FEED_ADDRESS,
        interface.AggregatorV3Interface.abi)

    rounds = []
    latest_round = price_feed.latestRoundData()[0]
    multicall(address=UNISWAP_MULTICALL2)
    with multicall:
        for round_id in range(latest_round, latest_round - 50, -1):
            round_data = price_feed.getRoundData(round_id)
            rounds.append(round_data)
    print(rounds)
