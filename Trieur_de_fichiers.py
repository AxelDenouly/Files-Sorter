import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


# Crée une classe appelée FileOrganizerApp qui gère l'application
class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Trieur de fichiers")  # Définit le titre de la fenêtre principale
        self.root.geometry("600x400")  # Redimensionnez la fenêtre si nécessaire

        # Chargez l'image que vous souhaitez utiliser en tant que background
        bg_image = Image.open(
            "C:/Users/aghat/Desktop/Python_WallPaper.jpeg")  # Remplacez par le chemin de votre image
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Créez une étiquette pour afficher l'image en arrière-plan
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(relwidth=1, relheight=1)

        # Crée une étiquette (label) pour afficher un message de bienvenue
        self.label = tk.Label(root, text="Bienvenue dans l'organisateur de fichiers", bg='black', fg='white',
                              font=("Helvetica", 16))
        self.label.pack(pady=20)  # Affiche l'étiquette dans la fenêtre

        # Crée un bouton pour parcourir et sélectionner un dossier
        self.browse_button = tk.Button(root, text="Parcourir Dossiers", bg='black', fg='white',
                                       command=self.browse_folder, bd=5, highlightbackground='white')
        self.browse_button.pack()  # Affiche le bouton dans la fenêtre

        # Crée un bouton pour lancer le tri des fichiers
        self.organize_button = tk.Button(root, text="Trier les fichiers", bg='black', fg='white', state=tk.DISABLED,
                                         command=self.organize_files, bd=5, highlightbackground='white')
        self.organize_button.pack(pady=10)  # Affiche le bouton dans la fenêtre

        self.folder_path = ""  # Chemin du dossier sélectionné

        self.signature_label = tk.Label(root, text="made by Axel Denouly", bg='black', fg='white', font=("Georgia", 7, "italic"))
        self.signature_label.pack(side=tk.BOTTOM, anchor=tk.W, padx=10, pady=10)  # Affiche l'étiquette en bas avec un peu d'espace

    # Méthode appelée lorsque le bouton de parcours est cliqué
    def browse_folder(self):
        self.folder_path = filedialog.askdirectory()  # Ouvre une boîte de dialogue pour choisir un dossier
        if self.folder_path:
            self.organize_button.config(state=tk.NORMAL)  # Active le bouton "Trier les fichiers"
            messagebox.showinfo("Sélection du dossier", "Dossier sélectionné : " + self.folder_path)

    # Méthode pour trier les fichiers dans des dossiers en fonction de leurs extensions
    def organize_files(self):
        if not self.folder_path:
            messagebox.showerror("Erreur", "Sélectionnez d'abord un dossier!")
            return

        files = os.listdir(self.folder_path)  # Liste tous les fichiers dans le dossier sélectionné
        for file in files:
            if os.path.isfile(os.path.join(self.folder_path, file)):  # Vérifie si c'est un fichier
                file_extension = file.split('.')[-1]  # Obtient l'extension du fichier
                target_folder = self.get_target_folder(
                    file_extension)  # Obtient le dossier cible en fonction de l'extension
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)  # Crée le dossier cible s'il n'existe pas
                shutil.move(os.path.join(self.folder_path, file),
                            os.path.join(target_folder, file))  # Déplace le fichier vers le dossier cible

        messagebox.showinfo("Terminé", "Le tri des fichiers est terminé!")

    # Méthode pour obtenir le dossier cible en fonction de l'extension du fichier
    def get_target_folder(self, file_extension):
        predefined_folders = {
            'txt': 'Fichiers Texte',
            'png': 'Images',
            'jpg': 'Images',
            'gif': 'Images',
            'bmp': 'Images',
            'svg': 'Images',
            'tif': 'Images',
            'jpeg': 'Images',
            'pdf': 'PDFs',
            'mp3': 'Music',
            'wav': 'Music',
            'flac': 'Music',
            'aac': 'Music',
            'ogg': 'Music',
            'wma': 'Music',
            'mp4': 'Videos',
            'mkv': 'Videos',
            'mov': 'Videos',
            'wmv': 'Videos',
            'flv': 'Videos',
            'mpeg': 'Videos',
            'webm': 'Videos',
            'avi': 'Videos',
            'html': 'Web Front-End',
            'css': 'Web Front-End',
            'py': 'Fichiers python',
        }

        if file_extension in predefined_folders:
            return os.path.join(self.folder_path, predefined_folders[file_extension])
        else:
            divers_folder = os.path.join(self.folder_path, 'Fichiers divers')
            if not os.path.exists(divers_folder):
                os.makedirs(divers_folder)
            return divers_folder


# Point d'entrée du programme
if __name__ == "__main__":
    root = tk.Tk()  # Crée une fenêtre Tkinter
    root.geometry("600x200")
    root.config(bg="black")
    app = FileOrganizerApp(root)  # Crée une instance de la classe FileOrganizerApp
    root.mainloop()  # Lance la boucle principale de l'interface graphique
