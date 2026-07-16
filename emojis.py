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
        "ownership": "<:ownership:1525881027841757284>",
        "report": "<a:report:1523097248689422497>",
        "support": "<a:support:1523094283605905509>",
        "bug": "<:bug:1522610156326883488>",
        "anticheat": "<:anticheat:1523096351527931964>",
        "close": "<:close:1523096376311939153>",
        "ping": "<a:ping:1523097186760392754>",
        "ticket": "<:ticket:1523091708525547631>",
    },
    "jobs": {
        "civilian": "<:civilian:1523097039515291751>",
        "criminal": "<a:criminal:1523097070104481885>",
    },
    "donate": {
        "donate": "<a:donate:1522610435092648016>",  # παράδειγμα animated
    },
    "suggestions": {
        "upvote": "<:upvote:1523094625110200520>",
        "downvote": "<:downvote:1523094599193858259>",
    },
    "moderation": {
        "ban": "<a:ban:1523093855774314546>",
        "unban": "<a:unban:1523097248689422497>",
        "kick": "<a:kick:1523097248689422497>",
        "timeout": "<a:timeout:1523097248689422497>",
        "untimeout": "<a:untimeout:1523097248689422497>",
        "clear": "<:clear:1523097248689422497>",
    },
    "voice": {
        "join": "<a:voice_join:1522609639223595168>",
        "leave": "<a:voice_leave:1522609632890065087>",
        "temp": "<a:temp_voice:1523094283605905509>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:1522609639223595168>",
        "off_duty": "<a:off_duty:1522609632890065087>",
        "leaderboard": "<a:leaderboard:1523095718137434213>",
    },
    "applications": {
        "elas": "<:elas:1522609078046691449>",
        "ekab": "<:ekab:1523086471114784858>",
        "staff": "<:staff:1522610147078176808>",
        "strato":  "<:strato:1527249115195379733>",
        "fbi":     "<:fbi:1527249174746234910>",
        "manager": "<:manager:1522610164757430527>",
        "accept": "<:accept:1523096701416636607>",
        "deny": "<:deny:1523096672278810685>",
        "apply": "<:apply:1523095747577385020>",
        "send": "<:send:1523096701416636607>",
        "ping_staff": "<a:ping_staff:1523097186760392754>",
    },
    "panel": {
        "list": "<:list:1523095747577385020>",
    },
}


def emoji(category: str, name: str) -> str:
    """Επιστρέφει το emoji string. Αν δεν βρεθεί, επιστρέφει κενό string (δεν σκάει το bot)."""
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
