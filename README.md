# Synchronous and asynchronous client for coinpayments.net (New API)

Before use, it is advisable to familiarize yourself with the official CoinPayments documentation (https://docs.coinpayments.net/api). The application implements the interaction protocol described in this document.

Note: The function of this library is currently limited to handling automatic authentication for requests. That is why it has only one method (`.request`) for making requests.
## Installation

```
pip install git+https://github.com/HK-Mattew/python-coinpayments.git@new-api
```

## Synchronous usage example

```python
from coinpayments import Client


def main():

    cp = Client(
        client_id="<your-client-id>",
        client_secret="<your-client-secret>",
    )

    # Create wallet
    print(
        cp.request(
            method="POST",
            endpoint="https://a-api.coinpayments.net/api/v2/merchant/wallets",
            json={"currency": "BTC", "label": "Wallet creation test via API"},
        )
    )

    # Get wallets
    print(
        cp.request(
            method="GET",
            endpoint="https://a-api.coinpayments.net/api/v2/merchant/wallets",
        )
    )


if __name__ == "__main__":
    main()

```

## Asynchronous usage example

```python
import asyncio

from coinpayments import AsyncClient


async def main():

    cp = AsyncClient(
        client_id="<your-client-id>",
        client_secret="<your-client-secret>",
    )

    # Create wallet
    print(
        await cp.request(
            method="POST",
            endpoint="https://a-api.coinpayments.net/api/v2/merchant/wallets",
            json={"currency": "BTC", "label": "Wallet creation test via API"},
        )
    )

    # Get wallets
    print(
        await cp.request(
            method="GET",
            endpoint="https://a-api.coinpayments.net/api/v2/merchant/wallets",
        )
    )


if __name__ == "__main__":
    asyncio.run(main())

```
