import tkinter as tk
from tkinter import filedialog, messagebox, ttk, Scale
import fitz  # PyMuPDF
from PIL import Image, ImageTk
import os

# Variáveis globais para a seleção do retângulo
x0, y0, x1, y1 = 0, 0, 0, 0
selection_made = False
rect_id = None
current_zoom_level = 1.0  # Variável global para armazenar o nível de zoom atual

class PDFViewer:
    def __init__(self, master, filepath):
        global x0, y0, x1, y1, selection_made, rect_id
        self.master = master
        self.filepath = filepath
        self.zoom_level = 1.0

        self.window = tk.Toplevel(master)
        self.window.title("Visualização do PDF")

        self.canvas = tk.Canvas(self.window, cursor="cross")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

        self.zoom_slider = Scale(self.window, from_=1, to=4, resolution=0.1, orient="horizontal", command=self.update_zoom)
        self.zoom_slider.pack()

        self.save_button = tk.Button(self.window, text="Salvar Seleção", command=self.save_selection)
        self.save_button.pack()

        self.load_pdf()

    def on_click(self, event):
        global x0, y0, selection_made, rect_id
        x0, y0 = event.x, event.y
        selection_made = False
        if rect_id:
            self.canvas.delete(rect_id)

    def on_drag(self, event):
        global rect_id
        if rect_id:
            self.canvas.delete(rect_id)
        rect_id = self.canvas.create_rectangle(x0, y0, event.x, event.y, outline='red')

    def on_release(self, event):
        global x1, y1, selection_made
        x1, y1 = event.x, event.y
        selection_made = True

    def load_pdf(self):
        self.doc = fitz.open(self.filepath)
        self.page = self.doc.load_page(0)  # Carrega a primeira página
        self.show_page()

    def show_page(self):
        pix = self.page.get_pixmap(matrix=fitz.Matrix(self.zoom_level, self.zoom_level))
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        self.canvas_img = ImageTk.PhotoImage(image=img)
        self.canvas.create_image(0, 0, image=self.canvas_img, anchor='nw')

    def update_zoom(self, val):
        global current_zoom_level
        self.zoom_level = float(val)
        current_zoom_level = self.zoom_level
        self.show_page()

    def save_selection(self):
        # Lógica para salvar a seleção
        self.window.destroy()

def open_pdf():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not filepath:
        return
    PDFViewer(root, filepath)

def extrair_texto_da_area_selecionada(pdf_file, zoom_level):
    global x0, y0, x1, y1, selection_made
    if not selection_made:
        messagebox.showwarning("Aviso", "Selecione uma área primeiro.")
        return None

    # Ajustando as coordenadas com base no zoom
    rect_x0 = x0 / zoom_level
    rect_y0 = y0 / zoom_level
    rect_x1 = x1 / zoom_level
    rect_y1 = y1 / zoom_level

    doc = fitz.open(pdf_file)
    page = doc.load_page(0)  # Carrega a primeira página
    rect = fitz.Rect(rect_x0, rect_y0, rect_x1, rect_y1)
    words = page.get_text("words")
    selected_text = ""
    for word in words:
        word_rect = fitz.Rect(word[:4])
        if word_rect.intersects(rect):
            selected_text += word[4] + " "
    doc.close()
    return selected_text.strip()

def renomear_arquivo(pdf_path, texto_extrai, pasta_destino):
    nome_arquivo = f"{texto_extrai}.pdf"
    novo_caminho = os.path.join(pasta_destino, nome_arquivo)
    contador = 1
    while os.path.exists(novo_caminho):
        nome_arquivo = f"{texto_extrai}_({contador}).pdf"
        novo_caminho = os.path.join(pasta_destino, nome_arquivo)
        contador += 1
    os.rename(pdf_path, novo_caminho)

def iniciar_processo(diretorio_origem, diretorio_destino):
    global current_zoom_level
    if not selection_made:
        messagebox.showwarning("Aviso", "Selecione uma área no PDF antes de iniciar.")
        return

    try:
        for arquivo in os.listdir(diretorio_origem):
            if arquivo.endswith(".pdf"):
                caminho_completo = os.path.join(diretorio_origem, arquivo)
                texto_extrai = extrair_texto_da_area_selecionada(caminho_completo, current_zoom_level)
                if texto_extrai:
                    renomear_arquivo(caminho_completo, texto_extrai, diretorio_destino)
        messagebox.showinfo("Concluído", "Processo concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

root = tk.Tk()
root.title("Renomear PDFs com Seleção de Área")

open_pdf_btn = tk.Button(root, text="Abrir PDF", command=open_pdf)
open_pdf_btn.pack(side="top", fill="x")

diretorio_origem = tk.StringVar()
diretorio_destino = tk.StringVar()

btn_diretorio_origem = ttk.Button(root, text="Selecionar Diretório Origem", command=lambda: diretorio_origem.set(filedialog.askdirectory(title="Selecione onde estão seus arquivos.")))
btn_diretorio_origem.pack(side="top", fill="x")

entry_diretorio_origem = ttk.Entry(root, textvariable=diretorio_origem, state='readonly')
entry_diretorio_origem.pack(side="top", fill="x")

btn_diretorio_destino = ttk.Button(root, text="Selecionar Diretório Destino", command=lambda: diretorio_destino.set(filedialog.askdirectory(title="Selecione onde quer salvar seus arquivos.")))
btn_diretorio_destino.pack(side="top", fill="x")

btn_iniciar = ttk.Button(root, text="Iniciar Renomeação", command=lambda: iniciar_processo(diretorio_origem.get(), diretorio_destino.get()))
btn_iniciar.pack(side="bottom", pady=5)

root.mainloop()
