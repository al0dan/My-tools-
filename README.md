```markdown
# CyberSec Tools Suite  

[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Issues](https://img.shields.io/github/issues/al0dan/CyberSecTools?style=for-the-badge)](https://github.com/al0dan/CyberSecTools/issues)
[![Stars](https://img.shields.io/github/stars/al0dan/CyberSecTools?style=for-the-badge)](https://github.com/al0dan/CyberSecTools/stargazers)

A suite of Python-based tools for cybersecurity enthusiasts and professionals, including DNS enumeration, recursive directory fuzzing, and an exploit for the **realest.lol** lab.

---

## Tools  

### 1. **DNS Enumeration Tool**  
Filename: `dns_enum.py`  
Description: Performs DNS enumeration by querying DNS records and fuzzing domain names to discover subdomains and other hidden records.

#### Features: 
- Supports A, MX, NS, TXT and CNAME records.
- Fuzzing with a custom wordlist is possible.

---

### 2. **Recursive Directory Fuzzing Tool** 
Filename: `dir_fuzzer.py` 
Description: This tool will recursively fuzz directories and files on a target web server in order to find "hidden" endpoints or other sensitive information.

#### Features: 
- Supports HTTP and HTTPS.
- Can be configured to perform recursive fuzzing at any depth.
- Can take a custom wordlist as input.

---

3. **Exploit for realest.lol**  Filenames: `realest_exploit.py`  Description: Exploits a Blind Code/Command Injection vulnerability in the **realest.lol** lab.

#### Features: 
- Interactive shell for blind command injection.
- Custom payload injection.
- Outputs results for local exploitation without OOB (Out-of-Band) communication.

---

## Usage 

1. Clone the repository:  
```bash
git clone https://github.com/al0dan/CyberSecTools.git
cd CyberSecTools
Install dependencies: 
   ```bash
   pip install -r requirements.txt
   ```

3. Use the desired tool: 
   ```bash
   python dns_enum.py
   python dir_fuzzer.py
   python realest_exploit.py
   ```

---

## Contributing 

Contributions are welcome! Feel free to fork the repository and create a pull request. We encourage that all code should be in Python best practices.

---

## License 

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
**Happy Hacking!**
```
