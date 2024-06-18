```python
from nas_file_access.client import NASFileAccess

base_url = "<BaseURL>"
username = "<YourUserName>"
password = "<YourPassword>"
folder_path = "<Folderpath>"
filename = "<Filename>"

nas_client = NASFileAccess(base_url, username, password)
count = nas_client.count_file(folder_path, filename)
print(f"Number of {filename} files: {count}")
nas_client.logout()

```
