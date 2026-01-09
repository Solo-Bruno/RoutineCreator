from fpdf import FPDF
from fpdf.enums import XPos, YPos
import sys
import os


class RutinaPDF(FPDF):

    def __init__(self, nombre_rutina):
        super().__init__()
        self.nombre_rutina = nombre_rutina

    def resource_path(self,relative_path):
        """ Obtiene la ruta absoluta de los recursos para desarrollo y para .exe """
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def header(self):
        self.set_font('Helvetica', 'B', 16)

        self.cell(0, 18, self.nombre_rutina.upper(), align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def draw_exercise(self, x, y, exercise):
        w_card = 45
        img_h = 35

        self.set_xy(x, y)

        ruta_real = self.resource_path(exercise['exercise_img'])
        try:
            self.image(ruta_real, x=x, y=y, w=w_card, h=img_h)
        except Exception:
            self.rect(x, y, w_card, img_h)
            self.set_xy(x, y + (img_h / 2))
            self.set_font('Helvetica', 'I', 7)
            self.cell(w_card, 5, "Sin Imagen", align='C')

        self.set_xy(x, y + img_h + 2)
        self.set_font('Helvetica', 'B', 9)
        info_text = f"{exercise['series']}X{exercise['repeticiones']} ({exercise['peso']}kg)"
        self.cell(w_card, 5, info_text, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_x(x)
        self.set_font('Helvetica', '', 8)
        self.multi_cell(w_card, 4, exercise['exercise_name'].upper(), align='C')

