from pathlib import Path


DATAFORMAT = "%Y-%m-%d %H:%M:%S"
PROJECT_DIR = Path(__file__).parent.parent
LOG_FILE = f"{PROJECT_DIR}/shell.log"
HISTORY_FILE = f"{PROJECT_DIR}/.history"
UNDO_HISTORY_FILE = f"{PROJECT_DIR}/.undo_history"
TRASH_DIR = f"{PROJECT_DIR}/.trash"
