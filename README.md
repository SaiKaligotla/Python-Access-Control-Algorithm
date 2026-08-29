# 🛡️ Python Algorithm for Automating Access Control via IP Address Filtering

## 📝 Project Description
In this project, I acted as a security professional working at a healthcare company tasked with managing access to restricted personal patient records[cite: 11]. Access to this sensitive network is controlled by an allow list of approved IP addresses[cite: 11]. To ensure security compliance, I developed a Python algorithm to automate the process of cross-referencing an active allow list against a dynamically updated remove list, automatically revoking access for specific employees and updating the file[cite: 11]. 

---

## 💻 Python Algorithm Execution Steps

### 1. Open the file that contains the allow list
To begin parsing the data, the external text file containing the approved IP addresses must be opened[cite: 11]. 

```python
import_file = "allow_list.txt"

with open(import_file, "r") as file:
```
**Explanation:** 
I assigned the target file name to a string variable called `import_file`[cite: 11]. I then utilized a `with` statement alongside the `open()` function to open the file in read mode ("r")[cite: 11]. Using the `with` statement is best practice because it automatically handles resource management and closes the file when the block of code finishes execution.

### 2. Read the file contents
The contents of the file need to be extracted into a usable format within the Python script[cite: 11].

```python
    ip_addresses = file.read()
```
**Explanation:** 
Inside the `with` statement, I used the `.read()` method to convert the raw contents of the allow list file into a single text string[cite: 11]. This string is then assigned to the variable `ip_addresses` so it can be manipulated in subsequent steps[cite: 11]. 

### 3. Convert the string into a list
To easily isolate and remove individual IP addresses, the data must be transformed from a single, continuous string into an iterable data structure[cite: 11]. 

```python
ip_addresses = ip_addresses.split()
```
**Explanation:** 
I applied the `.split()` method to the `ip_addresses` string[cite: 11]. By default, this method separates the string at every whitespace, converting the IP addresses into individual elements stored inside a Python list[cite: 11].

### 4. Iterate through the remove list
A separate list named `remove_list` contains the specific IP addresses that need their network access revoked[cite: 11]. 

```python
for element in remove_list:
```
**Explanation:** 
To process the revocation, I set up the header of a `for` loop[cite: 11]. This loop iterates through the `remove_list`, processing one IP address at a time using `element` as the designated loop variable[cite: 11]. 

### 5. Remove IP addresses that are on the remove list
During the iteration, the algorithm must verify if the targeted IP address exists in the approved list before attempting to remove it[cite: 11].

```python
    if element in ip_addresses:
        ip_addresses.remove(element)
```
**Explanation:** 
Within the body of the `for` loop, I created a conditional `if` statement to evaluate if the loop variable (`element`) is actively present within the `ip_addresses` list[cite: 11]. If the condition evaluates to True, the `.remove()` method is applied to delete the IP address from the allow list[cite: 11]. Applying the `.remove()` method in this way is possible because there are no duplicate IP addresses in the `ip_addresses` list[cite: 11].

### 6. Update the file with the revised list of IP addresses
Once the revoked IP addresses have been successfully scrubbed from the list, the external file must be updated to reflect the new security posture[cite: 11].

```python
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)
```
**Explanation:** 
First, I used the `.join()` method to convert the `ip_addresses` list back into a string, appending a newline character (`"\n"`) to ensure each IP address is placed on a separate line in the text file[cite: 11]. Finally, I used another `with` statement to open the file in write mode ("w") and utilized the `.write()` method to overwrite the original file with the secure, revised list of authorized IP addresses[cite: 11].

---

## 🔒 Summary & Business Impact
This Python algorithm successfully automates the management of network access control lists within a highly regulated healthcare environment[cite: 11]. By leveraging Python's file handling functions (`with open()`, `.read()`, and `.write()`) and string manipulation methods (`.split()` and `.join()`), the script seamlessly extracts and formats critical security data[cite: 11]. Furthermore, by utilizing iterative logic (`for` loops) and conditional statements (`if`), the algorithm accurately cross-references an active allow list against a dynamically changing remove list to revoke access securely[cite: 11]. This automation ensures that restricted patient records are safeguarded and reduces the risk of human error during manual access control audits.
