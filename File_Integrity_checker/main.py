import hashlib

filename = "important_file.txt"

with open(filename, "rb") as file:
    current_data = file.read()

current_hash = hashlib.sha256(current_data).hexdigest()

with open("original_hash.txt", "r") as file:
    original_hash = file.read()

print("===== FILE INTEGRITY CHECKER =====\n")

print("Original Hash:")
print(original_hash)

print("\nCurrent Hash:")
print(current_hash)

if original_hash == current_hash:
    print("\nFile Integrity Maintained")
else:
    print("\nWARNING!")
    print("File Has Been Modified")