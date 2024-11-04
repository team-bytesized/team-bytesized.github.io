import base64
import io
import zipfile

with open("base64by32.zip", "rb") as file:
    data = file.read()

# Unzipping the decoded data in memory
with zipfile.ZipFile(io.BytesIO(data)) as zip_file:
    with zip_file.open("base64by32") as base64_file:  # Open the file inside the zip
        b64_data = base64_file.read()
for i in range(32):
    b64_data = base64.b64decode(b64_data)
print(b64_data.decode())
