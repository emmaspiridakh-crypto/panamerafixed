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

GUILD_ID = 1442267433938456668  # PLACEHOLDER: το ID του server σου
PREFIX = "!"

# =========================================================
# ROLES
# =========================================================
OWNERSHIP_ROLE_ID        = 1519086910222499890 # PLACEHOLDER
MANAGER_ROLE_ID          = 1442267434299035855 # PLACEHOLDER
STAFF_ROLE_ID            = 1442267434290516029  # PLACEHOLDER
DEVELOPER_ROLE_ID        = 1442267434290516038  # PLACEHOLDER
CIVILIAN_MANAGER_ROLE_ID = 1519079183677132921  # PLACEHOLDER
CRIMINAL_MANAGER_ROLE_ID = 1442267434299035852  # PLACEHOLDER
DONATE_MANAGER_ROLE_ID   = 1442267434299035857  # PLACEHOLDER
FOUNDER_ROLE_ID          = 1442267434320138421  # PLACEHOLDER
ON_DUTY_ROLE_ID          = 1519079057390698630 
ANTICHEAT_MANAGER_ID = 1519094390243725334# PLACEHOLDER
WAITING_INTERVIEW_ROLE_ID = 1519094598025351340
AUTOROLE_ID = 1442268787364860026# PLACEHOLDER (μπαίνει σε accepted applicants)

# Ρόλοι που θεωρούνται "staff team" γενικά (χρησιμοποιείται σε αρκετά permission checks)
STAFF_TEAM_ROLE_IDS = [STAFF_ROLE_ID, MANAGER_ROLE_ID, OWNERSHIP_ROLE_ID]

# =========================================================
# TICKET SYSTEM #1 - SUPPORT (dropdown, 4 κατηγορίες, ξεχωριστό category η κάθε μία)
# =========================================================
TICKET_SUPPORT_CHANNEL_ID = 1442267435326771337  # PLACEHOLDER: πού θα σταλεί το panel (slash command target)
TICKET_SUPPORT_BANNER_URL = "https://i.imgur.com/43q8TUx.png"
TICKET_SUPPORT_THUMBNAIL_URL = "https://i.imgur.com/X41ekFC.gif"

CAT_TICKET_OWNERSHIP_ID = 1519076395152576693  # PLACEHOLDER category
CAT_TICKET_REPORT_ID    = 1519077262501216337 # PLACEHOLDER category
CAT_TICKET_SUPPORT_ID   = 1519077318218350662  # PLACEHOLDER category
CAT_TICKET_BUG_ID        = 1519077358987116584
CAT_TICKET_ANTICHEAT_ID = 1519076672765300837 # PLACEHOLDER category

# =========================================================
# TICKET SYSTEM #2 - JOBS (button, civilian + criminal, ΙΔΙΟ category και τα δύο)
# =========================================================
CAT_JOBS_ID = 1519076231876972584  # PLACEHOLDER (ΚΟΙΝΟ category civilian + criminal)

TICKET_JOBS_BANNER_URL = "https://i.imgur.com/43q8TUx.png"
TICKET_JOBS_THUMBNAIL_URL = "https://i.imgur.com/X41ekFC.gif"

# =========================================================
# TICKET SYSTEM #3 - DONATE (button, δικό του category)
# =========================================================
CAT_DONATE_ID = 1519076342296088576  # PLACEHOLDER category

TICKET_DONATE_BANNER_URL = "https://i.imgur.com/43q8TUx.png"
TICKET_DONATE_THUMBNAIL_URL = "https://i.imgur.com/X41ekFC.gif"

# Channel όπου γίνεται ping το staff team όταν ανοίγει ΟΠΟΙΟΔΗΠΟΤΕ ticket (support/jobs/donate) ή temp voice
STAFF_PING_CHANNEL_ID = 1519081656047374376  # PLACEHOLDER

# Ticket logs (open + close) - ΞΕΧΩΡΙΣΤΟ από το STAFF_PING_CHANNEL_ID
LOG_TICKETS_CHANNEL_ID = 1519081058304524318   # PLACEHOLDER

# =========================================================
# SUGGESTIONS
# =========================================================
SUGGESTIONS_CHANNEL_ID = 1442267436169822259   # PLACEHOLDER (εδώ ο χρήστης γράφει -> γίνεται auto suggestion)

# =========================================================
# TEMP VOICE
# =========================================================
TEMP_VOICE_JOIN_CHANNEL_ID = 1442267435326771338   # PLACEHOLDER ("Join to Create" channel)
TEMP_VOICE_CATEGORY_ID     = 1519077669147377786   # PLACEHOLDER (εκεί δημιουργούνται τα temp channels)

