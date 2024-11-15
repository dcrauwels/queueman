import visitor

class Queue:
    # Manages visitors as defined in visitor.py

    # __init__
    def __init__(self, purposes: list = []) -> None:
        # queue attribute: list of visitors
        self.__queue = []
        
        # purpose_queues attribute: dictionary of Queues
        if len(purposes) > 0: 
            self.__purpose_queues = dict.fromkeys(purposes, Queue()) # init dict
        else:
            self.__purpose_queues = {} # not sure if needed

        return None

    # methods
    ## add queue to purpose_queues attribute
    def add_queue(self, purpose: str):
        if purpose in self.__purpose_queues:
            raise ValueError("Purpose already in queue.")
        else:
            self.__purpose_queues[purpose] = Queue()

        
    ## add visitor to the queue and also in purpose queue if needed
    def add_visitor(self, visitor) -> None:
        # append to main queue
        self.__queue.append(visitor)

        # append to purpose-queue dict
        purpose = visitor.get_purpose()
        if purpose in self.__purpose_queues:
            self.__purpose_queues[purpose].add_visitor(visitor)
        else: 
            self.__purpose_queus[purpose] = Queue()

        # return
        return None

    ## get visitor (either FIFO or purpose)
    def get_visitor(
            self, 
            purpose: str = None, # either take visitor 
            position: int = -1, # allows you to fetch a specific visitor position
            ) -> visitor:

        # update position
        if position == -1:
            position = len(self.__queue)
        # return FIFO 
        if purpose == None:
            return self.__queue[position]
        else:
            return self.__purpose_queues[purpose]
        if position == 0 and :
            
        return get_visitor(purpose, position - 1)

    ## remove_visitor
