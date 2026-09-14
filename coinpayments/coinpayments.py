import json as json_m
from typing import Any, Literal

import httpx
from httpx._types import QueryParamTypes

from ._utils import gen_cp_auth_signature as _gen_cp_auth_signature


class Client:
    def __init__(self, client_id: str, client_secret: str):
        self._client_id = client_id
        self._client_secret = client_secret

    def request(
        self,
        method: Literal["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "PATCH"],
        endpoint: str,
        params: QueryParamTypes | None = None,
        json: Any | None = None,
    ):
        body = json_m.dumps(
            json,
            separators=(",", ":"),
            ensure_ascii=False,
        )

        request = httpx.Request(
            method=method,
            url=endpoint,
            content=body or None,
            params=params,
        )

        iso_date, hmac_signature = _gen_cp_auth_signature(
            http_method=method,
            api_endpoint=str(
                request.url
            ),  # Use request.url to include the query parameters.
            client_id=self._client_id,
            client_secret=self._client_secret,
            body=body,
        )

        request.headers.update(
            {
                "Content-Type": "application/json",
                "X-CoinPayments-Client": self._client_id,
                "X-CoinPayments-Timestamp": iso_date,
                "X-CoinPayments-Signature": hmac_signature,
            }
        )

        with httpx.Client() as client:
            response = client.send(request)
            response.raise_for_status()
            return response.json()
