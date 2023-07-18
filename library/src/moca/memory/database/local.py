import chromadb

import moca.settings.app as mocasa


def setup_dirs():
    mocasa.config.names.long_term_memories_folder.mkdir(exist_ok=True)
    mocasa.config.names.short_term_memories_folder.mkdir(exist_ok=True)
    mocasa.config.names.sensations_folder.mkdir(exist_ok=True)


def setup_db():
    mocasa.config.client.heartbeat()
