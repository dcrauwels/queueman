import json
from visitor import Visitor
from collections import deque

class Queue:
    # Manages visitors as defined in visitor.py

    # transforms
    ## __init__
    def __init__(
            self, 
            inner: bool = False, # defines whether we are inside of a purpose Queue or in the outer queue
            purposes: list = []
            ) -> None:
        # queue attribute: list of visitors
        self.__queue = deque()
        self.__inner = inner
        
        # purpose_queues attribute: dictionary of Queues
        if len(purposes) > 0: 
            self.__purpose_queues = dict.fromkeys(purposes, Queue(True)) # init dict
        else:
            self.__purpose_queues = {} # not sure if needed

        return None

    ## __getitem__ (this is self["purpose1"] implementation)
    def __getitem__(self, key):
        return self.__purpose_queues[key]

    ## __repr__
    def __repr__(self):
        return f"Queue() of {self.get_waiting_count()} visitors."

    # methods
    ## get methods
    ### return main queue
    def get_queue(self):
        return self.__queue

    def get_inner(self) -> bool:
        return self.__inner
    
    ### return purposes (keys from dict)
    def get_purposes(self):
        return self.__purpose_queues.keys()

    ### return visitor (either FIFO or purpose)
    def get_visitor(
            self, 
            purpose: str = None, # either take visitor 
            position: int = -1, # allows you to fetch a specific visitor position
            ):

        # update position
        if position == -1:
            position = len(self.get_queue())
            if position == 0:
                raise ValueError("Queue.get_visitor(): Queue is empty.")

        # return visitor
        if purpose == None:
            return self.get_queue()[position - 1]
        else:
            return self[purpose][position - 1]

    ### return waiting count, optionally with purpose filtering
    def get_waiting_count(self, purpose=None) -> int:
        if purpose is None:
            return len(self.get_queue())
        else:
            try:
                return len(self[purpose].get_queue())
            except:
                raise KeyError(f"Queue.get_waiting_count({purpose}): Purpose not part of queue.")

    ### return a list of all waiting visitors with waiting times
    def get_all_waiting(self) -> list:
        from datetime import datetime
        result = [(v, datetime.now() - v.get_datetime()) for v in self.get_queue()]
        return result

    ## add methods
    ### replace queue
    ### NOTE that this FULLY replaces the queue with a new list of visitors. Do not call this lightly!
    def replace_queue(self, rep: list) -> None:
        self.__queue = deque(rep) # fully replace queue
        # replace purpose queues next:
        self.__purpose_queues = dict() # set up empty dict
        for v in rep: # iterate over all visitors in replacement list
            p = v.get_purpose() # store purpose
            if p is not None: # in case it has a purpose
                try:
                    self.add_purpose_queue(p) # add purpose queue
                except ValueError:
                    print(f"W: Purpose {p} already in queue.") # warning message, might toss out
                finally:
                    self[p].add_visitor(v)
                    
        return None


    ### add queue to purpose_queues dict attribute
    def add_purpose_queue(self, purpose: str) -> None:
        # check for duplicate purpose
        if purpose in self.get_purposes():
            raise ValueError(f"Queue.add_purpose_queue({purpose}): Purpose already in queue.")
        else:
            self.__purpose_queues[purpose] = Queue(True)
        # return
        return None

        
    ### add visitor to the queue and also in purpose queue if needed
    def add_visitor(self, visitor) -> None:
        # append to main queue
        self.__queue.append(visitor)

        # append to purpose-queue dict
        purpose = visitor.get_purpose()
        if purpose is not None and self.get_inner() == False:
            if purpose in self.get_purposes():
                self[purpose].add_visitor(visitor)
            else: 
                self.add_purpose_queue(purpose)
                self[purpose].add_visitor(visitor)   

        # return
        return None


    ## remove_visitor
    def remove_visitor(self, visitor = None) -> None:
        # remove a specific visitor from the queue or the last one
        
        # get purpose
        purpose = visitor.get_purpose()

        # remove from main queue
        self.__queue.remove(visitor)

        # remove from purpose queue if needed
        if purpose is not None:
            try:
                self.__queue[purpose].remove_visitor(visitor)
            except:
                raise KeyError(f"Queue.remove_visitor(): Purpose '{purpose}' not part of queue but on visitor.")

        return None

    
    ## JSON import and export
    ### export
    def save_to_json(self, path = "database/queue.json"):
        with open(path, 'w') as f:
            json.dump([visitor.to_dict() for visitor in self.get_queue()], f)

    ### import
    def load_from_json(self, path = "database/queue.json"):
        try:
            with open(path, 'r') as f:
                self.replace_queue([Visitor.from_dict(data) for data in json.load(f)])
        except FileNotFoundError:
            self.replace_queue([])

            


def main():
    pass

if __name__ == "__main__":
    main()
