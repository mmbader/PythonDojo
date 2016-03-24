import re


def validateEmail(email):
    if re.match("^[a-z0-9._-]+@[a-z0-9.-]+\.[a-z]{2,}$", email, flags=re.IGNORECASE):
        return True
    return False

emaillist = list()
emaillist.append("cabarca@paypal.com")
emaillist.append("cabarca@paypal.com.co")
emaillist.append("carlos.abarca@paypal.com")
emaillist.append("carlos-abarca@paypal.com.co")
emaillist.append("carlos_abarca@paypal.com")
emaillist.append("CArlosAbarca@paypal.com")
emaillist.append("cabarca@paypal")
emaillist.append("@paypal.com")
emaillist.append("carlos.abarca paypal.com")
emaillist.append("carlos abarca@paypal.com")
emaillist.append(" @paypal.com.co")
emaillist.append("cabarca@paypal.c")

print ("%s\n%-30s | %9s\n%s" % ("="*42, "EMAIL ADDRESS", "IS VALID?", "="*42))

for email in emaillist:
    print ("%-30s | %9s" % (email, validateEmail(email)))
