import sys
import database
from cli import main_menu

if __name__ == "__main__":
    database.create_tables()
    main_menu()
ad