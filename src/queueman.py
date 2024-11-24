from visitor import Visitor
from queue import Queue
import argparse

# simplistic version of a CLI. Not supporting operator yet.
def main():
    q = Queue()
    q.load_from_json()

    parser = argparse.ArgumentParser(
            prog = "Queue Manager CLI",
            description = "Simplistic queue manager prototype. Allows you to add and call visitors from a queue."
            )
    subparsers = parser.add_subparsers(dest = "command")

    # Add
    add_parser = subparsers.add_parser("add", help = "Add a new visitor to the queue.")
    add_parser.add_argument("name", help = "Set visitor name. Optional.", default = None)
    add_parser.add_argument("purpose", help = "Set visitor purpose. Optional.", default = None)

    # Call
    call_parser = subparsers.add_parser("call", help = "Call a visitor from the queue.")
    call_parser.add_argument("purpose", help = "Priority call from a specific purpose queue. Optional.", default = None)

    # View queue
    view_parser = subparsers.add_parser("view", help = "View the queue status.")
    view_parser.add_argument("purpose", help = "View queue for a specific purpose. Optional.", default = None)

    # actual argument parsing
    args = parser.parse_args()

    if args.command == "add":
        q.add_visitor(Visitor(args.purpose, args.name, len(q.get_queue()) + 1))
    elif args.command == "call":
        try:
            v = q.get_visitor(args.purpose)
            print(v)
        except ValueError:
            print("Queue is empty.")
    elif args.command == "view":
        if len(q.get_queue()) > 0:
            print(q)
            for l in q.get_queue():
                print(l)
        else:
            print("Queue is empty.")

    # save to JSON
    q.save_to_json()

if __name__ == "__main__":
    main()
