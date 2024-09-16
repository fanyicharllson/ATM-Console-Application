import logging
from Entryapp import EntryInfo

file_handler = logging.FileHandler("Database.log")
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s', handlers=[file_handler])

def main():
    """Main entry point of the ATM Application"""
    EntryInfo()


if __name__ == '__main__':
    logging.info("Application starting...")
    main()
