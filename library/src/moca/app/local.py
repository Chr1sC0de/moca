import moca.memory.database.local


def main():
    moca.memory.database.local.setup_dirs()
    moca.memory.database.local.setup_db()


if __name__ == "__main__":
    main()
