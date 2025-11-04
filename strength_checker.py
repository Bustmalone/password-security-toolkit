"""
Strength Checker
Analyzes password strength and provides recommendations
"""

import re
import string


class StrengthChecker:
    def __init__(self):
        self.common_passwords = self._load_common_passwords()
    
    def _load_common_passwords(self):
        """Load common passwords list"""
        common = [
            'password', '123456', '123456789', '12345678', '12345',
            'qwerty', 'abc123', 'password1', 'welcome', 'monkey'
        ]
        return common
    
    def check(self, password):
        """Check password strength"""
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use at least 8 characters")
        
        if len(password) >= 12:
            score += 1
        
        # Character variety
        if re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if re.search(r'[A-Z]', password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if re.search(r'[0-9]', password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if re.search(r'[^a-zA-Z0-9]', password):
            score += 1
        else:
            feedback.append("Add special characters")
        
        # Check for common patterns
        if password.lower() in [p.lower() for p in self.common_passwords]:
            score = max(0, score - 2)
            feedback.append("Avoid common passwords")
        
        # Check for sequential patterns
        if re.search(r'(abc|123|qwe)', password.lower()):
            score = max(0, score - 1)
            feedback.append("Avoid sequential patterns")
        
        # Determine strength label
        if score <= 2:
            label = "Very Weak"
        elif score <= 3:
            label = "Weak"
        elif score <= 4:
            label = "Fair"
        elif score <= 5:
            label = "Good"
        elif score <= 6:
            label = "Strong"
        else:
            label = "Very Strong"
        
        return {
            'score': score,
            'label': label,
            'recommendations': feedback if feedback else ["Password is strong!"]
        }

