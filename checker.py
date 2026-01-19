import re
import getpass

def check_password(password):
    score = 0
    issues = []

    if len(password) >= 8:
        score += 1
    else:
        issues.append("Mot de passe trop court")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("Pas de majuscule")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("Pas de minuscule")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        issues.append("Pas de chiffre")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        issues.append("Pas de caractère spécial")

    return score, issues

password = getpass.getpass("Entrez votre mot de passe : ")
score, issues = check_password(password)

if score <= 2:
    level = "FAIBLE ❌"
elif score <= 4:
    level = "MOYEN ⚠️"
else:
    level = "FORT ✅"

print("\nRésultat :", level)
for issue in issues:
    print("-", issue)
