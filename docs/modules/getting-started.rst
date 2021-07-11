Getting Started
===============

Example Usage
=============

.. code-block:: python

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

.. code-block:: guess

    >>> User ID: 691406006277898302
    >>> User Avatar URL: https://cdn.discordapp.com/avatars/691406006277898302/5c8f69a903a8c5e34f93fe6ece5348c7.png 

