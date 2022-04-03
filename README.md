<h1 align="center">
<sub>
    <img src=".github/icon.png" height="36">
</sub>
&nbsp;
discord-ext-oauth
</h1>
<p align="center">
<sup>
An asynchronous OAuth2 extension for discord.py.
</sup>
<br>
<sup>
    <a href="">Read the documentation online.</a>
</sup>
</p>

[![Documentation Status](https://readthedocs.org/projects/discordextoauth/badge/?version=latest)](https://discordextoauth.readthedocs.io/en/latest/?badge=latest)

***
## Installing the extension
> Installing the stable version:
> ```sh
> pip install discord-ext-oauth
> ```

> Installing the development version:
> ```sh
> pip install git+https://github/justanotherbyte/discord-ext-oauth
> ```

## Example Usage
```py
import asyncio
from discord.ext import oauth

client = oauth.OAuth2Client(
    client_id = 000000000000000000,
    client_secret = "CLIENT_SECRET",
    redirect_uri = "https://www.google.com/",
    scopes = ["identify",  "guilds", "email", "connections"]
)


async def main():
    resp = await client.exchange_code("access_token_here")
    user = await client.fetch_user(resp)
    print(f"User ID: {user.id}")
    print(f"User Avatar URL: {user.avatar_url}")
    await client.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```
> Output
> ```sh
> User ID: 691406006277898302
> User Avatar URL: https://cdn.discordapp.com/avatars/691406006277898302/5c8f69a903a8c5e34f93fe6ece5348c7.png 
> ```


