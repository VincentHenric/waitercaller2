MOCK_USERS = [{
                "email": "test@example.com",
               "salt": "gCioHZKNFMMsH6oJEJI+",
               "hashed": "3cdd526869a0e59cfaa81bfecd9aa10e1b37af5dd4a98ea3e8051761c611ee77a4964eba68c09c7af9f40675a607549806ebc49b270902a44e1f91ab6a7e1fa9"
               }]

MOCK_TABLES = [{
                "_id": "1",
                "number": "1",
                "owner": "test@example.com",
                "url": "mockurl"
              }]

class MockDBHelper:

    def add_table(self, number, owner):
        MOCK_TABLES.append({"_id": number, "number": number, "owner": owner})
        return number

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email":email, "salt": salt, "hashed": hashed})

    def delete_table(self, table_id):
        for i, table in enumerate(MOCK_TABLES):
            if table.get("_id") == table_id:
                del MOCK_TABLES[i]
                break

    def get_tables(self, owner_id):
        return MOCK_TABLES

    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def update_table(self, _id, url):
        for table in MOCK_TABLES:
            if table.get("_id") == _id:
                table["url"] = url
                break
