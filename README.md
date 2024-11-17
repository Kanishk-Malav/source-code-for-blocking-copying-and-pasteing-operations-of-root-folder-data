> Block Copy-Paste Operations for Root Folder Data

This project implements software to restrict users from copying and pasting files or content from a specific "root" folder to any location outside this folder, including external drives or cloud locations. The system continuously monitors the clipboard to ensure that any copy-paste attempts adhere to the restrictions set on the root folder.

>> Features
>> Monitor Clipboard: The system continuously checks the clipboard to see if a file path is copied.
>> Root Folder Restrictions: 
  - If content is copied from the root folder (or its subfolders), it can only be pasted back into the root folder or its subfolders.
  - If content is copied from outside the root folder, it can be pasted anywhere, including the root folder.
>> Real-time Monitoring**: The script runs in real-time, monitoring the clipboard and applying restrictions as soon as the user attempts to copy-paste content.

>> Folder Structure

In this example, the `root` folder contains subfolders and files. When content is copied from the root, it can only be pasted within this folder and its subdirectories.

>> Requirements

This project requires Python and the following libraries:
- `pywin32` (for clipboard access on Windows)
- `pyperclip` (for clipboard operations)

You can install the required libraries using `pip`.

>> Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Kanishk-Malav/C---source-code-for-blocking-copying-and-pasteing-operations-of-root-folder-data.git
    cd C---source-code-for-blocking-copying-and-pasteing-operations-of-root-folder-data
    ```

2. Create a Virtual Environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python your_script.py
    ```
   The script will start monitoring the clipboard for any file paths. When you copy a file path, the script will check whether it belongs to the root folder and apply the corresponding restrictions.

>> Usage

- Copy a file path from the root folder to see how the script restricts pasting it outside the root folder.
- Copy a file path from outside the root folder to verify that it can be pasted anywhere.

>> Example Output

When monitoring the clipboard, the script will display messages such as:

