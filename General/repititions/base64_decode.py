import base64

def decode_base64(encoded_str):
    try:
        decoded_str = base64.b64decode(encoded_str).decode('utf-8')
        return decoded_str
    except Exception as e:
        print(f"Error decoding: {e}")
        return None

def read_encoded_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    file_path = "/home/hoang/Downloads/enc_flag"
    encoded_text = read_encoded_text_from_file(file_path)

    if encoded_text is not None:
        while not encoded_text.startswith("pico"):
            decoded_text = decode_base64(encoded_text)
            if decoded_text is None:
                break  # Break the loop if decoding fails
            encoded_text = decoded_text

        print(f"Flag: {encoded_text}")

if __name__ == "__main__":
    main()
