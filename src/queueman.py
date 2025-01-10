import argparse
from visitor import Visitor

# simplistic version of a CLI. Not supporting operator yet.
def main():
    # import queue and operator
    from queue import Queue
    q = Queue()
    q.load_from_json()
    from queue_operator import Operator
    o = Operator.load_from_json()
    if o.get_name() == "Operator":
        print("W: No operator name specified. Consult -h or --help for more instructions.")

    parser = argparse.ArgumentParser(
            prog = "Queue Manager CLI",
            description = "Simplistic queue manager prototype. Allows you to add and call visitors from a queue."
            )
    subparsers = parser.add_subparsers(dest = "command")

    # subparsers
    ## Add
    add_parser = subparsers.add_parser("add", help = "Add a new visitor to the queue.")
    add_parser.add_argument("-n", "--name", help = "Set visitor name. Optional.", nargs = '?', const = None, type = str)
    add_parser.add_argument("-p", "--purpose", help = "Set visitor purpose. Optional.", nargs = '?', const = None, type = str)

    ## Call
    call_parser = subparsers.add_parser("call", help = "Call a visitor from the queue.")
    call_parser.add_argument("-p", "--purpose", help = "Priority call from a specific purpose queue. Optional.", nargs = '?', const = None, type = str)

    ## View queue
    view_parser = subparsers.add_parser("view", help = "View the queue status.")
    view_parser.add_argument("-p", "--purpose", help = "View queue for a specific purpose. Optional.", nargs = '?', const = None, type = str)

    ## Set operator
    operator_parser = subparsers.add_parser("operator", help = "Modify operators and set one in use.")
    operator_parser.add_argument("name", help = "Set operator name.", nargs = '?', type = str)
    operator_parser.add_argument("-d", "--desk", help = "Set desk associated with operator. Optional.", nargs = '?', const = None, type = int)
    operator_parser.add_argument("-s", "--status", help = "Set operator status. Optional.", nargs = '?', const = "Ready", default = "Ready", type = str)

    # actual argument parsing
    args = parser.parse_args()
    #print(f"hi {args}") # NOTE this is debugging purposes for now

    if args.command == "add":
        q.add_visitor(Visitor(args.purpose, args.name))
    elif args.command == "call":
        try:
            v = q.get_visitor(args.purpose)
            print(v) # NOTE of course just printing is not sufficient.
        except ValueError:
            print("Queue is empty.")
    elif args.command == "view":
        print(o)
        if len(q) > 0:
            print(q)
            for l in q:
                print(l)
        else:
            print("Queue is empty.")
    elif args.command == "operator":
        o.set_name(args.name)
        o.set_status(args.status)
        o.set_desk(args.desk)

    # save to JSON
    q.save_to_json()
    o.save_to_json()

if __name__ == "__main__":
    main()
