"""
cogs/tickets.py
"""

from __future__ import annotations

import discord
from discord import ui, app_commands
from discord.ext import commands

import config
from emojis import emoji
from utils import storage
from utils.permissions import has_roles
from utils.components import build_base_container, add_action_row, add_separator, add_text

STORE_NAME = "tickets"


def _ticket_types() -> dict:
    return {
        "ownership": {
            "label": "Ownership",
            "emoji": emoji("tickets", "ownership"),
            "category_id": config.CAT_TICKET_OWNERSHIP_ID,
            "view_roles": [config.OWNERSHIP_ROLE_ID],
        },
        "report": {
            "label": "Report",
            "emoji": emoji("tickets", "report"),
            "category_id": config.CAT_TICKET_REPORT_ID,
            "view_roles": [config.OWNERSHIP_ROLE_ID, config.MANAGER_ROLE_ID],
        },
        "support": {
            "label": "Support",
            "emoji": emoji("tickets", "support"),
            "category_id": config.CAT_TICKET_SUPPORT_ID,
            "view_roles": config.STAFF_TEAM_ROLE_IDS,
        },
        "bug": {
            "label": "Bug Report",
            "emoji": emoji("tickets", "bug"),
            "category_id": config.CAT_TICKET_BUG_ID,
            "view_roles": [config.DEVELOPER_ROLE_ID, config.OWNERSHIP_ROLE_ID],
        },
        "civilian_job": {
            "label": "Civilian Job",
            "emoji": emoji("jobs", "civilian"),
            "category_id": config.CAT_JOBS_ID,
            "view_roles": [config.CIVILIAN_MANAGER_ROLE_ID],
        },
        "criminal_job": {
            "label": "Criminal Job",
            "emoji": emoji("jobs", "criminal"),
            "category_id": config.CAT_JOBS_ID,
            "view_roles": [config.CRIMINAL_MANAGER_ROLE_ID],
        },
        "donate": {
            "label": "Donate",
            "emoji": emoji("donate", "donate"),
            "category_id": config.CAT_DONATE_ID,
            "view_roles": [config.OWNERSHIP_ROLE_ID, config.DONATE_MANAGER_ROLE_ID],
        },
    }


def _safe_name(text: str) -> str:
    text = text.lower().strip().replace(" ", "-")
    return "".join(c for c in text if c.isalnum() or c == "-")[:90]


