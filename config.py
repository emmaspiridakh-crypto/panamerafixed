"""
config.py
---------
ΟΛΑ τα IDs του server μπαίνουν εδώ. Κάθε placeholder λέει ΤΙ ΑΚΡΙΒΩΣ πρέπει να βάλεις.
Βάλε τα IDs σαν integers (χωρίς εισαγωγικά), π.χ. OWNERSHIP_ROLE_ID = 123456789012345678

Tip: Discord Developer Mode -> Right click role/channel/category -> Copy ID
"""

import os
from dotenv import load_dotenv

load_dotenv()

# =========================================================
# BOT TOKEN (μπαίνει στο .env locally, ή Environment Variable στο Render)
# =========================================================
TOKEN = os.getenv("DISCORD_TOKEN")

GUILD_ID = 1510300348341031113   # PLACEHOLDER: το ID του server σου
PREFIX = "!"

# =========================================================
# ROLES
# =========================================================
OWNERSHIP_ROLE_ID        = 1523088527691354253 # PLACEHOLDER
MANAGER_ROLE_ID          = 1510300348374323210 # PLACEHOLDER
STAFF_ROLE_ID            = 1510300348353478812 # PLACEHOLDER
DEVELOPER_ROLE_ID        = 1510300348374323214 # PLACEHOLDER
CIVILIAN_MANAGER_ROLE_ID = 1523067480816488620  # PLACEHOLDER
CRIMINAL_MANAGER_ROLE_ID = 1510300348353478815  # PLACEHOLDER
DONATE_MANAGER_ROLE_ID   = 1510300348374323215  # PLACEHOLDER
FOUNDER_ROLE_ID          = 1510300348374323218  # PLACEHOLDER
ON_DUTY_ROLE_ID          = 1523067577352323102 
ANTICHEAT_MANAGER_ID = 1510300348341031117# PLACEHOLDER
WAITING_INTERVIEW_ROLE_ID = 1510300348341031121
AUTOROLE_ID = 1510300348341031114# PLACEHOLDER (μπαίνει σε accepted applicants)

# Ρόλοι που θεωρούνται "staff team" γενικά (χρησιμοποιείται σε αρκετά permission checks)
STAFF_TEAM_ROLE_IDS = [STAFF_ROLE_ID, MANAGER_ROLE_ID, OWNERSHIP_ROLE_ID]

# =========================================================
# TICKET SYSTEM #1 - SUPPORT (dropdown, 4 κατηγορίες, ξεχωριστό category η κάθε μία)
# =========================================================
TICKET_SUPPORT_CHANNEL_ID = 1510300349582413858  # PLACEHOLDER: πού θα σταλεί το panel (slash command target)
TICKET_SUPPORT_BANNER_URL = "https://i.imgur.com/CIYO8rT.jpeg"
TICKET_SUPPORT_THUMBNAIL_URL = "https://i.imgur.com/TnTQ7x1.gif"

CAT_TICKET_OWNERSHIP_ID =  1523076534607544400 # PLACEHOLDER category
CAT_TICKET_REPORT_ID    =  1523076682704093214 # PLACEHOLDER category
CAT_TICKET_SUPPORT_ID   =  1523076363517427843 # PLACEHOLDER category
CAT_TICKET_BUG_ID        = 1523076572100296714
CAT_TICKET_ANTICHEAT_ID = 1523076429745750141 # PLACEHOLDER category

# =========================================================
# TICKET SYSTEM #2 - JOBS (button, civilian + criminal, ΙΔΙΟ category και τα δύο)
# =========================================================
CAT_JOBS_ID = 1523076883930026024 # PLACEHOLDER (ΚΟΙΝΟ category civilian + criminal)

TICKET_JOBS_BANNER_URL = "https://i.imgur.com/CIYO8rT.jpeg"
TICKET_JOBS_THUMBNAIL_URL = "https://i.imgur.com/TnTQ7x1.gif"

# =========================================================
# TICKET SYSTEM #3 - DONATE (button, δικό του category)
# =========================================================
CAT_DONATE_ID = 1523077060506157126 # PLACEHOLDER category

TICKET_DONATE_BANNER_URL = "https://i.imgur.com/CIYO8rT.jpeg"
TICKET_DONATE_THUMBNAIL_URL = "https://i.imgur.com/TnTQ7x1.gif"

# Channel όπου γίνεται ping το staff team όταν ανοίγει ΟΠΟΙΟΔΗΠΟΤΕ ticket (support/jobs/donate) ή temp voice
STAFF_PING_CHANNEL_ID = 1523073829122084885  # PLACEHOLDER

# Ticket logs (open + close) - ΞΕΧΩΡΙΣΤΟ από το STAFF_PING_CHANNEL_ID
LOG_TICKETS_CHANNEL_ID = 1523089687743299726    # PLACEHOLDER

