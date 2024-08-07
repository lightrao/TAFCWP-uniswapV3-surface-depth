# Structure trading pair groups
def structure_trading_pairs(pairs, limit):

    triangular_pairs_list = []
    remove_duplicates_list = []
    pairs_list = pairs[:limit]

    # Loop through each coin to find potential matches
    for pair_a in pairs_list:

        # Get first pair (A)
        a_base = pair_a["token0"]["symbol"]
        a_quote = pair_a["token1"]["symbol"]
        print(a_base)
        a_pair = a_base + "_" + a_quote
        a_token_0_id = pair_a["token0"]["id"]
        a_token_1_id = pair_a["token1"]["id"]
        a_contract = pair_a["id"]
        a_token_0_decimals = pair_a["token0"]["decimals"]
        a_token_1_decimals = pair_a["token1"]["decimals"]
        a_token_0_price = pair_a["token0Price"]
        a_token_1_price = pair_a["token1Price"]
