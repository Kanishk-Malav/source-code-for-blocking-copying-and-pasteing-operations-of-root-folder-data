import os
import win32clipboard as clipboard
import time

# Define the root folder
ROOT_FOLDER = r"C:\root"

def get_clipboard_content():
    """
    Retrieves the current content of the clipboard.
    """
    clipboard.OpenClipboard()
    try:
        # Get clipboard data as Unicode text
        data = clipboard.GetClipboardData()
    except Exception as e:
        data = None  # Handle cases with no valid clipboard data
    clipboard.CloseClipboard()
    return data

def is_path_in_root(path):
    """
    Check if the given path is inside the root folder.
    """
    try:
        # Ensure the path is absolute and normalize for comparison
        absolute_path = os.path.abspath(path)
        return os.path.commonpath([absolute_path, ROOT_FOLDER]) == ROOT_FOLDER
    except Exception as e:
        return False  # Handle invalid paths gracefully

def monitor_clipboard():
    """
    Monitor the clipboard and validate paths for copy-paste operations.
    """
    previous_content = None
    print("Monitoring clipboard for file paths... (Press Ctrl+C to stop)")
    
    while True:
        current_content = get_clipboard_content()
        if current_content != previous_content:
            print(f"Clipboard updated: {current_content}")
            previous_content = current_content  # Update the last seen content
            
            # Check if clipboard content is a valid path
            if os.path.exists(current_content):
                if is_path_in_root(current_content):
                    print(f"Valid path: {current_content} (Inside root)")
                else:
                    print(f"Blocked path: {current_content} (Outside root)")
            else:
                print(f"Clipboard does not contain a valid file path: {current_content}")
        time.sleep(1)  # Poll every second
import pyperclip

# Copy a valid file path to the clipboard
def copy_file_path_to_clipboard(path):
    pyperclip.copy(path)
    print(f"Copied to clipboard: {path}")

# Example usage (copying a valid path to the clipboard)
copy_file_path_to_clipboard(r"C:\Users\User\Desktop\java open source\your_script.py")


if __name__ == "__main__":
    monitor_clipboard()
