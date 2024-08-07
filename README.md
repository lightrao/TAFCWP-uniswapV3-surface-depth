# Uniswap V3 Triangular Arbitrage

## Uniswap V3 - Calculating Surface Rates

create python virtual environment: go to `https://code.visualstudio.com/docs/python/environments`

Understanding Uniswap V3 Graph QL:
go to:
`https://thegraph.com/explorer/subgraphs/5zvR82QoaXYFyDEKLZ9t6v9adgnptxYpKpSbxtgVENFV?view=Query&chain=arbitrum-one`
`https://thegraph.com/hosted-service/subgraph/uniswap/uniswap-v3`

GraphQL:

```
{
  pools(orderBy:totalValueLockedETH,orderDirection:desc,first:5) {
    id
    totalValueLockedUSD
    totalValueLockedETH
    token1Price
    token0Price
    feeTier
    token1 {
      decimals
      id
      symbol
      name
    }
    token0 {
      id
      symbol
      name
      decimals
    }
  }
}
```

Pulling Liquid Uniswap Pool Prices

```shell
pip install python-dotenv
pip freeze > requirements.txt
python python main_v2.py
```

Structuring Triangular Groups - Part 1

Structuring Triangular Groups - Part 2
