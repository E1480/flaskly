from dotenv import load_dotenv
from mysql.connector import connect
import os
class Database:
    def __init__(self):
        load_dotenv()
        self.db = connect(
            host=os.getenv("db_host"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password"),
            database=os.getenv("db_name"),
            buffered=True
        )
        self.cr = self.db.cursor()

    def get_all_messages(self):
        self.cr.execute("SELECT * FROM messages")
        return self.cr.fetchall()

    def add_message(self, name, email, subject, message):
        self.cr.execute(
            "INSERT INTO messages (name, email, subject, message) VALUES (%s, %s, %s, %s)",
            (name, email, subject, message)
        )
        self.db.commit()
    
    def delete_message(self, message_id):
        self.cr.execute("DELETE FROM messages WHERE id = %s", (message_id,))
        self.db.commit()

    def close(self):
        self.cr.close()
        self.db.close()


# Usage
# db = Database()
# print(db.get_all_messages())
# db.add_message("test", "test@example.com", "Test Subject", "Test Message")
# db.close()