import json
from visitor import Visitor
from queue import Queue

class Operator:
    # describes a user calling visitors and tracking their state

    statuses = ["Offline", "Ready", "Working"]

    def __init__(
            self,
            name: str = "Operator",
            desk: int = None, # currently an int for the visitor class as well
            status: int = 0,
            ):
        self.__name = name
        self.__desk = desk
        self.__status = statuses[status]

    def set_status(self, status:int = 0):
        self.__status = statuses[status]

    def call_next(queue, purpose: str = None, position: int = 0, visitor: Visitor = None):
        # calls next visitor in the queue (status 1)
        
        # serve previous visitor if one is present
        if visitor is not None:
            self.serve_visitor(visitor)

        # get new visitor and set status to called (1)
        visitor = queue.get_visitor(purpose, position)
        visitor.set_status(1)

        # set own status to working (2)
        self.set_status(2)
        

    def serve_visitor(self, visitor):
        # mark visitor as served (status 2) and remove them from queue
        visitor.set_status(2)
        self.set_status(1)

