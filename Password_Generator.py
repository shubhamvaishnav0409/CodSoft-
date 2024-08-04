
import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols):
  """Generates a password based on the given criteria."""

  characters = []
  if include_lowercase:
    characters += string.ascii_lowercase
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_digits:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  if not characters:
    return "Please select at least one character type."

  password = ''.join(random.choice(characters) for i in range(length))
  return password

def main():
  """Prompts the user for password criteria and prints the generated password."""

  length = int(input("Enter desired password length: "))
  include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
  include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
  include_digits = input("Include digits? (y/n): ").lower() == 'y'
  include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

  password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)
  print("Generated password:", password)

if __name__ == "__main__":
  main()