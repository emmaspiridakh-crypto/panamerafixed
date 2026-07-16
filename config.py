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
APPLICATION_ACCEPTED_ROLES = {
    "elas":   1527256651118153778 ,  # PLACEHOLDER
    "ekab":   1527256723042074675,  # PLACEHOLDER
    "strato": 1527256930488287302 ,  # PLACEHOLDER
    "fbi":    1527256806517375036 ,  # PLACEHOLDER
    "staff":  1510300348341031121 ,  # PLACEHOLDER - Waiting for Interview Staff
    "manager":1527257268729679902,  # PLACEHOLDER - Waiting for Interview Manager
}
AUTOROLE_ID = 1510300348341031114# PLACEHOLDER (μπαίνει σε accepted applicants)

# Ρόλοι που θεωρούνται "staff team" γενικά (χρησιμοποιείται σε αρκετά permission checks)
STAFF_TEAM_ROLE_IDS = [STAFF_ROLE_ID, MANAGER_ROLE_ID, OWNERSHIP_ROLE_ID]

# =========================================================
# TICKET SYSTEM #1 - SUPPORT (dropdown, 4 κατηγορίες, ξεχωριστό category η κάθε μία)
# =========================================================
TICKET_SUPPORT_CHANNEL_ID = 1510300349582413858  # PLACEHOLDER: πού θα σταλεί το panel (slash command target)
TICKET_SUPPORT_BANNER_URL = "https://i.imgur.com/0xmFvSH.jpeg"
TICKET_SUPPORT_THUMBNAIL_URL = "https://i.imgur.com/Ntirila.gif"

CAT_TICKET_OWNERSHIP_ID =  1523076534607544400 # PLACEHOLDER category
CAT_TICKET_REPORT_ID    =  1523076682704093214 # PLACEHOLDER category
CAT_TICKET_SUPPORT_ID   =  1523076363517427843 # PLACEHOLDER category
CAT_TICKET_BUG_ID        = 1523076572100296714
CAT_TICKET_ANTICHEAT_ID = 1523076429745750141 # PLACEHOLDER category

# =========================================================
# TICKET SYSTEM #2 - JOBS (button, civilian + criminal, ΙΔΙΟ category και τα δύο)
# =========================================================
CAT_JOBS_ID = 1523076883930026024 # PLACEHOLDER (ΚΟΙΝΟ category civilian + criminal)

TICKET_JOBS_BANNER_URL = "https://i.imgur.com/0xmFvSH.jpeg"
TICKET_JOBS_THUMBNAIL_URL = "https://i.imgur.com/Ntirila.gif"

# =========================================================
# TICKET SYSTEM #3 - DONATE (button, δικό του category)
# =========================================================
CAT_DONATE_ID = 1523077060506157126 # PLACEHOLDER category