# =========================================================
# SUGGESTIONS
# =========================================================
SUGGESTIONS_CHANNEL_ID = 1510300350022815957   # PLACEHOLDER (εδώ ο χρήστης γράφει -> γίνεται auto suggestion)

# =========================================================
# TEMP VOICE
# =========================================================
TEMP_VOICE_JOIN_CHANNEL_ID = 1510300349582413859    # PLACEHOLDER ("Join to Create" channel)
TEMP_VOICE_CATEGORY_ID     = 1510300349582413856   # PLACEHOLDER (εκεί δημιουργούνται τα temp channels)

# =========================================================
# STAFF ACTIVITY
# =========================================================
STAFF_ACTIVITY_VOICE_CHANNEL_ID = 1510300349213184175 # PLACEHOLDER (το channel που μετράμε χρόνο)
STAFF_ACTIVITY_PANEL_CHANNEL_ID = 1510300349003600090  # PLACEHOLDER (πού στέλνεται/μένει το leaderboard panel)
STAFF_ACTIVITY_LOG_CHANNEL_ID   = 1523073238098514132 # PLACEHOLDER
STAFF_ACTIVITY_BANNER_URL = "https://i.imgur.com/CIYO8rT.jpeg"

# =========================================================
# LOGS (Requirement 8)
# =========================================================
LOG_JOIN_LEAVE_CHANNEL_ID = 1523072794705789128 # PLACEHOLDER (join + leave μαζί)
LOG_ROLES_CHANNEL_ID      = 1523072951455580353  # PLACEHOLDER
LOG_CHANNELS_CHANNEL_ID   = 1523073336291233792# PLACEHOLDER (create/delete/edit channels)
LOG_MESSAGES_CHANNEL_ID   = 1523072933235261520  # PLACEHOLDER (edit/delete messages)
LOG_VOICE_CHANNEL_ID      = 1523072879221276873 # PLACEHOLDER
LOG_APPLICATIONS_CHANNEL_ID = 1523073005193007155    # PLACEHOLDER

# Invite logs: ποιος προσκάλεσε ποιον, πόσα invites/μέλη μέσα/έχουν φύγει ανά inviter
INVITE_LOG_CHANNEL_ID = 1523072907310268416   # PLACEHOLDER

# Command logs (Requirement 5) - ξεχωριστό log ανά εντολή, εκτός say/say2/dmall (κοινό)
LOG_BAN_CHANNEL_ID          = 1523073122323005510 # PLACEHOLDER
LOG_UNBAN_CHANNEL_ID        = 1523073122323005510# PLACEHOLDER
LOG_KICK_CHANNEL_ID         = 1523073200802758727 # PLACEHOLDER
LOG_TIMEOUT_CHANNEL_ID      = 1523073158402408542  # PLACEHOLDER
LOG_UNTIMEOUT_CHANNEL_ID    = 1523073158402408542# PLACEHOLDER
LOG_CLEARMESSAGES_CHANNEL_ID = 1523073089267695746 # PLACEHOLDER
LOG_SAY_DMALL_CHANNEL_ID    = 1523073089267695746 # PLACEHOLDER (say, say2, dmall μαζί)

# =========================================================
# APPLICATIONS (Requirement 9)
# =========================================================
APPLICATIONS_PANEL_CHANNEL_ID = 1518980714060578907   # PLACEHOLDER (πού στέλνεται το panel)
APPLICATIONS_CATEGORY_ID      = 1523076951072575528 # PLACEHOLDER (εκεί ανοίγουν τα application channels)
APPLICATIONS_BANNER_URL = "https://i.imgur.com/CIYO8rT.jpeg"

