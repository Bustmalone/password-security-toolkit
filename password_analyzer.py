#!/usr/bin/env python3
"""
Password Security Toolkit
Comprehensive password security analysis
"""

import sys
import argparse
import hashlib
import math
from colorama import init, Fore, Style
from entropy_calculator import EntropyCalculator
from breach_checker import BreachChecker
from strength_checker import StrengthChecker

init()

class PasswordAnalyzer:
    def __init__(self):
        self.entropy_calc = EntropyCalculator()
        self.breach_checker = BreachChecker()
        self.strength_checker = StrengthChecker()
    
    def analyze(self, password, check_breach=False):
        """Analyze password security"""
        print(f"{Fore.CYAN}[*]{Style.RESET_ALL} Analyzing password...")
        
        # Calculate strength
        strength = self.strength_checker.check(password)
        
        # Calculate entropy
        entropy = self.entropy_calc.calculate(password)
        
        # Estimate time to crack
        time_to_crack = self._estimate_crack_time(entropy)
        
        # Display results
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Length: {len(password)} characters")
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Entropy: {entropy:.1f} bits")
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Strength: {strength['label']}")
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Time to crack: ~{time_to_crack}")
        
        # Display recommendations
        if strength.get('recommendations'):
            print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} Recommendations:")
            for rec in strength['recommendations']:
                print(f"    - {rec}")
        
        # Check breach database
        if check_breach:
            is_breached = self.breach_checker.check(password)
            if is_breached:
                print(f"{Fore.RED}[!]{Style.RESET_ALL} Password found in breach database!")
            else:
                print(f"{Fore.GREEN}[+]{Style.RESET_ALL} Password not found in breach database")
        
        return {
            'strength': strength,
            'entropy': entropy,
            'time_to_crack': time_to_crack
        }
    
    def _estimate_crack_time(self, entropy):
        """Estimate time to crack password"""
        # Assume 1 billion guesses per second
        guesses_per_second = 1e9
        total_guesses = 2 ** entropy
        
        seconds = total_guesses / guesses_per_second
        
        # Convert to readable format
        if seconds < 60:
            return f"{seconds:.0f} seconds"
        elif seconds < 3600:
            return f"{seconds/60:.1f} minutes"
        elif seconds < 86400:
            return f"{seconds/3600:.1f} hours"
        elif seconds < 31536000:
            return f"{seconds/86400:.1f} days"
        elif seconds < 31536000000:
            return f"{seconds/31536000:.1f} years"
        else:
            return f"{seconds/31536000:.0e} years"


def main():
    parser = argparse.ArgumentParser(description="Password Security Toolkit")
    parser.add_argument("--password", help="Password to analyze")
    parser.add_argument("--file", help="File containing passwords (one per line)")
    parser.add_argument("--check-breach", action="store_true", help="Check against breach database")
    
    args = parser.parse_args()
    
    if not args.password and not args.file:
        parser.print_help()
        sys.exit(1)
    
    try:
        analyzer = PasswordAnalyzer()
        
        if args.password:
            analyzer.analyze(args.password, check_breach=args.check_breach)
        
        elif args.file:
            with open(args.file, 'r') as f:
                for line in f:
                    password = line.strip()
                    if password:
                        print(f"\n{'='*50}")
                        analyzer.analyze(password, check_breach=args.check_breach)
    
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

