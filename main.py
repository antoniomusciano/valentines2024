from bing_image_downloader import downloader
import os
import tkinter as tk
from PIL import Image, ImageTk


def fetch_images(query):
    downloader.download(query, limit=5, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60,
                        verbose=True)


def display_images(folder):
    pass


if __name__ == "__main__":
    choice = input("Enter c or p: ")  # cow or pig
    if choice == 'c':
        choice = 'cow'
        adj = input("Please enter an adjective (preferably a nice one): ")

    if choice == 'p':
        choice = 'pig'
        adj = input("Please enter an adjective (preferably a nice one): ")

    fetch_images(adj + choice)
    display_images("dataset/" + adj + choice)
