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
        "ownership": "<:ownership:1442512112956997724>",
        "report": "<a:report:1519095063765061702>",
        "support": "<a:support:1519095001143972043>",
        "bug": "<a:bug:1519094162774032464>",
        "anticheat": "<:anticheat:1519100803145662616>",
        "close": "<:close:1519100858615464138>",
        "ping": "<a:ping:1519098406453379172>",
        "ticket": "<:ticket:1519095115526832258>",
    },
    "jobs": {
        "civilian": "<:civilian:1519097131174985962>",
        "criminal": "<a:criminal:1519096930473349311>",
    },
    "donate": {
        "donate": "<a:donate:1519094970005323937>",  # παράδειγμα animated
    },
    "suggestions": {
        "upvote": "<:upvote:1519095560508936293>",
        "downvote": "<:downvote:1519095608638570616>",
    },
    "moderation": {
        "ban": "<a:ban:1519095220548010095>",
        "unban": "<:unban:1519093727056887948>",
        "kick": "<a:kick:1519095034761318600>",
        "timeout": "<a:timeout:1519094243639955497>",
        "untimeout": "<a:untimeout:1519094243639955497>",
        "clear": "<:clear:1519094211348004864>",
    },
    "voice": {
        "join": "<a:voice_join:1519093727056887948>",
        "leave": "<a:voice_leave:1519093767259296006>",
        "temp": "<a:temp_voice:1519095001143972043>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:1519093727056887948>",
        "off_duty": "<a:off_duty:1519093767259296006>",
        "leaderboard": "<a:leaderboard:1519096111359463464>",
    },
    "applications": {
        "elas": "<:elas:1519097027567288372>",
        "ekab": "<:ekab:1519097055430181024>",
        "army": "<:army:1519097107368251523>",
        "staff": "<:staff:1519096046486028478>",
        "manager": "<:manager:1519097080474243275>",
        "accept": "<:accept:1519096285150580876>",
        "deny": "<:deny:1519096315064225974>",
        "apply": "<a:apply:1519096111359463464>",
        "send": "<:send:1519096285150580876>",
        "ping_staff": "<a:ping_staff:1519098406453379172>",
    },
    "panel": {
        "list": "<:list:1519098380876251166>",
    },
}


def emoji(category: str, name: str) -> str:
    """Επιστρέφει το emoji string. Αν δεν βρεθεί, επιστρέφει κενό string (δεν σκάει το bot)."""
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
