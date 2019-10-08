import asyncio
import json

from async_swgoh_help import async_swgoh_help, settings


# Change the settings below
#creds = settings('deesnow', 'R594HXam8guw')
creds = settings('deesnow', 'R594HXam8guw')
client = async_swgoh_help(creds)

allycodes = [376764962]


async def guild():
    print("getGuild called")
    # zetas = await client.fetchZetas()
    # return zetas['zetas']   --- EZ OK
    guild_allycodes = await client.fetchGuilds(allycodes)

    print("getGuild return")

    return guild_allycodes

async def player():
    print("getPLayer called")
    player = await client.fetchPlayers(allycodes)
    print("getPLayer return")
    return player


async def main():
    t1 = loop.create_task(guild())
    t2 = loop.create_task(player())
    await t1
    await t2
    return t1._result, t2._result




if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    t1, t2  = loop.run_until_complete(main())
    print(t1, t2)
    
    