import json
from visitor import Visitor
from queue import Queue

class Operator:
    # describes a user calling visitors and tracking their state

    statuses = ["Offline", "Ready", "Working"]
    
    # init
    def __init__(
            self,
            name: str = "Operator",
            desk: int = None, # currently an int for the visitor class as well
            status: str = "Offline",
            ):
        self.__name = name
        self.__desk = desk
        self.__status = status

    def __repr__(self):
        return f"Operator: name {self.get_name()}, desk {self.get_desk()}, status {self.get_status()}."
        
    
    # get attributes
    def get_name(self) -> str:
        return self.__name
    def get_desk(self) -> int:
        return self.__desk
    def get_status(self) -> str:
        return self.__status

    # copy operator
    def copy_operator(self, other_op: 'Operator') -> None:
        # for the load_from_json() function really
        self.__name = other_op.get_name()
        self.__desk = other_op.get_desk()
        self.__status = other_op.get_status()
        return None

    # set status
    def set_status(self, status:str = "Ready") -> None:
        if status in Operator.statuses:
            self.__status = status
            return None
        else:
            raise ValueError(f"Status must be in {Operator.statuses}")

    def set_name(self, name:str = "Operator") -> None:
        self.__name = name
        return None

    def set_desk(self, desk:int = None) -> None:
        self.__desk = desk
        return None
    
    # visitor operations
    ## call visitor
    def call_next(queue, purpose: str = None, position: int = 0, visitor: Visitor = None) -> None:
        # calls next visitor in the queue (status 1)
        
        # serve previous visitor if one is present
        if visitor is not None:
            self.serve_visitor(visitor)

        # get new visitor and set status to called (1)
        visitor = queue.get_visitor(purpose, position)
        visitor.set_status(1)

        # set own status to working (2)
        self.set_status(2)

        # return
        return None
        
    ## directly set visitor to served
    def serve_visitor(self, visitor) -> None:
        # mark visitor as served (status 2) and remove them from queue
        visitor.set_status(2)
        self.set_status(1)
        return None

    ## conversion to and from dict(). Needed for JSON io
    ### operator from dict
    @classmethod
    def from_dict(cls, data) -> 'Operator':
        return cls(
                data["name"],
                data["desk"],
                data["status"]
                )


    ### operator to dict
    def to_dict(self) -> dict:
        return {
                "name": self.get_name(),
                "desk": self.get_desk(),
                "status": self.get_status()
                }

    ## JSON import and export
    ### import from json
    @classmethod
    def load_from_json(cls, name: str = "Operator", path:str = "") -> "Operator":
        if path == "":
            path = f"database/operator.json"
        try:
            with open(path, 'r') as f:
                data = json.load(f)
                return cls.from_dict(data) 
        except FileNotFoundError:
            print("W: No existing operator file found. Initializing empty operator.")
            return cls()

    ### export to json
    def save_to_json(self, path:str = "") -> None:
        if path == "":
            path = f"database/operator.json"
        with open(path, 'w') as f:
            json.dump(self.to_dict(), f)
        return None


