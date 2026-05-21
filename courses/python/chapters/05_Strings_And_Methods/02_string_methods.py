"""
String Methods
===============
Run: python3 02_string_methods.py

Covers:
- Case methods: upper(), lower(), title(), capitalize()
- Search methods: find(), index(), count(), startswith(), endswith()
- Modify methods: replace(), strip(), lstrip(), rstrip()
- Split and join: split(), join()
- Check methods: isalpha(), isdigit(), isalnum(), isspace()
- Alignment: center(), ljust(), rjust(), zfill()
"""


# =============================================================================
# CASE METHODS
# =============================================================================

print("=" * 55)
print("  CASE METHODS")
print("=" * 55)

text = "hello, World! python IS great"
print(f"\n  text = '{text}'")
print(f"\n  .upper()      = '{text.upper()}'")
print(f"  .lower()      = '{text.lower()}'")
print(f"  .title()      = '{text.title()}'")
print(f"  .capitalize() = '{text.capitalize()}'")

# =============================================================================
# SEARCH METHODS
# =============================================================================

print(f"\n{'=' * 55}")
print("  SEARCH METHODS")
print("=" * 55)

text = "Python is awesome and Python is powerful"
print(f"\n  text = '{text}'")

# find() returns index, -1 if not found
print(f"\n  .find('Python')     = {text.find('Python')}")      # 0
print(f"  .find('Python', 1)  = {text.find('Python', 1)}")    # 22 (search from index 1)
print(f"  .find('Java')       = {text.find('Java')}")          # -1

# count() returns number of occurrences
print(f"\n  .count('Python')    = {text.count('Python')}")     # 2
print(f"  .count('is')        = {text.count('is')}")           # 2

# startswith() and endswith()
print(f"\n  .startswith('Python') = {text.startswith('Python')}")  # True
print(f"  .endswith('powerful') = {text.endswith('powerful')}")    # True
print(f"  .endswith('awesome')  = {text.endswith('awesome')}")     # False


# =============================================================================
# MODIFY METHODS
# =============================================================================

print(f"\n{'=' * 55}")
print("  MODIFY METHODS")
print("=" * 55)

# replace()
text = "I love Java and Java is fun"
print(f"\n  text = '{text}'")
print(f"  .replace('Java', 'Python') = '{text.replace('Java', 'Python')}'")
print(f"  .replace('Java', 'Python', 1) = '{text.replace('Java', 'Python', 1)}'")

# strip() — removes whitespace (or specified chars)
text = "   Hello, World!   "
print(f"\n  text = '{text}'")
print(f"  .strip()  = '{text.strip()}'")
print(f"  .lstrip() = '{text.lstrip()}'")
print(f"  .rstrip() = '{text.rstrip()}'")

# Strip specific characters
url = "///path/to/file///"
print(f"\n  url = '{url}'")
print(f"  .strip('/') = '{url.strip('/')}'") # strips '/' from both ends


# =============================================================================
# SPLIT AND JOIN
# =============================================================================

print(f"\n{'=' * 55}")
print("  SPLIT AND JOIN")
print("=" * 55)

# split() — breaks string into a list
sentence = "Python is a great language"
words = sentence.split()
print(f"\n  '{sentence}'.split()")
print(f"  = {words}")

csv_data = "name,age,city"
fields = csv_data.split(",")
print(f"\n  '{csv_data}'.split(',')")
print(f"  = {fields}")

# split with maxsplit
text = "one-two-three-four-five"
print(f"\n  '{text}'.split('-', 2)")
print(f"  = {text.split('-', 2)}")   # Split only first 2

# splitlines() - splits by line breaks
multi = "Line 1\nLine 2\nLine 3"
print(multi.splitlines())  # ['Line 1', 'Line 2', 'Line 3']

#Get file extension
filename = "report.pdf"
name, ext = filename.rsplit(".", 1)   # Split from right, max 1
print(f"\n  '{filename}'.rsplit('.', 1)")
print(f"  = filename: '{name}', ext: '{ext}'")

# join() — combines a list into a string
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(f"\n  ' '.join({words})")
print(f"  = '{joined}'")

path_parts = ["home", "user", "documents"]
path = "/".join(path_parts)
print(f"\n  '/'.join({path_parts})")
print(f"  = '{path}'")


# =============================================================================
# CHECK METHODS (return True/False)
# =============================================================================

print(f"\n{'=' * 55}")
print("  CHECK METHODS")
print("=" * 55)

print(f"\n  'hello'.isalpha()  = {'hello'.isalpha()}")    # True (all letters)
print(f"  'hello1'.isalpha() = {'hello1'.isalpha()}")     # False
print(f"  '12345'.isdigit()  = {'12345'.isdigit()}")      # True (all digits)
print(f"  '123.4'.isdigit()  = {'123.4'.isdigit()}")      # False (dot isn't digit)
print(f"  'abc123'.isalnum() = {'abc123'.isalnum()}")     # True (letters + digits)
print(f"  '   '.isspace()    = {'   '.isspace()}")         # True (all whitespace)
print(f"  'Hello'.isupper()  = {'Hello'.isupper()}")      # False
print(f"  'HELLO'.isupper()  = {'HELLO'.isupper()}")      # True
print(f"  'hello'.islower()  = {'hello'.islower()}")      # True
# ASCII checks: It checks whether all characters in the string are ASCII characters (Unicode code points 0–127).
'''
ASCII mainly represents standard English characters and basic computer symbols.
A-Z
a-z
0-9
basic symbols: @ # $ % & *
control characters: \n, \t, \r
'''
print(f"  'hello'.isascii()   = {'hello'.isascii()}")      # True
print(f"  '123'.isascii()     = {'123'.isascii()}")        # True
print(f"  'αβγ'.isascii()     = {'αβγ'.isascii()}")        # False
print(f"  '😀'.isascii()      = {'😀'.isascii()}")         # False


# =============================================================================
# ALIGNMENT METHODS
# =============================================================================

print(f"\n{'=' * 55}")
print("  ALIGNMENT METHODS")
print("=" * 55)

text = "Python"
print(f"\n  text = '{text}'")
print(f"  .center(20, '-') = '{text.center(20, '-')}'")
print(f"  .ljust(20, '.')  = '{text.ljust(20, '.')}'")
print(f"  .rjust(20, '.')  = '{text.rjust(20, '.')}'")

# zfill — pad with zeros (useful for IDs, timestamps)
num = "42"
print(f"\n  '42'.zfill(5) = '{num.zfill(5)}'")   # '00042'

print(f"\n{'=' * 55}")
