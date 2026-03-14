# lzt-api

Python API wrapper for Lolzteam Forum & Market. Supports sync and async. Auto-generated from OpenAPI schemas.

## Installation

```bash
pip install lzt-api
```

## Quick Start

### Sync

```python
from lzt_api.forum import ForumClient
from lzt_api.market import MarketClient

forum = ForumClient(token="your_token")
threads = forum.threads_list()
print(threads)

market = MarketClient(token="your_token")
accounts = market.category_list()
print(accounts)
```

### Async

```python
import asyncio
from lzt_api.forum import AsyncForumClient
from lzt_api.market import AsyncMarketClient

async def main():
    async with AsyncForumClient(token="your_token") as forum:
        threads = await forum.threads_list()
        print(threads)

    async with AsyncMarketClient(token="your_token") as market:
        accounts = await market.category_list()
        print(accounts)

asyncio.run(main())
```

### Proxy

```python
forum = ForumClient(token="your_token", proxy="http://user:pass@proxy:8080")
```

### Error Handling

```python
from lzt_api.exceptions import RateLimitError, AuthError, NotFoundError

try:
    result = forum.threads_get(thread_id=123)
except RateLimitError as e:
    print(f"Rate limited, retry after {e.retry_after}s")
except AuthError:
    print("Invalid token")
except NotFoundError:
    print("Thread not found")
```

## Code Generation

Methods and models are auto-generated from OpenAPI schemas. To regenerate:

```bash
pip install jinja2

python -m codegen.generate --schema schemas/forum.json --output src/lzt_api/forum/ --class-name ForumClient
python -m codegen.generate --schema schemas/market.json --output src/lzt_api/market/ --class-name MarketClient
```

## Features

- Sync and async support via httpx
- Auto-retry on 429/502/503 with exponential backoff
- Proxy support
- Pydantic v2 models for response schemas
- 151 forum methods, 115 market methods

## License

MIT
