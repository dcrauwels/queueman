import json
from visitor import Visitor
from collections import deque


class Queue(deque):
    # Manages visitors as defined in visitor.py

    # transforms
    ## __init__
    def __init__(
            self, 
            name: str = None,
            *args,
            **kwargs
            ) -> None:
        # queue attribute: list of visitors
        super().__init__(*args, **kwargs)
        self.__name = None # see set_name()

    ## __repr__
    def __repr__(self):
        return f"Queue() '{self.get_name()}' of {self.get_visitor_count()} visitors."

    # methods
    ## other methods
    ### sort queue
    def sort_queue(self, *args, **kwargs) -> None:
        items = list(self)
        items.sort(*args, **kwargs)
        self.clear()
        self.extend(items)
        return None


    ## get methods
    ### return queue name
    def get_name(self) -> str:
        return self.__name
    
    ### return purposes 
    def get_purposes(self) -> set:
        result = set()
        for v in self:
            p = v.get_purpose()
            if p is not None and p not in result:
                result.add(p)
        return result

    ### return Queue filtered for purpose
    def get_purpose_filtered(self, purpose: str) -> 'Queue':
        return Queue(self.get_name(), [x for x in self if x.get_purpose() == purpose])

    ### return visitor (either FIFO or purpose)
    def get_visitor(
            self, 
            purpose: str = None, # pure fifo (None) versus filtered fifo
            position: int = 0, # fifo (0) versus specified customer
            ) -> Visitor:

        # sort queue
        self.sort_queue()
        
        # return visitor
        '''Note that I check first for position, then for purpose. I.e. position overrides purpose.'''
        if position != 0: # specified customer
            return self.pop(position)
        elif purpose is None: # easiest scenario, pure fifo, no filter
            return self.popleft()
        elif purpose in self.get_purposes():
            for i,v in enumerate(self):
                if v.get_purpose() == purpose:
                    return self.pop(i)
        else:
            raise Exception("Purpose not found in queue.")


    ### return waiting count, optionally with purpose filtering
    def get_visitor_count(self, purpose=None) -> int:
        if purpose is None:
            return len(self)
        elif len(self) > 0:
            return len([x for x in self if x.get_purpose() == purpose])  
        else:
            return 0

    ### return a list of all waiting visitors with waiting times
    # I think this will not be needed
    def get_all_waiting(self) -> list:
        from datetime import datetime
        result = [(v, datetime.now() - v.get_datetime()) for v in self.get_queue()]
        return result


    ## add methods
    ### set name
    def set_name(self, name: str) -> None:
        self.__name = name
        return None
    
    ### replace queue
    ### NOTE that this FULLY replaces the queue with a new list of visitors. Do not call this lightly!
    def replace_queue(self, name:str = None, rep: list = []) -> None:
        # fully replace queue
        self.set_name(name)
        self.clear()
        self.extend(rep)
        return None

    ### add visitor to the queue, can be given priority (first position in queue)
    def add_visitor(self, visitor, priority: bool = False) -> None:
        # append to main queue
        self.append(visitor)
        
        # sort queue
        self.sort_queue()

        # set priority position
        if priority:
            self.rotate()

        # return
        return None


    ## remove_visitor
    def remove_visitor(self, visitor:Visitor = None) -> Visitor:
        # remove a specific visitor from the queue or the last one
        if visitor is None:
            return self.pop()
        else:
            self.remove(visitor)
            return visitor

    
    ## JSON import and export
    ### export
    def save_to_json(self, path:str = "") -> None:
        if path == "":
            path = f"database/{self.get_name()}_queue.json"
        with open(path, 'w') as f:
            queue_name = self.get_name()
            queue_contents = [visitor.to_dict() for visitor in self]
            json_dict = {"name": queue_name, "contents": queue_contents}
            json.dump(json_dict, f)
        return None

    ### import
    def load_from_json(self, name: str = None, path:str = "") -> None:
        if path == "":
            path = f"database/{self.get_name()}_queue.json"
            print(path)
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                #print(data)
                #print([Visitor.from_dict(v) for v in data["contents"]])
                self.replace_queue(
                        name = data["name"],
                        rep = [Visitor.from_dict(v) for v in data["contents"]]
                        )
                print(self)
        except FileNotFoundError:
            print("W: No existing database file found. Initializing empty queue.")
            self.replace_queue()
        return None


def main():
    pass

if __name__ == "__main__":
    main()
