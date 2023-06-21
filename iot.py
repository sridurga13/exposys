morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def encrypt_to_morse(text):
    encrypted_message = ""
    for char in text:
        if char.upper() in morse_code:
            encrypted_message += morse_code[char.upper()] + " "
    return encrypted_message.strip()

# Example usage
plaintext = input("Enter the text to encrypt: ")
encrypted_text = encrypt_to_morse(plaintext)
print("Encrypted message:", encrypted_text)

import time
# Function to control the flashlight
def flash_light(duration):
    print("Flashlight ON")
    time.sleep(duration)
    print("Flashlight OFF")

# Function to convert text to Morse code and blink the flashlight
def morse_to_flashlight(text):
    for char in text:
        if char.upper() in morse_code:
            code = morse_code[char.upper()]
            for symbol in code:
                if symbol == ".":
                    flash_light(0.2)  # Flash the flashlight for a short duration for a dot
                elif symbol == "-":
                    flash_light(0.5)  # Flash the flashlight for a longer duration for a dash
                else:
                    time.sleep(0.2)  # Pause between letters
            time.sleep(0.5)  # Pause between words

# Example usage
plaintext = input("Enter the text to convert to Morse code and blink the flashlight: ")
morse_to_flashlight(plaintext)

import time
import keyboard
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


# Function to record the flash pattern
def record_flash_pattern():
    flash_pattern = []
    prev_time = time.time()
    while True:
        current_time = time.time()
        if current_time - prev_time >= 0.2:  # Minimum time threshold to detect a flash
            flash_duration = current_time - prev_time
            flash_pattern.append(flash_duration)
            prev_time = current_time
        if keyboard.is_pressed('esc'):  # Press 'Esc' to stop recording
            break
    return flash_pattern

# Function to convert flash pattern to Morse code
def flash_pattern_to_morse(flash_pattern):
    morse_code_pattern = ''
    for flash_duration in flash_pattern:
        if flash_duration < 0.3:  # Assuming flashes shorter than 0.3 seconds are dots
            morse_code_pattern += '.'
        else:  # Flashes equal to or longer than 0.3 seconds are dashes
            morse_code_pattern += '-'
    return morse_code_pattern

# Function to decrypt Morse code to text
def decrypt_morse(morse_code_pattern):
    decrypted_message = ''
    symbols = morse_code_pattern.split(' ')
    for symbol in symbols:
        if symbol in morse_code:
            decrypted_message += morse_code[symbol]
    return decrypted_messageSR

# Example usage
print("Recording flash pattern...")
flash_pattern = record_flash_pattern()
print("Flash pattern recorded:", flash_pattern)

morse_code_pattern = flash_pattern_to_morse(flash_pattern)
print("Morse code pattern:", morse_code_pattern)

decrypted_message = decrypt


