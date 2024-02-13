from bing_image_downloader import downloader
import os
import tkinter as tk
from PIL import Image, ImageTk


def get_user_choice():
    choice = input("HELLO MY BEAUTIFUL WIFE WELCOME TO YOUR VALENTINES DAY GIFT! Please pick either C or P: ").lower()
    if choice == 'c':
        adj = input("Please enter an adjective for the cow (preferably a nice one): ")
    elif choice == 'p':
        adj = input("Please enter an adjective for the pig (preferably a nice one): ")
    else:
        print("Invalid choice. Please enter C or P.")
        return None, None
    return choice, adj


def fetch_images(query):
    downloader.download(query, limit=5, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60,
                        verbose=True)


def display_images(folder):
    # Create a Tkinter window
    root = tk.Tk()
    root.title("I LOVE YOU WITH ALL MY HEART ALWAYS AND FOREVER")

    # Get a list of all files in the folder
    files = os.listdir(folder)

    # Filter the list to include only image files (e.g., jpg, png)
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Loop through each image file and display it in the window
    for image_file in image_files:
        image_path = os.path.join(folder, image_file)
        image = Image.open(image_path)
        image = image.resize((200, 200))  # Resize the image to 200x200 pixels
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.pack()

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    choice, adj = get_user_choice()
    if choice and adj:
        query = adj + ('cow' if choice == 'c' else 'pig')
        fetch_images(query)
        display_images(os.path.join("dataset", query))
