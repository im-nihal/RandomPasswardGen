import random

uppr_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = uppr_letters.lower()
spec_chars = """~!@#$%^&*()_+"'-=}{[]:;?><,./"""
digits = "0123456789"

allChar = ""  #putting all data into it.

#To include any of the characters = True & for excluding = False.
upper, lower, nums, symbols = True, True, True, True

if upper: allChar += uppr_letters
if lower: allChar += lower_letters
if nums: allChar += digits
if symbols: allChar += spec_chars

Length = int(input("Enter The Legth Of Passwrod: "))
amount = 5 #prints the random password 5 times.
for i in range(amount):
    psk = "".join(random.sample(allChar, Length))
    print(psk)