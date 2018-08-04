MOCK_USERS = [{
                "email": "test@example.com",
               "salt": "gCioHZKNFMMsH6oJEJI+",
               "hashed": "3cdd526869a0e59cfaa81bfecd9aa10e1b37af5dd4a98ea3e8051761c611ee77a4964eba68c09c7af9f40675a607549806ebc49b270902a44e1f91ab6a7e1fa9"
               }]

class MockDBHelper:

    def get_user(self, email):
        user = [x for x in MOCK_USERS if x.get("email") == email]
        if user:
            return user[0]
        return None

    def add_user(self, email, salt, hashed):
        MOCK_USERS.append({"email":email, "salt": salt, "hashed": hashed})
