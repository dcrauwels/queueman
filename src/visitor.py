class Visitor:
    # track number of overall visitors
    visitor_count = 0

    # __init__ 
    def __init__(
            self,
            purpose: str = "",
            ):
        ## imports
        import time
        ## self-referring
        self.__purpose = purpose
        ## default inits
        self.__desk = 0
        self.__served = False # always inits to False
        Visitor.visitor_count += 1
        self.__count = Visitor.visitor_count # how many visitors since start of run
        self.__timestamp = time.time() # when did the visitor get in queue
        self.__time_served = 0 # when did the visitor get called

    # get methods
    def get_served(self):
        return self.__served
    def get_count(self):
        return self.__count
    def get_purpose(self_):
        return self.__purpose
    def get_timestamp(self):
        return self.__timestamp
    def get_datetime(self):
        from datetime import datetime
        return datetime.fromtimestamp(self.__timestamp)
    def get_desk(self):
        return self.__desk
    def get_time_served(self):
        return self.__time_served
    
    # assign desk method
    def set_desk(self, desk):
        self.__desk = desk
        self.__served = True
        self.__time_served = time.time()

def main():
    pass

if __name__ == "__main__":
    main()
