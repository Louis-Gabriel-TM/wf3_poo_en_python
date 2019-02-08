import hashlib
from .databasehandler import DatabaseHandler


class Controller:
    def __init__(self, guiHandler_ref):
        self.guiHandler = guiHandler_ref
        self.db = DatabaseHandler(self)

    def generate_hash(self, password):
        """
        Hash the password given in parameters following SHA256 algorithm
        """

        return hashlib.sha256(bytes(password, "UTF-8")).hexdigest()

    def login(self, login, password):
        login = login
        password = self.generate_hash(password)

        if (login == "admin") and (password == self.generate_hash("Admin42")):
            self.guiHandler.logged_menu("admin", login)

        elif (login == "") or (password == ""):
            self.guiHandler.login_menu()

        else:
            self.guiHandler.logged_menu("student", login)

    def db_shutdown_request(self):
        self.db.db_shutdown()

    def view_request(self):
        results = self.db.view_table("student")
        self.guiHandler.view_result(results)

    def create_table_request(self, table):
        self.db.create_table(table)

    def insert_request(self):
        self.db.insert_table("student")

    def submit(self):
        self.db.insert_table("user")

    def form_clear(self):
        pass

if __name__ == "__main__":
    ctl = Controller()
    print(ctl.generate_hash("Hello World !"))