# Τύποι αιτήσεων -> ερωτήσεις. Βάλε τις ερωτήσεις σου εδώ (μία λίστα string ανά τύπο).
APPLICATION_TYPES = {
    "elas": {
        "label": "ΕΛ.ΑΣ",
        "questions": [
            "Πόσο χρονών είστε;",
            "Ποιο είναι το Roblox Name σας;",
            "Πόσες ώρες την ημέρα μπορείτε να αφιερώνετε πάνω στο κομμάτι της ΕΛ.ΑΣ;",
            "Γιατί θέλεις να μπεις στην ΕΛ.ΑΣ",
            "Έχεις εμπειρία από άλλους RP servers; Αν ναι, ποια",
            "Τι σε κάνει κατάλληλο άτομο για αστυνομικό",
            "Πώς θα αντιδρούσες σε έναν παίκτη που δεν υπακούει στις εντολές σου",
            "Πώς θα χειριζόσουν μια ληστεία",
            "Τι θεωρείς failRP σε μια αστυνομική σκηνή",
            "Πώς θα αντιμετώπιζες παίκτη που σε βρίζει ή σε προκαλεί",
            "Τι θα έκανες αν δεις συνάδελφο να παραβιάζει κανόνες",
            "Ποιος είναι ο ρόλος της ΕΛ.ΑΣ μέσα στο RP"
        ],
    },
    "ekab": {
        "label": "ΕΚΑΒ",
        "questions": [
            "Πόσο χρονών είστε;",
            "Ποιο είναι το Roblox Name σας;",
            "Γιατί θέλεις να μπεις στο ΕΚΑΒ",
            "Έχεις εμπειρία από ιατρικούς ρόλους σε άλλους RP servers",
            "Τι σε κάνει κατάλληλο άτομο για διασώστη",
            "Πώς θα χειριζόσουν έναν τραυματία που δεν συνεργάζεται",
            "Πώς αντιμετωπίζεις παίκτη που κάνει failRP σε ιατρική σκηνή",
            "Πώς θα αντιδρούσες σε σοβαρό τροχαίο με πολλούς τραυματίες",
            "Τι θεωρείς ως σωστό ιατρικό RP",
            "Πώς θα χειριζόσουν παίκτη που σε βρίζει ενώ προσπαθείς να τον βοηθήσεις",
            "Τι θα έκανες αν δεις συνάδελφο να κάνει λάθος ή να παραβιάζει κανόνες",
            "Ποιος είναι ο ρόλος του ΕΚΑΒ μέσα στο RP"
        ],
    },
    "staff": {
        "label": "Staff",
        "questions": [
            "Πόσο χρονών είστε;",
            "Ποιο είναι το Roblox Name σας;",
            "Πόσες ώρες έχετε στο Roblox και πόσες σαν Staff;",
            "Πόσες ώρες την ημέρα μπορείτε να αφιερώνετε πάνω στο κομμάτι του staff;",
            "Θεωρείτε ότι πρέπει να υπακούτε τον ανώτερο σας και γιατί;",
            "Τι σημαίνει ιεραρχία για εσάς; Θεωρείτε ότι χρειάζεται σε ένα staff team;",
            "Γιατί θα πρέπει να σας επιλέξουμε σε σχέση με κάποιον άλλον user;",
            "Πείτε μας κατά την άποψη σας πια είναι τα θετικά και πια τα αρνητικά στοιχεία του εαυτού σας;",
            "Τι σημαίνει για εσάς σεβασμός στον user;",
            "Κατανοείς ότι αν η αίτηση σου γίνει αποδεκτή θα ενταχθείς στο staff team με τον ρόλο του server helper/supporter αναλόγως τις απαντήσεις σου στο interview;"
        ],
    },
    "manager": {
        "label": "Manager",
        "questions": [
            "Πόσο χρονών είστε;",
            "Ποιο είναι το Roblox Name σας;",
            "Πες μας λίγα λόγια για εσένα και την εμπειρία σου σε RP servers.",
            "Τι σε κάνει κατάλληλο/η για Manager στον συγκεκριμένο server.",
            "Πώς αντιδράς όταν κάποιος παίκτης παραβιάζει κανόνες αλλά επιμένει ότι έχει δίκιο.",
            "Πώς χειρίζεσαι τοξική συμπεριφορά μέσα στο staff team.",
            "Πώς θα αντιμετώπιζες έναν φίλο σου που παραβιάζει κανόνες.",
            "Πώς διαχειρίζεσαι πίεση ή πολλά reports ταυτόχρονα.",
            "Πείτε μας κατά την άποψη σας πια είναι τα θετικά και πια τα αρνητικά στοιχεία του εαυτού σας;",
            "Πώς θα βελτίωνες την επικοινωνία ανάμεσα σε staff και players."
            "Ποια είναι η γνώμη σου για τα logs και πώς πρέπει να χρησιμοποιούνται.",
            "Πώς αντιμετωπίζεις κάποιον που κάνει powergaming ή metagaming.",
            "Πώς θα έλυνες μια διαφωνία για ένα RP scenario χωρίς να χαλάσει η εμπειρία των παικτών."
            
        ],
    },
}

# =========================================================
# SERVER STATUS (Requirement 10) - voice channels που λειτουργούν ως "οθόνες"
# =========================================================
STATUS_MEMBERS_CHANNEL_ID = 1523085502536880188  # PLACEHOLDER (π.χ. "👥 Members: 120")
STATUS_ONLINE_CHANNEL_ID  = 1523085406331994183  # PLACEHOLDER
STATUS_BOOSTS_CHANNEL_ID  = 1523085582698414100# PLACEHOLDER
STATUS_BOTS_CHANNEL_ID    = 1523085536187650098  # PLACEHOLDER

# =========================================================
# ΓΕΝΙΚΑ
# =========================================================
EMBED_COLOR = FEE75C      # default χρώμα για logs/embeds, άλλαξέ το όπως θες
