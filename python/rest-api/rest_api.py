import json

class RestAPI:

    def __init__(self, database=None):
        self.database = {}

        # load database in the following form
        # { "Adam:": {{"name": "Adam", "owes": {}}}
        if database != None:
            for user in database["users"]:
                self.database[user["name"]] = user

    def __get_for_all(self):
        ans = {"users":[]}

        for name in self.database:
            ans["users"].append(self.database[name])
        
        return ans
    
    def __get_for_specific(self, filtered_names):
        ans = {"users":[]}

        for name in filtered_names:
            if name in self.database:
                ans["users"].append(self.database[name])
        
        return ans

    def __create_user(self, payload):
        name = payload["user"]

        if name not in self.database:
            summary = {"name": name, "owes": {}, "owed_by":{}, "balance": 0.0}
            self.database[name] = summary
        
        users = self.__get_for_specific([name])
        
        return users["users"][0]
    
    def __update_lender(self, lender_name, borrower_name, amount):
        lender = self.database[lender_name]
        owes_amount = 0.0

        if borrower_name in lender["owes"]:
            owes_amount = lender["owes"][borrower_name]

        if owes_amount == amount:
            # debt is clear
            lender["owes"].pop(borrower_name)
        elif owes_amount > amount:
            # still some debt is left
            lender["owes"][borrower_name] -= amount
        else:
            # debt is cleared, and is now owed by borrower
            if borrower_name in lender["owes"]:
                lender["owes"].pop(borrower_name)
            owed_by_amount = amount - owes_amount
            lender["owed_by"][borrower_name] = owed_by_amount
        
        # always update the balance
        lender["balance"] += amount

    def __update_borrower(self, lender_name, borrower_name, amount):
        borrower = self.database[borrower_name]
        owed_by_amount = 0.0

        if lender_name in borrower["owed_by"]:
            owed_by_amount = borrower["owed_by"][lender_name]

        if owed_by_amount == amount:
            # balance is clear
            borrower["owed_by"].pop(lender_name)
        elif owed_by_amount > amount:
            # still some balance is left
            borrower["owed_by"][lender_name] -= amount
        else:
            # debt is cleared, and is now owes to lender
            if lender_name in borrower["owed_by"]:
                borrower["owed_by"].pop(lender_name)
            owes_amount = amount - owed_by_amount
            borrower["owes"][lender_name] = owes_amount
        
        borrower["balance"] -= amount

    def __create_iou(self, payload):
        lender_name = payload["lender"]
        borrower_name = payload["borrower"]
        amount = payload["amount"]


        # update/add entry in lender
        self.__update_lender(lender_name, borrower_name, amount)
        self.__update_borrower(lender_name, borrower_name, amount)

        # get the user objects for lender and borrower
        names = [lender_name, borrower_name]
        names.sort()

        users = self.__get_for_specific(names)

        return users
    
    def get(self, url, payload=None):
        ans = None

        if payload != None:
            payload = json.loads(payload)
            filtered_names = payload["users"]
            filtered_names.sort()

            ans = self.__get_for_specific(filtered_names)
            
        else:
            ans = self.__get_for_all()
            
        return json.dumps(ans)

    def post(self, url, payload=None):
        payload = json.loads(payload)

        if payload == None or url == None:
            return

        if url == "/add":
            res = self.__create_user(payload)
            return json.dumps(res)
        elif url == "/iou":
            return json.dumps(self.__create_iou(payload))
        else:
            return