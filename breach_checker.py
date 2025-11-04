"""
Breach Checker
Checks passwords against Have I Been Pwned database
"""

import hashlib
import requests


class BreachChecker:
    def __init__(self):
        self.api_url = "https://api.pwnedpasswords.com/range/"
    
    def check(self, password):
        """Check if password is in breach database"""
        # Hash password with SHA-1
        sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        
        try:
            response = requests.get(f"{self.api_url}{prefix}", timeout=5)
            response.raise_for_status()
            
            # Check if suffix is in response
            hashes = response.text.split('\n')
            for hash_line in hashes:
                if hash_line.startswith(suffix):
                    return True
            
            return False
        
        except requests.exceptions.RequestException:
            # If API is unavailable, return False (assume not breached)
            return False

