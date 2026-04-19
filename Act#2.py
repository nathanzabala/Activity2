try:
    first_entry = input("Enter a short note/message: ")
    with open("notes.txt", "w") as note_file:
        note_file.write(first_entry + "\n")
    print("\nSaved successfully!")
except Exception as err:
    print("Write error:", err)

try:
    with open("notes.txt", "r") as reader:
        stored_text = reader.read()
    print("\n--- File Content ---")
    print(stored_text)
except FileNotFoundError:
    print("File not found.")

try:
    extra_entry = input("\nEnter another note: ")
    with open("notes.txt", "a") as append_file:
        append_file.write(extra_entry + "\n")
    print("\nAppended successfully!")

    with open("notes.txt", "r") as final_reader:
        final_text = final_reader.read()
    print("\n--- Updated File Content ---")
    print(final_text)
except Exception as err:
    print("Append error:", err)