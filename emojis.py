"""
emojis.py
---------
Custom emojis χωρισμένα ανά κατηγορία.

ΠΩΣ ΤΟ ΣΥΜΠΛΗΡΩΝΕΙΣ:
- Static emoji:   "<:name:ID>"
- Animated emoji: "<a:name:ID>"   (πρόσεξε το "a" πριν τα δύο κόλον)

Το "name" δεν χρειάζεται να ταιριάζει 100% με το πραγματικό όνομα του emoji,
αλλά καλό είναι να το αφήσεις ίδιο για ευκολία. Το μόνο που μετράει στην
εμφάνιση είναι το σωστό ID.

Χρήση μέσα στον κώδικα:
    from emojis import emoji
    emoji("tickets", "close")
"""

EMOJIS = {
    "tickets": {
        "ownership": "<:ownership:>",
        "report": "<a:report:>",
        "support": "<a:support:>",
        "bug": "<a:bug:>",
        "anticheat": "<:anticheat:>",
        "close": "<:close:>",
        "ping": "<a:ping:>",
        "ticket": "<:ticket:>",
    },
    "jobs": {
        "civilian": "<:civilian:>",
        "criminal": "<a:criminal:>",
    },
    "donate": {
        "donate": "<a:donate:>",  # παράδειγμα animated
    },
    "suggestions": {
        "upvote": "<:upvote:>",
        "downvote": "<:downvote:>",
    },
    "moderation": {
        "ban": "<a:ban:>",
        "unban": "<:unban:>",
        "kick": "<a:kick:>",
        "timeout": "<a:timeout:>",
        "untimeout": "<a:untimeout:>",
        "clear": "<:clear:>",
    },
    "voice": {
        "join": "<a:voice_join:>",
        "leave": "<a:voice_leave:>",
        "temp": "<a:temp_voice:>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:>",
        "off_duty": "<a:off_duty:>",
        "leaderboard": "<a:leaderboard:>",
    },
    "applications": {
        "elas": "<:elas:>",
        "ekab": "<:ekab:>",
        "army": "<:army:>",
        "staff": "<:staff:>",
        "manager": "<:manager:>",
        "accept": "<:accept:>",
        "deny": "<:deny:>",
        "apply": "<:apply:>",
        "send": "<:send:>",
        "ping_staff": "<a:ping_staff:>",
    },
    "panel": {
        "list": "<:list:>",
    },
}


def emoji(category: str, name: str) -> str:
    """Επιστρέφει το emoji string. Αν δεν βρεθεί, επιστρέφει κενό string (δεν σκάει το bot)."""
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