# =========================================================
# STAFF ACTIVITY
# =========================================================
STAFF_ACTIVITY_VOICE_CHANNEL_ID = 1442267435326771335  # PLACEHOLDER (το channel που μετράμε χρόνο)
STAFF_ACTIVITY_PANEL_CHANNEL_ID = 1519085579399331871  # PLACEHOLDER (πού στέλνεται/μένει το leaderboard panel)
STAFF_ACTIVITY_LOG_CHANNEL_ID   = 1519096891974090752 # PLACEHOLDER
STAFF_ACTIVITY_BANNER_URL = "https://i.imgur.com/43q8TUx.png"

# =========================================================
# LOGS (Requirement 8)
# =========================================================
LOG_JOIN_LEAVE_CHANNEL_ID = 1442267434848485469  # PLACEHOLDER (join + leave μαζί)
LOG_ROLES_CHANNEL_ID      = 1519080301211422810  # PLACEHOLDER
LOG_CHANNELS_CHANNEL_ID   = 1519080064644546640 # PLACEHOLDER (create/delete/edit channels)
LOG_MESSAGES_CHANNEL_ID   = 1519080023536173187  # PLACEHOLDER (edit/delete messages)
LOG_VOICE_CHANNEL_ID      = 1519079947736449186 # PLACEHOLDER
LOG_APPLICATIONS_CHANNEL_ID = 1519081352509526126   # PLACEHOLDER

# Invite logs: ποιος προσκάλεσε ποιον, πόσα invites/μέλη μέσα/έχουν φύγει ανά inviter
INVITE_LOG_CHANNEL_ID = 1519081477139071078  # PLACEHOLDER

# Command logs (Requirement 5) - ξεχωριστό log ανά εντολή, εκτός say/say2/dmall (κοινό)
LOG_BAN_CHANNEL_ID          = 1519080153781895198  # PLACEHOLDER
LOG_UNBAN_CHANNEL_ID        = 1519080153781895198  # PLACEHOLDER
LOG_KICK_CHANNEL_ID         = 1519080193694892254  # PLACEHOLDER
LOG_TIMEOUT_CHANNEL_ID      = 1519080248380100618  # PLACEHOLDER
LOG_UNTIMEOUT_CHANNEL_ID    = 1519080248380100618  # PLACEHOLDER
LOG_CLEARMESSAGES_CHANNEL_ID = 1519082710369308672  # PLACEHOLDER
LOG_SAY_DMALL_CHANNEL_ID    = 1519082710369308672 # PLACEHOLDER (say, say2, dmall μαζί)

# =========================================================
# APPLICATIONS (Requirement 9)
# =========================================================
APPLICATIONS_PANEL_CHANNEL_ID = 1442267435884347557   # PLACEHOLDER (πού στέλνεται το panel)
APPLICATIONS_CATEGORY_ID      = 1519077451261804664 # PLACEHOLDER (εκεί ανοίγουν τα application channels)
APPLICATIONS_BANNER_URL = "https://i.imgur.com/43q8TUx.png"

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
    "army": {
        "label": "Στρατός",
        "questions": [
            "Πόσο χρονών είστε;",
            "Ποιο είναι το Roblox Name σας;",
            "Γιατί θέλεις να μπεις στον Στρατό",
            "Έχεις εμπειρία από στρατιωτικούς ρόλους σε άλλους RP servers",
            "Τι σε κάνει κατάλληλο άτομο για στρατιώτη",
            "Πώς θα αντιδρούσες σε εντολή ανώτερου που δεν σου αρέσει αλλά είναι νόμιμη στο RP",
            "Πώς θα χειριζόσουν παίκτη που δεν υπακούει στις εντολές σου",
            "Τι θεωρείς failRP σε στρατιωτικές σκηνές",
            "Πώς θα αντιμετώπιζες κατάσταση έκτακτης ανάγκης (π.χ. εισβολή, τρομοκρατική απειλή, μαζικό χάος)",
            "Πώς θα αντιδρούσες αν δεις συνάδελφο να παραβιάζει κανόνες",
            "Πώς θα χειριζόσουν παίκτη που σε προκαλεί ή σε βρίζει",
            "Ποιος είναι ο ρόλος του Στρατού μέσα στο RP"
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
STATUS_MEMBERS_CHANNEL_ID = 1519083070270079036  # PLACEHOLDER (π.χ. "👥 Members: 120")
STATUS_ONLINE_CHANNEL_ID  = 1519083135583916192  # PLACEHOLDER
STATUS_BOOSTS_CHANNEL_ID  = 1519083208224936099 # PLACEHOLDER
STATUS_BOTS_CHANNEL_ID    = 1519083165845688561  # PLACEHOLDER

# =========================================================
# ΓΕΝΙΚΑ
# =========================================================
EMBED_COLOR = 0x5865F2      # default χρώμα για logs/embeds, άλλαξέ το όπως θες
