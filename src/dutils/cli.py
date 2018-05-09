import argparse
import fnmatch, re

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
    group.add_argument("-i", '--init', help='Initialize Docker files for the specified version',
            nargs='*',
            metavar=("HYBRIS_VERSION"),
            action=InitAction)

    group.add_argument("--info", help="Get some infos", action="store_true")
    group.add_argument("--stop", help="Stops the last recipe", action="store_true")
    group.add_argument("--list", help="List available recipes", action="store_true")
    group.add_argument("--clean", help="Cleaning", action="store_true")

    return parser

def main():
    from hybr import actions
    parser = create_parser()
    args = vars(parser.parse_args())
    # print(args)
    if "hversion" in args :
        actions.init(args['hversion'], args["hpath"])
    elif "recipe_name" in args:
        actions.startRecipe(args["recipe_name"])        
    elif args["info"]:
        actions.get_infos()
    elif args["list"]:
        actions.list_recipes()
    elif args["stop"]:
        actions.stop_services()
    elif args["clean"]:
        actions.clean()
    else:
        parser.print_help()
