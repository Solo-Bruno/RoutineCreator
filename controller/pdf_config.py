from fpdf import FPDF
from fpdf.enums import XPos, YPos


class RutinaPDF(FPDF):

    def __init__(self, nombre_rutina):
        super().__init__()
        self.nombre_rutina = nombre_rutina

    def header(self):
        self.set_font('Helvetica', 'B', 16)
        self.set_fill_color(0, 0, 0)
        self.set_text_color(255, 255, 255)


        self.cell(0, 18, self.nombre_rutina.upper(), align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_text_color(0, 0, 0)
        self.ln(2)

    def draw_exercise(self, x, y, exercise):
        w_card = 45
        img_h = 35
        # Dibujar Imagen
        try:
            self.image(exercise['exercise_img'], x=x, y=y, w=w_card, h=img_h)
        except:
            self.rect(x, y, w_card, img_h)  # Recuadro si no hay imagen
            self.set_xy(x, y + (img_h / 2))
            self.set_font('Helvetica', 'I', 7)
            self.cell(w_card, 5, "Sin Imagen", align='C')

        # Datos del ejercicio
        self.set_xy(x, y + img_h + 2)
        self.set_font('Helvetica', 'B', 9)
        info_text = f"{exercise['series']}X{exercise['repeticiones']} ({exercise['peso']}kg)"
        self.cell(w_card, 5, info_text, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Nombre del ejercicio
        self.set_x(x)
        self.set_font('Helvetica', '', 8)
        self.multi_cell(w_card, 4, exercise['exercise_name'].upper(), align='C')