from pgsql import connect, load
import argparse

FOLDER = "data"

def main(args):
    if args.skip:
        pass
    else:
        engine = connect.get_engine()
        load.process_csv_folder(FOLDER, engine=engine)
        pass

def parse_args():
    """Pass command line arguments to the script."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--folder", 
        type=str, 
        default="data", 
        help="The path to the data folder. Default: `data`"
    )
    parser.add_argument(
        "--skip",
        type=bool,
        default=False,
        help="Option to skip data load into database. Default: False."
    )
    args = parser.parse_args()
    return args

if __name__=="__main__":
    args = parse_args()
    main(args)


