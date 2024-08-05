import requests
import json
import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

subgraphs_api_key = os.getenv("subgraphs_api_key")

""" RETRIEVE GRAPH QL MID PRICES FOR UNISWAP"""


def retrieve_uniswap_information():

    query = """
         {
              pools (orderBy: totalValueLockedETH, 
                orderDirection: desc,
                first:500) 
                {
                    id
                    totalValueLockedETH
                    token0Price
                    token1Price
                    feeTier
                    token0 {id symbol name decimals}
                    token1 {id symbol name decimals}
                }
        }
    """

    url = f"https://gateway-arbitrum.network.thegraph.com/api/{subgraphs_api_key}/subgraphs/id/HUZDsRpEVP2AvzDCyzDHtdc64dyDxx8FQjzsmqSg4H3B"
    req = requests.post(url, json={"query": query})
    json_dict = json.loads(req.text)
    return json_dict


if __name__ == "__main__":
    mid_prices = retrieve_uniswap_information()
    print(mid_prices["data"]["pools"][0])
