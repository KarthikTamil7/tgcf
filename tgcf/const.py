"""Declare all global constants."""

COMMANDS = {
    "start": "Check if 😊 I'm Alive",
    "about": "About Me 😌",
    "help": "How to Use Me❓",
    "forward": "Set a New Forward ⏩",
    "remove": "Remove 🚫 an Existing Forward",
    "style": "Change Font Style 🔠",
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.json"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"

MONGO_DB_NAME = "tgcf-config"
MONGO_COL_NAME = "tgcf-instance-0"
