# Password Security Toolkit

A comprehensive password security analysis suite including strength checker, common password detection, and breach database lookup. Implements entropy calculation, time-to-crack estimation, and security recommendations. Educational tool for promoting password security best practices.

## Features

- **Strength Analysis** - Calculate password strength and entropy
- **Breach Checking** - Check passwords against Have I Been Pwned database
- **Entropy Calculation** - Calculate password entropy in bits
- **Security Recommendations** - Provide actionable security advice
- **Time-to-Crack Estimation** - Estimate time to crack passwords
- **Common Password Detection** - Check against common password lists

## Requirements

- Python 3.8+

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Analyze Password Strength
```bash
python password_analyzer.py --password "YourPassword123!"
```

### Check Password Against Breach Database
```bash
python password_analyzer.py --password "test" --check-breach
```

### Analyze Password File
```bash
python password_analyzer.py --file passwords.txt
```

## Example Output

```
[*] Analyzing password...
[+] Length: 16 characters
[+] Entropy: 85.2 bits
[+] Strength: Very Strong
[+] Time to crack: ~10^15 years
[!] Recommendations:
    - Password is strong
    - Consider using a password manager
```

## Project Structure

```
password-security-toolkit/
├── password_analyzer.py    # Main analysis script
├── entropy_calculator.py    # Entropy calculation
├── breach_checker.py        # Breach database checking
├── strength_checker.py     # Strength analysis
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── common_passwords.txt    # Common password list
```

## Security Notice

⚠️ **This tool analyzes passwords. Never analyze actual passwords in production. Use only for educational purposes or with test passwords.**

## License

MIT License

## Author

John Bustamante - Cybersecurity Professional

