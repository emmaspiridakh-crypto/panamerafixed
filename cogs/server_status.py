"""
cogs/server_status.py
------------------------
Requirement #10. 4 voice channels λειτουργούν ως "οθόνες":
    - Members (χωρίς bots)
    - Online Members (χωρίς bots)
    - Boosts
    - Bots

Ενημερώνονται ΑΜΕΣΩΣ σε κάθε σχετικό event (join/leave/status/boost),
όχι σε χρονοδιάγραμμα. ΠΡΟΣΟΧΗ: Το Discord έχει ΔΙΚΟ ΤΟΥ rate limit στο
rename channel (περίπου 2 φορές/10 λεπτά ανά channel) — αυτό είναι platform
limit, όχι κάτι που μπορούμε να παρακάμψουμε. Ο κώδικας πάντως προσπαθεί
να κάνει update αμέσως κάθε φορά.

ΑΠΑΡΑΙΤΗΤΟ: στο main.py πρέπει να είναι ενεργό intents.members = True και
intents.presences = True, αλλιώς δεν θα δουλέψει το online count.
"""

from __future__ import annotations

import discord
from discord.ext import commands

import config
from emojis import emoji

_last_values: dict[str, int] = {}


def _counts(guild: discord.Guild):
    members = sum(1 for m in guild.members if not m.bot)
    online = sum(1 for m in guild.members if not m.bot and m.status != discord.Status.offline)
    bots = sum(1 for m in guild.members if m.bot)
    boosts = guild.premium_subscription_count or 0
    return members, online, boosts, bots


class ServerStatus(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def update_stats(self, guild: discord.Guild):
        members, online, boosts, bots = _counts(guild)

        targets = {
            "members": (config.STATUS_MEMBERS_CHANNEL_ID, f"👥 Members: {members}"),
            "online": (config.STATUS_ONLINE_CHANNEL_ID, f"🟢 Online: {online}"),
            "boosts": (config.STATUS_BOOSTS_CHANNEL_ID, f"🚀 Boosts: {boosts}"),
            "bots": (config.STATUS_BOTS_CHANNEL_ID, f"🤖 Bots: {bots}"),
        }

        for key, (channel_id, new_name) in targets.items():
            if _last_values.get(key) == new_name:
                continue  # δεν άλλαξε, μην κάνεις άσκοπο API call
            channel = guild.get_channel(channel_id)
            if channel:
                try:
                    await channel.edit(name=new_name)
                    _last_values[key] = new_name
                except discord.HTTPException:
                    pass  # πιθανότατα rate limit από Discord, θα ξαναπροσπαθήσει στο επόμενο event

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            await self.update_stats(guild)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        await self.update_stats(member.guild)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        await self.update_stats(member.guild)

    @commands.Cog.listener()
    async def on_presence_update(self, before: discord.Member, after: discord.Member):
        if before.status != after.status:
            await self.update_stats(after.guild)

    @commands.Cog.listener()
    async def on_guild_update(self, before: discord.Guild, after: discord.Guild):
        if before.premium_subscription_count != after.premium_subscription_count:
            await self.update_stats(after)


async def setup(bot: commands.Bot):
    await bot.add_cog(ServerStatus(bot))
