import os
import shutil


FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


class FileOrganizer:
    def __init__(self, path):
        self.path = path
        self.moved_files_count = 0

    def is_valid_path(self):
        return os.path.exists(self.path)

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.path, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        return folder_path

    def get_category(self, extension):
        for category, extensions in FILE_TYPES.items():
            if extension.lower() in extensions:
                return category
        return "Others"

    def organize_files(self):
        try:
            for file in os.listdir(self.path):
                file_path = os.path.join(self.path, file)

                if os.path.isfile(file_path):
                    _, ext = os.path.splitext(file)
                    category = self.get_category(ext)

                    dest_folder = self.create_folder(category)
                    dest_path = os.path.join(dest_folder, file)

                    # Handle duplicate names
                    if os.path.exists(dest_path):
                        base, extension = os.path.splitext(file)
                        counter = 1
                        while os.path.exists(dest_path):
                            new_name = f"{base}_{counter}{extension}"
                            dest_path = os.path.join(dest_folder, new_name)
                            counter += 1

                    shutil.move(file_path, dest_path)
                    self.moved_files_count += 1

            print(f"✅ Organization complete! {self.moved_files_count} files moved.")

        except Exception as e:
            print("❌ Error occurred:", e)


if __name__ == "__main__":
    folder_path = input("Enter folder path to organize: ")

    organizer = FileOrganizer(folder_path)

    if organizer.is_valid_path():
        organizer.organize_files()
    else:
        print("❌ Invalid folder path.")
