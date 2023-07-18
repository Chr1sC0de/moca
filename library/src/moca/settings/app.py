from typing import Self
import os
import pathlib as pt

import chromadb
import yaml
from pydantic import BaseModel

moca_config_path = pt.Path(os.environ.get("MOCA_HOME", "./.moca-config.yml"))


class MocaNames(BaseModel):
    short_term_memories_folder: pt.Path = ".moca-memories-short-term"
    long_term_memories_folder: pt.Path = ".moca-memories-long-term"
    sensations_folder: pt.Path = ".moca-sensations"

    local_client_name: str = "database"

    explicit_memory_collection: str = "explicit-memories"
    implicit_memory_collection: str = "implicit-memory-collection"


def get_names() -> MocaNames:
    config = None
    if moca_config_path.exists():
        with open(moca_config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f.read())["names"]

    if config is None:
        config = {}
    return MocaNames(**config)


class Configuration:
    _singleton: "Configuration" = None
    _client: chromadb.API = None

    names: MocaNames = None

    def __new__(cls) -> Self:
        if cls._singleton is None:
            cls._singleton: "Configuration" = super(
                Configuration.__class__, cls
            ).__new__(cls)
            cls._singleton.names = get_names()
        return cls._singleton

    @property
    def client(self) -> chromadb.API:
        if self._client is None:
            self._client = chromadb.PersistentClient(
                path=(
                    self.names.long_term_memories_folder
                    / self.names.local_client_name
                ).as_posix()
            )
        return self._client


config = Configuration()
