import asyncio
from discord_web.oauth2 import Oauth2Client

client = Oauth2Client(770301542170361896, "IEPPgpA6JvDL4ZYf7OAqNI7RMUxH1TVN", "http://localhost:8000", ["identify", "guilds"])


async def main():
    token = await client.exchange_code("ANV9d7cOeRV52KQCO6Yf9cmJrEY06a")
    member = await client.fetch_member(token.access_token)
    guilds = await member.fetch_guilds()
    for guild in guilds:
        print(guild)
    

    



loop = asyncio.get_event_loop()
loop.run_until_complete(main())