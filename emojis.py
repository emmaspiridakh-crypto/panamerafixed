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
        "ownership": "<:ownership:1516905859614249123>",
        "report": "<a:report:1517127382014759013>",
        "support": "<a:support:1517127015843500143>",
        "bug": "<a:bug:1502334244981309602>",
        "close": "<:close:1516970641448898671>",
        "ping": "<a:ping:1517127060701577387>",
        "ticket": "<:ticket:1516970584599302184>",
    },
    "jobs": {
        "civilian": "<:civilian:1516970677456867440>",
        "criminal": "<a:criminal:1516983884137500743>",
    },
    "donate": {
        "donate": "<a:donate:1517127268470751342>",  # παράδειγμα animated
    },
    "suggestions": {
        "upvote": "<:upvote:1516970594610974822>",
        "downvote": "<:downvote:1516970592715280586>",
    },
    "moderation": {
        "ban": "<a:ban:1516983894535180512>",
        "unban": "<:unban:1516970617633771570>",
        "kick": "<a:kick:1517127137780305972>",
        "timeout": "<a:timeout:1517127137780305972>",
        "untimeout": "<a:untimeout:1517127137780305972>",
        "clear": "<:clear:1516970617633771570>",
    },
    "voice": {
        "join": "<a:voice_join:1517127412771455036>",
        "leave": "<a:voice_leave:1517127340860113027>",
        "temp": "<a:temp_voice:1517127015843500143>",
    },
    "staff_activity": {
        "on_duty": "<a:on_duty:1517127412771455036>",
        "off_duty": "<a:off_duty:1517127340860113027>",
        "leaderboard": "<a:leaderboard:1516983905075466332>",
    },
    "applications": {
        "elas": "<:elas:1516970582397419530>",
        "ekab": "<:ekab:1516970579134251008>",
        "army": "<:army:1517151997466251405>",
        "staff": "<:staff:1516970619609022514>",
        "manager": "<:manager:1516970625472663724>",
        "accept": "<:accept:1516970645030703144>",
        "deny": "<:deny:1516970643101454366>",
        "apply": "<:apply:1516970615221911694>",
        "send": "<:send:1516970621488074885>",
        "ping_staff": "<a:ping_staff:1517127060701577387>",
    },
    "panel": {
        "list": "<:list:1516970615221911694>",
    },
}


def emoji(category: str, name: str) -> str:
    """Επιστρέφει το emoji string. Αν δεν βρεθεί, επιστρέφει κενό string (δεν σκάει το bot)."""
    try:
        return EMOJIS[category][name]
    except KeyError:
        return ""
