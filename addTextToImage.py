from PIL import Image
from PIL import ImageDraw, ImageFont
import time

def generateImg(text, position, salary, workingTime, template="default"):
    class TextWrapper(object):
        """ Helper class to wrap text in lines, based on given text, font
            and max allowed line width.
        """

        def __init__(self, text, font, max_width):
            self.text = text
            self.text_lines = [
                ' '.join([w.strip() for w in l.split(' ') if w])
                for l in text.split('\n')
                if l
            ]
            self.font = font
            self.max_width = max_width

            self.draw = ImageDraw.Draw(
                Image.new(
                    mode='RGB',
                    size=(100, 100)
                )
            )

            self.space_width = self.draw.textsize(
                text=' ',
                font=self.font
            )[0]

        def get_text_width(self, text):
            return self.draw.textsize(
                text=text,
                font=self.font
            )[0]

        def wrapped_text(self):
            wrapped_lines = []
            buf = []
            buf_width = 0

            for line in self.text_lines:
                for word in line.split(' '):
                    word_width = self.get_text_width(word)

                    expected_width = word_width if not buf else \
                        buf_width + self.space_width + word_width

                    if expected_width <= self.max_width:
                        # word fits in line
                        buf_width = expected_width
                        buf.append(word)
                    else:
                        # word doesn't fit in line
                        wrapped_lines.append(' '.join(buf))
                        buf = [word]
                        buf_width = word_width

                if buf:
                    wrapped_lines.append(' '.join(buf))
                    buf = []
                    buf_width = 0

            return '\n'.join(wrapped_lines)

    # Open an Image

    img = Image.open(
        './templates/default.png') if template == "default" else Image.open("./templates/" + template)

    # Set colros
    black = (0, 0, 0)
    teal = (0, 89, 89)
    blackTeal = (0, 37, 37)

    # Set font and style
    bold = ImageFont.truetype(font='./fonts/monserrat_font.ttf', size=36)
    bold.set_variation_by_name('Bold')
    regular = ImageFont.truetype(font='./fonts/monserrat_font.ttf', size=24)
    regular.set_variation_by_name('Regular')
    h2 = ImageFont.truetype(font='./fonts/monserrat_font.ttf', size=28)
    h2.set_variation_by_name('Bold')
    p = ImageFont.truetype(font='./fonts/monserrat_font.ttf', size=21)
    p.set_variation_by_name('Bold')

    # Call draw Method to add 2D graphics in an image
    draw = ImageDraw.Draw(img)

    wrapper = TextWrapper(text, bold, 700)
    text = wrapper.wrapped_text()

    draw.text((73, 300), "OFERTA DE EMPLEO", font=bold, fill=teal)
    draw.text((73, 350), text=position, font=h2, fill=black)
    draw.multiline_text((73, 395), align="left",
                        text=text, font=regular, fill=blackTeal)
    draw.text((73, 580), "Salario: " + salary + " - Tiempo: " + workingTime,
              font=p, fill=black, align="left")

    # Display edited image
    img.show()

    # Save the edited image
    fileName = "./outputs/digest_" + str(time.time()) + ".png"
    img.save(fileName)

    return fileName

# # Add Text to an image
# text = """Estamos buscando algasdasf sadfuien como túd con ca  pacidad de análisis y dedicación a la causa Rusa en el conflicto contra Ucrania. Esperamos que todo mejore!s otra cosa aquí para agregar un par"""
# position = "Auxiliar de Enfermería"
# salary = "450000"
# workingTime = "Completo"

# generateImg(text=text, position=position, salary=salary,
#             workingTime=workingTime)
