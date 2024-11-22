class Visitor:
    # track number of overall visitors
    visitor_count = 0
    visitor_statuses = ["waiting", "called", "served"]

    # __init__ 
    def __init__(
            self,
            purpose: str = None,
            name: str = None,
            ):
        ## imports
        import time
        ## self-referring
        self.__purpose = purpose
        self.__name = name
        ## default inits
        self.__desk = 0
        self.__status = self.visitor_statuses[0] # always inits to "waiting"
        Visitor.visitor_count += 1
        self.__id = Visitor.visitor_count # how many visitors since start of run
        self.__timestamp = time.time() # when did the visitor get in queue
        self.__time_served = 0 # when did the visitor get called

    # get methods
    def get_status(self) -> str:
        return self.__status
    def get_count(self) -> int:
        return self.__id
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

def main():
    pass

if __name__ == "__main__":
    main()
