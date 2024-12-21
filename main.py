from scripts.utils import setup_logging, parse_arguments
from scripts.RawClean import RawClear
from scripts.config import LOG_FILE

def main():
    try: 
        if not setup_logging(LOG_FILE):
            print("Failed to initialise logging.")
            return 

        # get CML arguments 
        args = parse_arguments()

        # initialise RawClear
        raw_clear = RawClear(args.path, args.extensions)

        # get summary 
        summary = raw_clear.get_summary()
        print("\U0001F4DD Configuration Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")
        
        # start file transfer 
        transferred_files = raw_clear.tsf_files()
        print(f"\U00002705 Successfully transferred {transferred_files} files.")
    
    except KeyboardInterrupt:
        print("\n\U0001F6A8 Operation cancelled by the user.")
    except Exception as e: 
        print(f"\U0000274C An error occurred: {e}")

if __name__ == "__main__":
    main()