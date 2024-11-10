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
        self.__count = Visitor.visitor_count
        self.__timestamp = time.time()

    # report methods
    def report_served(self):
        return self.__served
    def report_count(self):
        return self.__count
    def report_purpose(self_):
        return self.__purpose
    def report_timestamp(self):
        return self.__timestamp
    def report_datetime(self):
        from datetime import datetime
        return datetime.fromtimestamp(self.__timestamp)
    def report_desk(self):
        return self.__desk
    
    # assign desk method
    def set_desk(self, desk):
        self.__desk = desk
        self.__served = True

def main():
    import time

    visitor1 = Visitor()
    time.sleep(2)
    visitor2 = Visitor()
    
    print(visitor1.report_served())
    visitor1.set_desk(1)
    print(visitor1.report_served())

    print(visitor2.report_datetime().second - visitor1.report_datetime().second)

if __name__ = "__main__":
    main()
