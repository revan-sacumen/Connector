"""Send request handler."""
from sac_requests.constants.general import HTTPS
from sac_requests.context.config import HttpConfig
from sac_requests.context.headers import HttpHeaders
from sac_requests.context.request import HttpRequest, Response
from sac_requests.context.url import HttpURL
from sac_requests.exceptions.base import HttpRequestError

from src.confige import API_URL, logger  # type: ignore


class ApiRequest:
    """Send Request to API and get Response Handling Exception."""

    def __init__(self, api_key: str) -> None:
        """Initialize required key.

        Args:
            api_key (str): access key for send request.
        """
        self.url = API_URL
        self.api_key = api_key

    @staticmethod
    def create_config() -> HttpConfig:
        """Require configuration."""
        return HttpConfig(
            timeout=5,
            retry_interval=1,
            status_force_list=[429, 500, 502, 503, 504, 422],
            max_retry=1,
            auth_type="BEARER_TOKEN",
        )

    def send_request_config(self, path: str, query: str, param: str) -> Response:
        """Send request and get response.

        Args:
            path (str): path of the url.
            query (str): pass required query.
            param (str): pass parameter get which response data.

        Returns:
            response : after send request response data will get.
        """
        config = self.create_config()
        http_url = HttpURL(host=self.url, protocol=HTTPS, )
        headers = HttpHeaders({
            'apikey': self.api_key,
            'Content-Type': 'application/json; charset=utf-8'
        })
        endpoint = f'{path}?{query}={param}'
        http_request = HttpRequest(headers=headers, url=http_url, config=config)
        response = Response()
        try:
            logger.info("request has been sent.")
            response = http_request.get(endpoint=endpoint)
            logger.info("response has been received.")
        except HttpRequestError as msg:
            response.status_code = msg.errcode
            logger.error("Response got error:%s", msg.message)
        return response
