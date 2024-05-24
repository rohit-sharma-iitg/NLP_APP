import json


class Database():

    def add_data(self, name, email, password):
        with open('db.json', 'r') as rf:
            database = json.load(rf)

        if email in database:
            return 1
        else:
            database[email] = [name, password]
            with open('db.json', 'w') as wf:
                json.dump(database, wf)
                return 0

    def check_data(self, email, password):
        with open('db.json', 'r') as rf:
            database = json.load(rf)

        if email in database and database[email][1] == password:
            return True
        else:
            return False
