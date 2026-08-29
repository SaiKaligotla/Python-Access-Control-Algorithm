# Define the file name and the list of IP addresses to remove
import_file = "allow_list.txt"
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# 1. Open the file that contains the allow list and read its contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# 2. Convert the string into a list
ip_addresses = ip_addresses.split()

# 3. Iterate through the remove list and remove targeted IP addresses
for element in remove_list:
    # Check if the IP address is currently in the allow list
    if element in ip_addresses:
        ip_addresses.remove(element)

# 4. Convert the revised list back into a string, separated by new lines
ip_addresses = "\n".join(ip_addresses)

# 5. Update the file with the revised list of IP addresses
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("Access control list updated successfully.")
