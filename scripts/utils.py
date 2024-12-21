import argparse
import logging 

def setup_logging(log_file: str) -> bool:
    try:
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler(), logging.FileHandler(log_file)] 
        )
        logging.info("Logging initialised successfully.")
        return True
    except Exception as e: 
        print(f"Failed to set up logging: {e}")
        return False

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Transfer specified file types from a directory to a new directory."
    )

    parser.add_argument(
        "path",
        type=str,
        help="Path to the directory containing files."
    )
    
    parser.add_argument(
        "--extensions",
        type=str,
        nargs="+",
        default=['jpg'],
        help="File extensions to transfer (e.g., --extensions jpg png)."
    )
    return parser.parse_args()