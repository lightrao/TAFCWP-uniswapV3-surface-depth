import requests
import json
import os
from dotenv import load_dotenv
import func_triangular_arb_v2


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
    pairs = retrieve_uniswap_information()["data"]["pools"]
    structured_pairs = func_triangular_arb_v2.structure_trading_pairs(pairs, 100)
    print(len(structured_pairs))
