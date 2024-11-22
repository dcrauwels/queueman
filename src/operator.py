import visitor, queue

class Operator:
    # describes a user calling visitors and tracking their state
    def __init__(
            self,
            queue = None,
            current_visitor = None
            purpose = None
            ):
        self.__queue = queue
        self.__current_visitor = current_visitor
        self.__purpose = purpose

    def call_next(visitor_order = True):
        # calls next visitor in the queue (status 1)
        pass

    def serve_visitor(visitor):
        # mark visitor as served (status 2) and remove them from queue
        pass

    def get_waiting_visitors(purpose = None):
        # returns a list of waiting visitors
        pass
    
    def change_queue_order(purpose = None):
        pass




