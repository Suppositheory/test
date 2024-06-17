### Írjone egy programot , ami egy új változóba másol egy karakterláncot úgy, hogy csillagot szúr be a karakterek közés 

def insert_asterisks():
    # Ask the user for input text
    text = input("Please enter your text: ")
    # Insert "*" between each character
    modified_text = '*'.join(text)
    # Return the modified text
    return modified_text

# Call the function
result = insert_asterisks()
print("Modified text:", result)