TICKET_DONATE_BANNER_URL = "https://i.imgur.com/0xmFvSH.jpeg"
TICKET_DONATE_THUMBNAIL_URL = "https://i.imgur.com/Ntirila.gif"

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
STAFF_ACTIVITY_PANEL_CHANNEL_ID = 1510300349003600090 # PLACEHOLDER (πού στέλνεται/μένει το leaderboard panel)
STAFF_ACTIVITY_LOG_CHANNEL_ID   = 1523073238098514132 # PLACEHOLDER
STAFF_ACTIVITY_BANNER_URL = "https://i.imgur.com/0xmFvSH.jpeg"

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
APPLICATIONS_BANNER_URL = "https://i.imgur.com/0xmFvSH.jpeg"

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
            "Πόσο χρονόν εισαι;",
            "Πως σε λένε στο Roblox;",
            "Πόσες ώρες θα μπορείς να είσαι on duty;",
            "Έχεις προηγούμενη εμπειρία σε staff; Και αν ναι που;",
            "Γιατί θες αυτή τη θέση;",
            "Δύο staff μαλώνουν δημόσια — τι κάνεις πρώτα;",
            "RDM/VDM/Combat Log — εξήγησέ τα με δικά σου λόγια",
            "Πώς αντιδράς όταν ένας παίκτης σε προσβάλλει προσωπικά ενώ κάνεις τη δουλειά σου;",
            "Τι κάνεις όταν διαφωνείς με απόφαση ανώτερου staff μπροστά σε παίκτη;",
            "Πώς τεκμηριώνεις ένα ban — τι στοιχεία κρατάς πάντα;",
            "Ένας παίκτης το παρακάνει με meta-gaming μέσω Discord voice channels μέσο RP. Πώς το εντοπίζεις/αποδεικνύεις;",
            "Δύο reports έρχονται ταυτόχρονα με ίδια σοβαρότητα. Ποιο κριτήριο χρησιμοποιείς για να διαλέξεις ποιο πρώτα;"
        ],
    },
    "manager": {
        "label": "Manager",
        "questions": [
            "Πόσο χρονών είστε;",
            "Ποιο είναι το Roblox Name σας;",
            "Ένα πράγμα που θα άλλαζες στη δομή του server & γιατί",
            "Πώς αξιολογείς αν ένας staff αξίζει προαγωγή;",
            "Πρέπει να υποβιβάσεις φίλο σου — θα το κάνεις; Πώς;",
            "Server χάνει active players — διαδικασία διάγνωσης;",
            "Disagreement με owner πάνω σε απόφασή του — πώς το χειρίζεσαι;",
            "Πώς θα έφτιαχνες staff team από την αρχή αν το τωρινό διαλυόταν εντελώς; Ποια κριτήρια θα κοιτούσες πρώτα;",
            "Ανακαλύπτεις ότι ένας staff πουλάει in-game πλεονεκτήματα για πραγματικά χρήματα εκτός συστήματος του server. Ποια είναι η ακριβής διαδικασία σου βήμα-βήμα;",
            "Πού βλέπεις το server σε 6 μήνες αν γίνεις manager, με συγκεκριμένα, μετρήσιμα ορόσημα;",
            "Ποιο θα ήταν το πρώτο πράγμα που θα έκανες τις πρώτες 48 ώρες στη θέση;",
            "Δύο staff κατηγορούν ο ένας τον άλλον για κλοπή δεδομένων. Πώς το διερευνάς χωρίς να πάρεις προκατειλημμένη θέση;",
            "Πόσες ώρες θα μπορείς να είσαι on;"
        ],
    },
    "strato": {
        "label": "Στρατός",
        "questions": [
            "Πόσο χρονών είσαι;",
            "Πως σε λένε στο roblox;",
            "Γιατί θέλεις να υπηρετήσεις στον στρατό;",
            "Ποια θεωρείς ότι είναι τα σημαντικότερα χαρακτηριστικά ενός καλού στρατιώτη;",
            "Πώς αντιμετωπίζεις καταστάσεις πίεσης ή άγχους;",
            "Έχεις συμμετάσχει ποτέ σε δραστηριότητες που απαιτούσαν ομαδική συνεργασία; Δώσε ένα παράδειγμα.",
            "Πώς θα αντιδρούσες αν λάμβανες μια δύσκολη διαταγή με την οποία δεν συμφωνούσες προσωπικά;",
            "Ποια είναι τα δυνατά σου σημεία και ποια θεωρείς ότι χρειάζονται βελτίωση;",
            "Πώς διατηρείς τη φυσική σου κατάσταση και πόσο σημαντική πιστεύεις ότι είναι η σωματική άσκηση για έναν στρατιωτικό;",
            "Πώς θα διαχειριζόσουν μια κατάσταση όπου θα έπρεπε να πάρεις γρήγορα μια κρίσιμη απόφαση;",
            "Τι γνωρίζεις για τις υποχρεώσεις και τις απαιτήσεις της στρατιωτικής ζωής;"
        ],
    },
    "fbi": {
        "label": "FBI",
        "questions": [
            "Πόσο χρονών είσαι;",
            "Πως σε λένε στο roblox;",
            "Γιατί θέλεις να μπεις στο FBI και όχι σε άλλη υπηρεσία;",
            "Τι σημαίνει για εσένα federal level professionalism;",
            "Πώς θα αντιδρούσες αν ένας πολίτης σε προκαλέσει ή σε βρίζει;",
            "Aν δεις έναν συνάδελφο να κάνει abuse, τι κάνεις;",
            "Τι είναι για εσένα probable cause;",
            "Πώς χειρίζεσαι έναν ύποπτο που δεν συνεργάζεται;",
            "Τι θα κάνεις αν ένας πολίτης σου ζητήσει πληροφορίες για μυστική έρευνα;",
            "Πόσο χρόνο μπορείς να είσαι ενεργός στο FBI κάθε εβδομάδα;",
            "Έχεις εμπειρία σε έρευνες, undercover ή πληροφοριοδότες;"
        ],
    },
}
# =========================================================
# SERVER STATUS (Requirement 10) - voice channels που λειτουργούν ως "οθόνες"
# =========================================================
STATUS_MEMBERS_CHANNEL_ID = 1523085502536880188  # PLACEHOLDER (π.χ. "👥 Members: 120")
STATUS_ONLINE_CHANNEL_ID  = 1523085406331994183  # PLACEHOLDER
STATUS_BOOSTS_CHANNEL_ID  = 1523085582698414100  # PLACEHOLDER
STATUS_BOTS_CHANNEL_ID    = 1523085536187650098  # PLACEHOLDER

# =========================================================
# ΓΕΝΙΚΑ
# =========================================================
EMBED_COLOR = 0xFEE75C
