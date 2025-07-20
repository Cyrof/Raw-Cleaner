# Raw Cleaner 
Raw Cleaner is a Python-based tool designed to organise and transfer files from a specified directory to a new destination folder. It allows users to specify file extensions for selective file management. The tool is modular and user-friendly, supporting optional configurations.

## Folder Structure 
```bash 
.
├── main.py
├── README.md
├── requirements.txt
└── scripts
    ├── config.py
    ├── __init__.py
    ├── RawClean.py
    └── utils.py
```

## Prerequisites 
- Python 3.10+ installed on your system 
- [uv](https://docs.astral.sh/uv/) package manager installed

## Installation 
1. **Clone the Repository**: 
    ```bash 
        git clone https://github.com/Cyrof/Raw-Cleaner.git
        cd Raw-Cleaner 
    ```

2. **Install Dependencies using `uv`**:
    ```bash
    uv sync
    ```

## Usage 
Run the application with the following command: 
```bash 
uv run cleaner <path_to_folder> --extentions <ext1 ext2>
```
### Arguments: 
- `<path_to_folder>`: Path to the directory containing the target files. 
- `--extentions` _(Optional)_: Space-separated file extensions to process (e.g., `jpg png`). If not provided, only `.jpg` files are processed.

### Examples:
- Process only `.jpg` files _(default behavior)_: 
    ```bash 
    uv run cleaner "/path/to/photos"
    ```
- Process `.jpg` and `.png` files: 
    ```bash 
    uv run cleaner "/path/to/photos" --extensions jpg png
    ```
- View help menu:
    ```bash
    uv run cleaner -h
    ```

## Output 
Processd files are transferred to a new folder named: 
```bash 
    <original_folder_name>-raw-clean
```
This folder will be located in the same parent directory as the source folder. 

## Features 
- **Default Extension Handling**: Processes `.jpg` files by default. 
- **Custom Extensions**: Supports multiple file extensions via the `--extensions` flag. 
- **Parallel Processing**: Faster file transfers using multi-threading. 
- **Logging**: Detailed logs are saved to `rawclear.log` for debugging and auditing. 
- **Progress Bar**: Real-time progress updates with `tqdm`. 

## License 
This project is licensed under the [Apache 2.0](https://github.com/Cyrof/Raw-Cleaner/blob/main/LICENSE)

## Contributing
1. Fork the repository. 
2. Create a feature branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature-branch` 
5. Open a pull request.
