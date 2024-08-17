import pytest
import httpx
import asyncio
from starlette.status import HTTP_429_TOO_MANY_REQUESTS
from app.routers.endpoints import router


@pytest.mark.asyncio
async def test_rate_limiter():
    # Setup
    async with httpx.AsyncClient(app=router, base_url="http://testserver") as client:
        endpoint = "api/transactions/"
        total_requests = 1000
        limit_per_minute = 20

        tasks = [client.post(endpoint, json={"data": "test"}) for _ in range(total_requests)]
        responses = await asyncio.gather(*tasks)

        too_many_requests_count = sum(1 for response in responses if response.status_code == HTTP_429_TOO_MANY_REQUESTS)

        assert too_many_requests_count > 0, "Rate limiter did not block any requests"

        assert too_many_requests_count >= total_requests - limit_per_minute, (
            f"Expected at least {total_requests - limit_per_minute} requests to be blocked, "
            f"but only {too_many_requests_count} were blocked."
        )
