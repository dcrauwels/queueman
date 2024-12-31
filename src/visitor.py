import time, uuid

class Visitor:
    # track count of overall visitors
    visitor_count = 0
    visitor_statuses = ["waiting", "called", "served"]

    # __init__ 
    def __init__(
            self,
            purpose: str = None,
            name: str = None,
            number: str = 'a',
            timestamp = 0,
            desk: int = 0,
            status: int = 0,
            ):
        ## self-referring
        self.__purpose = purpose
        self.__name = name
        ## default inits
        self.__desk = desk
        self.__status = self.visitor_statuses[status] # always inits to "waiting"
        Visitor.visitor_count += 1
        self.__number = number if number != 'a' else str(uuid.uuid4())
        self.__timestamp = time.time() if timestamp == 0 else timestamp # when did the visitor get in queue
        self.__time_served = 0 # when did the visitor get called

    # __repr__
    def __repr__(self):
        return f"ID: {self.get_number()}; Name: {self.get_name()}; Purpose: {self.get_purpose()}; Time: {self.get_datetime()}"

    # get methods
    def get_status(self) -> str:
        return self.__status
    def get_number(self) -> int:
        return self.__number
    def get_purpose(self) -> str:
        return self.__purpose
    def get_timestamp(self):
        return self.__timestamp
    def get_datetime(self):
        from datetime import datetime
        return datetime.fromtimestamp(self.__timestamp)
    def get_desk(self) -> int: # NOTE THIS MAY NOT TURN OUT TO BE AN INT
        return self.__desk
    def get_time_served(self) -> float:
        return float(self.__time_served)
    def get_name(self) -> str:
        return self.__name
    
    # assign desk method
    def call_visitor(self, operator) -> None:
        self.__desk = operator.desk # NYI
        self.__status = self.visitor_statuses[1]
        self.__time_served = time.time()

    # set status
    def set_status(self, status: int):
        if status < 0 or status > 2:
            raise ValueError("Status must be between 0 and 2.")
        self.__status = self.visitor_statuses[status]

    # export to dict
    def to_dict(self):
        return {
                "purpose": self.get_purpose(),
                "name": self.get_name(),
                "number": self.get_number(),
                "timestamp": self.get_timestamp(),
                "desk": self.get_desk(),
                "status": self.visitor_statuses.index(self.get_status())
                }

    # import from dict
    @classmethod
    def from_dict(cls, data):
        return cls(
                data["purpose"],
                data["name"],
                data["number"],
                data["timestamp"],
                data["desk"],
                data["status"]
                )

def main():
    pass

if __name__ == "__main__":
    main()
