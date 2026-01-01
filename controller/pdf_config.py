from fpdf import FPDF

class PDFRutina(FPDF):
    def header(self):
        # Configurar fuente: Arial, Negrita, 15
        self.set_font("Arial", "B", 15)
        # Título centrado
        self.cell(0, 10, "MI RUTINA PERSONALIZADA", border=False, ln=True, align="C")
        self.ln(5) # Salto de línea

    def footer(self):
        self.set_y(-15) # 1.5 cm desde el final
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Página {self.page_no()}", align="C")
