import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk
import os
from model.cnn_model import build_cnn_model
from tensorflow.keras.models import load_model

# Import our modules (dummy placeholders here)
import prediction.predict as predict
import prediction.advice as advice

class FirstAidChatUI:
    def __init__(self, root):
        self.root = root
        self.root.title("First Aid Assistance System")
        self.root.geometry("600x700")
        self.root.configure(bg="white")

        self.model = build_cnn_model()
        self.model = load_model("first_aid_cnn_model.h5")

        # Chat area
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", bg="#f9f9f9", fg="black", font=("Arial", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Frame for entry + buttons
        bottom_frame = tk.Frame(root, bg="white")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.entry = tk.Entry(bottom_frame, font=("Arial", 12), width=40)
        self.entry.pack(side=tk.LEFT, padx=(0,10), pady=5, fill=tk.X, expand=True)
        self.entry.bind("<Return>", self.handle_text_input)

        self.send_btn = tk.Button(bottom_frame, text="Send", command=self.handle_text_input, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
        self.send_btn.pack(side=tk.LEFT)

        self.img_btn = tk.Button(bottom_frame, text="Upload Image", command=self.handle_image_upload, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
        self.img_btn.pack(side=tk.LEFT, padx=(10,0))

        # Welcome message
        self.add_message("System", "Hello! 👋 You can type your symptoms or upload an image of the injury for first aid advice.\n")

    def add_message(self, sender, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {message}\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)

    def handle_text_input(self, event=None):
        user_input = self.entry.get().strip()
        if not user_input:
            return
        self.add_message("You", user_input)
        self.entry.delete(0, tk.END)

        # Get prediction (RBS text-based)
        prediction, confidence = predict.predict_text(user_input)
        advice_text = advice.get_advice(prediction, confidence)

        self.add_message("  System", f"🩺 Detected: {prediction} (confidence: {confidence*100:.2f}%)")
        self.add_message("  System", f"💡 First Aid Advice: {advice_text} \n")

    def handle_image_upload(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if not file_path:
            return

        self.add_message("You", f"[Image uploaded: {os.path.basename(file_path)}]")

        # Load and show thumbnail image in chat
        img = Image.open(file_path)
        img.thumbnail((300,300))
        img_tk = ImageTk.PhotoImage(img)
        self.chat_area.image_create(tk.END, image=img_tk)
        self.chat_area.insert(tk.END, "\n")
        self.chat_area.image = img_tk  # Keep reference

        # Get prediction (CNN image-based)
        prediction, confidence = predict.predict_image(self.model, file_path)
        advice_text = advice.get_advice(prediction, confidence)

        self.add_message("System", f"🩺 Detected: {prediction} (confidence: {confidence*100:.2f}%)")
        self.add_message("System", f"💡 First Aid Advice: {advice_text}")


if __name__ == "__main__":
    root = tk.Tk()
    app = FirstAidChatUI(root)
    root.mainloop()
