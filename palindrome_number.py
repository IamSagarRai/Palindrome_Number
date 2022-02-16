n = int(input("Enter any number: "))
temporary = n
reverse_n = 0

while(n>0):
    digit = n % 10
    reverse_n = reverse_n * 10 + digit
    n = n // 10

if (temporary == reverse_n):
    print("It is a Palindrome number")
else:
    print("It is not a Palindrome number")
