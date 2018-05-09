import argparse 

class InitAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        pass 


def create_parser():
    parser = argparse.ArgumentParser(
        description="""
            Additional Docker helper method.
        """
    )
    group = parser.add_mutually_exclusive_group()            
    group.add_argument("-c", '--config', help='Get config files of a container', metavar="CONTAINER_ID")

    group.add_argument('-i', "--info", help="Get some infos", action="store_true")
    group.add_argument('-l', "--list", help="List IDs of running containers",  action="store_true")

    return parser

def main():
    from dutils import actions 
    parser = create_parser()
    args = vars(parser.parse_args())
    print(args)
    if args["list"] : 
        actions.list_containers_ids()

