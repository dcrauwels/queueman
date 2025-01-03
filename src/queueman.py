import argparse
from visitor import Visitor

# simplistic version of a CLI. Not supporting operator yet.
def main():
    from queue import Queue
    q = Queue()
    q.load_from_json()
    print(q)

    parser = argparse.ArgumentParser(
            prog = "Queue Manager CLI",
            description = "Simplistic queue manager prototype. Allows you to add and call visitors from a queue."
            )
    subparsers = parser.add_subparsers(dest = "command")

    # subparsers
    ## Add
    add_parser = subparsers.add_parser("add", help = "Add a new visitor to the queue.")
    add_parser.add_argument("--name", help = "Set visitor name. Optional.", nargs = '?', const = None, type = str)
    add_parser.add_argument("--purpose", help = "Set visitor purpose. Optional.", nargs = '?', const = None, type = str)

    ## Call
    call_parser = subparsers.add_parser("call", help = "Call a visitor from the queue.")
    call_parser.add_argument("--purpose", help = "Priority call from a specific purpose queue. Optional.", nargs = '?', const = None, type = str)

    ## View queue
    view_parser = subparsers.add_parser("view", help = "View the queue status.")
    view_parser.add_argument("--purpose", help = "View queue for a specific purpose. Optional.", nargs = '?', const = None, type = str)

    ## Set operator
    operator_parser = subparsers.add_parser("operator", help = "Modify operators and set one in use.")
    operator_parser.add_argument("op", help = "Choose operator. Sets local operator ID.", nargs = '?', const = None, type = str)
    operator_parser.add_argument("--desk", help = "Set desk associated with operator. Optional.", nargs = '?', const = None, type = str)
    operator_parser.add_argument("--create", help = "Create new operator with the previously defined parameters. Optional.", nargs = '?', const = None, type = bool)

    ## List operators
    loper_parser = parser.add_argument("--loper", help = "List all operators in use.")

    # actual argument parsing
    args = parser.parse_args()
    print(args)

    if args.command == "add":
        q.add_visitor(Visitor(args.purpose, args.name))
    elif args.command == "call":
        try:
            v = q.get_visitor(args.purpose)
            print(v) # NOTE of course just printing is not sufficient.
        except ValueError:
            print("Queue is empty.")
    elif args.command == "view":
        if len(q) > 0:
            print(q)
            for l in q:
                print(l)
        else:
            print("Queue is empty.")

    # save to JSON
    q.save_to_json()

if __name__ == "__main__":
    main()