class Tickets(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # ---------------------------------------------------
    # Δημιουργία ticket channel
    # ---------------------------------------------------
    async def create_ticket(self, interaction: discord.Interaction, ticket_key: str):
        ttypes = _ticket_types()
        data = ttypes.get(ticket_key)
        if not data:
            await interaction.response.send_message("Άγνωστος τύπος ticket.", ephemeral=True)
            return

        guild = interaction.guild
        opener = interaction.user

        # Sync έλεγχοι πριν το defer
        store = storage.get_store(STORE_NAME)
        for ch_id, info in store.items():
            if info.get("opener_id") == opener.id and info.get("type") == ticket_key:
                channel = guild.get_channel(int(ch_id))
                if channel:
                    await interaction.response.send_message(
                        f"Έχεις ήδη ανοιχτό ticket: {channel.mention}", ephemeral=True
                    )
                    return

        category = guild.get_channel(data["category_id"])
        if category is None:
            await interaction.response.send_message(
                "⚠️ Δεν βρέθηκε το category. Έλεγξε το config.py.", ephemeral=True
            )
            return

        # FIX: defer πριν τις async λειτουργίες (channel creation παίρνει > 3 δευτ.)
        await interaction.response.defer(ephemeral=True)

        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            opener: discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True),
            guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, manage_channels=True),
        }
        for role_id in data["view_roles"]:
            role = guild.get_role(role_id)
            if role:
                overwrites[role] = discord.PermissionOverwrite(view_channel=True, send_messages=True)

        channel_name = f"{ticket_key}-{_safe_name(opener.display_name)}"
        new_channel = await guild.create_text_channel(
            name=channel_name, category=category, overwrites=overwrites
        )

        store[str(new_channel.id)] = {
            "type": ticket_key,
            "opener_id": opener.id,
            "guild_id": guild.id,
        }
        storage.save(STORE_NAME, store)

        container = build_base_container(
            title=f"{data['emoji']} {data['label']} Ticket",
            description=f"Άνοιξε από: {opener.mention}\nΠερίγραψε το θέμα σου, η ομάδα θα απαντήσει σύντομα.",
            color=discord.Colour.blurple(),
        )
        add_separator(container)
        close_btn = ui.Button(
            label="Close Ticket", style=discord.ButtonStyle.danger,
            emoji=emoji("tickets", "close"), custom_id=f"ticket_close:{new_channel.id}",
        )
        ping_btn = ui.Button(
            label="Ping User", style=discord.ButtonStyle.secondary,
            emoji=emoji("tickets", "ping"), custom_id=f"ticket_ping:{new_channel.id}",
        )
        add_action_row(container, close_btn, ping_btn)

        view = ui.LayoutView(timeout=None)
        view.add_item(container)
        await new_channel.send(view=view)
        
        ping_channel = guild.get_channel(config.STAFF_PING_CHANNEL_ID)
        if ping_channel:
            await ping_channel.send(
                f"{emoji('tickets', 'ticket')} Νέο ticket: {new_channel.mention} από {opener.mention} ({data['label']})"
            )

        # FIX: followup αντί για response (έχουμε ήδη κάνει defer)
        await interaction.followup.send(f"✅ Το ticket σου: {new_channel.mention}", ephemeral=True)

    # ---------------------------------------------------
    # Κλείσιμο ticket
    # ---------------------------------------------------
    async def handle_close(self, interaction: discord.Interaction, channel_id: int):
        store = storage.get_store(STORE_NAME)
        info = store.get(str(channel_id))
        if not info:
            await interaction.response.send_message("Αυτό το ticket δεν υπάρχει πια στο σύστημα.", ephemeral=True)
            return

        if interaction.user.id == info["opener_id"]:
            await interaction.response.send_message(
                "Δεν μπορείς να κλείσεις το δικό σου ticket — ζήτα από κάποιον άλλον.", ephemeral=True
            )
            return

        await interaction.response.send_message("🔒 Το ticket κλείνει σε 5 δευτερόλεπτα...", ephemeral=False)
        store.pop(str(channel_id), None)
        storage.save(STORE_NAME, store)
        await discord.utils.sleep_until(discord.utils.utcnow() + __import__("datetime").timedelta(seconds=5))
        channel = interaction.guild.get_channel(channel_id)
        if channel:
            await channel.delete(reason=f"Ticket closed by {interaction.user}")

    # ---------------------------------------------------
    # Ping User — FIX: role check + None check + DM πριν response
    # ---------------------------------------------------
    async def handle_ping_user(self, interaction: discord.Interaction, channel_id: int):
        store = storage.get_store(STORE_NAME)
        info = store.get(str(channel_id))
        if not info:
            await interaction.response.send_message("Αυτό το ticket δεν υπάρχει πια στο σύστημα.", ephemeral=True)
            return

        # FIX: μόνο staff/managers/ownership/developers μπορούν
        allowed_roles = [
            *config.STAFF_TEAM_ROLE_IDS,
            config.CIVILIAN_MANAGER_ROLE_ID,
            config.CRIMINAL_MANAGER_ROLE_ID,
            config.DONATE_MANAGER_ROLE_ID,
            config.DEVELOPER_ROLE_ID,
        ]
        if not has_roles(interaction.user, allowed_roles):
            await interaction.response.send_message(
                "⛔ Δεν έχεις δικαίωμα να χρησιμοποιήσεις αυτό το κουμπί.", ephemeral=True
            )
            return

        opener = interaction.guild.get_member(info["opener_id"])
        # FIX: έλεγχος αν ο opener έχει φύγει από τον server
        if opener is None:
            await interaction.response.send_message(
                "⚠️ Ο χρήστης δεν βρίσκεται πια στον server.", ephemeral=True
            )
            return

        # FIX: DM πρώτα, μετά respond (αν το DM κάνει crash δεν έχουμε ήδη απαντήσει)
        dm_sent = True
        try:
            await opener.send(f"🔔 Έχεις ειδοποίηση στο ticket σου: {interaction.channel.mention}")
        except discord.Forbidden:
            dm_sent = False

        note = "" if dm_sent else " _(τα DMs του είναι κλειστά)_"
        await interaction.response.send_message(f"🔔 {opener.mention}{note}", ephemeral=False)

    # ---------------------------------------------------
    # Κεντρικός interaction listener
    # ---------------------------------------------------
    @commands.Cog.listener()
    async def on_interaction(self, interaction: discord.Interaction):
        if interaction.type != discord.InteractionType.component:
            return
        custom_id = interaction.data.get("custom_id", "")

        if custom_id == "support_ticket_select":
            value = interaction.data["values"][0]
            await self.create_ticket(interaction, value)
        elif custom_id == "ticket_open_civilian_job":
            await self.create_ticket(interaction, "civilian_job")
        elif custom_id == "ticket_open_criminal_job":
            await self.create_ticket(interaction, "criminal_job")
        elif custom_id == "ticket_open_donate":
            await self.create_ticket(interaction, "donate")
        elif custom_id.startswith("ticket_close:"):
            await self.handle_close(interaction, int(custom_id.split(":")[1]))
        elif custom_id.startswith("ticket_ping:"):
            await self.handle_ping_user(interaction, int(custom_id.split(":")[1]))

    # ---------------------------------------------------
    # Slash commands — FIX: defer πρώτα, followup μετά
    # ---------------------------------------------------
    @app_commands.command(name="panel-support", description="Στέλνει το Support ticket panel (dropdown)")
    @app_commands.checks.has_any_role(config.OWNERSHIP_ROLE_ID, config.MANAGER_ROLE_ID, config.STAFF_ROLE_ID)
    async def panel_support(self, interaction: discord.Interaction):
        ttypes = _ticket_types()
        container = build_base_container(
            title="🎫 Support Tickets",
            description="Επίλεξε κατηγορία από το μενού παρακάτω για να ανοίξεις ticket.",
            banner_url=config.TICKET_SUPPORT_BANNER_URL,
            thumbnail_url=config.TICKET_SUPPORT_THUMBNAIL_URL,
        )
        add_separator(container)
        options = [
            discord.SelectOption(label=ttypes[k]["label"], value=k, emoji=ttypes[k]["emoji"] or None)
            for k in ("ownership", "report", "support", "bug")
        ]
        select = ui.Select(placeholder="Επίλεξε κατηγορία...", options=options, custom_id="support_ticket_select")
        add_action_row(container, select)

        view = ui.LayoutView(timeout=None)
        view.add_item(container)
        await interaction.response.defer(ephemeral=True)
        await new_channel.send(view=view)
        await interaction.followup.send("✅ Στάλθηκε.", ephemeral=True)

    @app_commands.command(name="panel-civilian-job", description="Στέλνει το Civilian Job panel")
    @app_commands.checks.has_any_role(config.OWNERSHIP_ROLE_ID, config.MANAGER_ROLE_ID, config.STAFF_ROLE_ID)
    async def panel_civilian_job(self, interaction: discord.Interaction):
        await self._send_button_panel(
            interaction, key="civilian_job", title="👷 Civilian Job Ticket",
            description="Πάτησε το κουμπί για να πάρεις Civilian Job.",
        )

    @app_commands.command(name="panel-criminal-job", description="Στέλνει το Criminal Job panel")
    @app_commands.checks.has_any_role(config.OWNERSHIP_ROLE_ID, config.MANAGER_ROLE_ID, config.STAFF_ROLE_ID)
    async def panel_criminal_job(self, interaction: discord.Interaction):
        await self._send_button_panel(
            interaction, key="criminal_job", title="🔫 Criminal Job Ticket",
            description="Πάτησε το κουμπί για να πάρεις Criminal Job.",
        )

    @app_commands.command(name="panel-donate", description="Στέλνει το Donate panel")
    @app_commands.checks.has_any_role(config.OWNERSHIP_ROLE_ID, config.MANAGER_ROLE_ID, config.STAFF_ROLE_ID)
    async def panel_donate(self, interaction: discord.Interaction):
        await self._send_button_panel(
            interaction, key="donate", title="💎 Donate",
            description="Πάτησε το κουμπί για να ανοίξεις donate ticket.",
        )

    async def _send_button_panel(self, interaction: discord.Interaction, *, key: str, title: str, description: str):
        ttypes = _ticket_types()
        data = ttypes[key]
        banner = {
            "civilian_job": config.TICKET_JOBS_BANNER_URL,
            "criminal_job": config.TICKET_JOBS_BANNER_URL,
            "donate": config.TICKET_DONATE_BANNER_URL,
        }[key]
        thumb = {
            "civilian_job": config.TICKET_JOBS_THUMBNAIL_URL,
            "criminal_job": config.TICKET_JOBS_THUMBNAIL_URL,
            "donate": config.TICKET_DONATE_THUMBNAIL_URL,
        }[key]

        container = build_base_container(title=title, description=description, banner_url=banner, thumbnail_url=thumb)
        add_separator(container)
        btn = ui.Button(
            label=data["label"], style=discord.ButtonStyle.success,
            emoji=data["emoji"] or None, custom_id=f"ticket_open_{key}",
        )
        add_action_row(container, btn)

        view = ui.LayoutView(timeout=None)
        view.add_item(container)
        # FIX: defer πρώτα, channel.send μετά, followup στο τέλος
        await interaction.response.defer(ephemeral=True)
        await new_channel.send(view=view)
        await interaction.followup.send("✅ Στάλθηκε.", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(Tickets(bot))
