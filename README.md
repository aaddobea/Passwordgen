# Passwordgen
This script presents a UI interface of a Password generator in python.

> DESCRIPTIVE FUNCTIONS
> 
**1. Password Length Control:**  Add a slider to let users choose the password length.

**2. Provide checkboxes**  to allow users to include/exclude letters, numbers, and symbols.

**3. Improved UI:** Organize widgets more neatly using frames and padding.

**4. Password Strength Indicator:** Add a color indicator for password strength.

**5. Copy to Clipboard Button:** Allow users to copy the generated password to the clipboard.

# Explanation 
+ Character Type Selection: Checkboxes for letters, numbers, and symbols let users customize the types of characters included in the password.
  
+ Password Length Control: A slider allows users to choose the password length between 8 and 32 characters.
  
+ Copy to Clipboard: The copy_to_clipboard method uses pyperclip to copy the generated password to the clipboard, making it easy to paste elsewhere.
  
+ Error Handling: Message boxes inform users if they haven't selected any character types or if there’s no password to copy.
  
## How to run the script
python password_generator.py
    
## To run this, you’ll need to install pyperclip:
> `pip install pyperclip`

## Screenshot of the sample use of the script

![Alt text](https://github.com/aaddobea/Passwordgen/blob/main/window.png)


## Author Name
***Addobea Akosua Abigail***
