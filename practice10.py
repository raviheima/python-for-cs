import re

def check_password_strength(password):
    """
    Check password strength based on multiple criteria
    Returns a score and detailed feedback
    """
    score = 0
    feedback = []
    
    # Check 1: Length (minimum 8 characters)
    if len(password) >= 8:
        score += 2
        feedback.append("✓ Good length (8+ characters)")
    elif len(password) >= 6:
        score += 1
        feedback.append("⚠ Acceptable length, but 8+ is better")
    else:
        feedback.append("✗ Too short (less than 6 characters)")
    
    # Check 2: Contains lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")
    
    # Check 3: Contains uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")
    
    # Check 4: Contains numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")
    
    # Check 5: Contains special characters
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")
    
    # Check 6: No common patterns
    common_patterns = ['123', 'abc', 'password', 'qwerty', '111', 'aaa']
    has_common = any(pattern in password.lower() for pattern in common_patterns)
    if not has_common:
        score += 1
        feedback.append("✓ No common patterns detected")
    else:
        feedback.append("✗ Contains common patterns (avoid 123, abc, etc.)")
    
    # Check 7: Bonus for extra length
    if len(password) >= 12:
        score += 1
        feedback.append("✓ Bonus: Extra long password!")
    
    return score, feedback

def get_strength_level(score):
    """Convert score to strength level"""
    if score >= 7:
        return "VERY STRONG", "🟢"
    elif score >= 5:
        return "STRONG", "🟡"
    elif score >= 3:
        return "MODERATE", "🟠"
    elif score >= 1:
        return "WEAK", "🔴"
    else:
        return "VERY WEAK", "⚫"

def main():
    """Main function to run the password checker"""
    print("=== PASSWORD STRENGTH CHECKER ===")
    print("Enter a password to check its strength:")
    print("(Press Enter with empty input to quit)")
    print()
    
    while True:
        password = input("Password: ").strip()
        
        if not password:
            print("Goodbye!")
            break
        
        # Check password strength
        score, feedback = check_password_strength(password)
        strength, emoji = get_strength_level(score)
        
        # Display results
        print(f"\n--- RESULTS ---")
        print(f"Password: {'*' * len(password)}")  # Hide actual password
        print(f"Score: {score}/8")
        print(f"Strength: {strength} {emoji}")
        print()
        
        print("Detailed feedback:")
        for item in feedback:
            print(f"  {item}")
        
        print("\n" + "="*50 + "\n")

# Example function to test different passwords
def test_passwords():
    """Test the checker with sample passwords"""
    test_cases = [
        "123",
        "password",
        "Password1",
        "MyP@ssw0rd!",
        "SuperSecure123!@#"
    ]
    
    print("=== TESTING SAMPLE PASSWORDS ===\n")
    
    for pwd in test_cases:
        score, feedback = check_password_strength(pwd)
        strength, emoji = get_strength_level(score)
        
        print(f"Password: {pwd}")
        print(f"Strength: {strength} {emoji} (Score: {score}/8)")
        print("Top feedback:")
        for item in feedback[:3]:  # Show first 3 items
            print(f"  {item}")
        print()

if __name__ == "__main__":
    # Uncomment the line below to see test examples first
    # test_passwords()
    
    # Run the interactive checker
    main()