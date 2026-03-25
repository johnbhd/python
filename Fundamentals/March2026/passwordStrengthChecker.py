def validation_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_num = any(c.isdigit() for c in password)
    
    if has_upper:
        score += 1
    
    if has_lower:
        score += 1

    if has_num:
        score += 1

    return score

def check_password(password): 
    validatepass = validation_password(password)
    response = ["Weak", "Moderate", "Strong"]
    text = ""

    if validatepass == 4:
        text = response[2]
    elif validatepass == 3:
        text = response[1]
    else: 
        text = response[0]

    return text

password = "Jbpogi123"
checkPassword = check_password(password)
print(checkPassword)