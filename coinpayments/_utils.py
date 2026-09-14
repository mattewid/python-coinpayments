import base64
import hashlib
import hmac
from datetime import datetime, timezone


def gen_cp_auth_signature(
    http_method: str,
    api_endpoint: str,
    client_id: str,
    client_secret: str,
    body: str,
) -> tuple[str, str]:
    """
    Doc Ref: https://docs.coinpayments.net/api/auth/generate-api-signature/

    :return: Iso date, signature
    :rtype: tuple[str, str]
    """

    iso_date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    message = f"\ufeff{http_method.upper()}{api_endpoint}{client_id}{iso_date}{body}"

    signature = base64.b64encode(
        hmac.new(
            client_secret.encode(),
            message.encode(),
            hashlib.sha256,
        ).digest()
    ).decode()
    return iso_date, signature
