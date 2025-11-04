"""
Entropy Calculator
Calculates password entropy in bits
"""

import math
import string


class EntropyCalculator:
    def calculate(self, password):
        """Calculate password entropy"""
        if not password:
            return 0
        
        # Determine character set size
        char_set_size = 0
        
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digits = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        if has_lower:
            char_set_size += 26
        if has_upper:
            char_set_size += 26
        if has_digits:
            char_set_size += 10
        if has_special:
            char_set_size += len(string.punctuation)
        
        # Calculate entropy
        entropy = len(password) * math.log2(char_set_size)
        
        return entropy

