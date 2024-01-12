import os

from reportlab.pdfgen import canvas


class PDFConfigs:
    PDF_PAGE_WIDTH = 3000
    PDF_PAGE_HEIGHT = 1800

    SENSOR_DATA_POS_X = 0
    SENSOR_DATA_POS_Y = 600

    TANK_DATA_POS_X = 0
    TANK_DATA_POS_Y = 1200

    MAX_HEIGHT_POS_X = 0
    MAX_HEIGHT_POS_Y = 1200

    AVERAGE_VELOCITY_POS_X = 0
    AVERAGE_VELOCITY_POS_Y = 600

    PARALLEL_VELOCITY_SUM_POS_X = 0
    PARALLEL_VELOCITY_SUM_POS_Y = 0


def convert_png_to_pdf(png_file):
    pdf_format = png_file.split(".")
    pdf_format[-1] = "pdf"
    save_file = ".".join(pdf_format)

    pdf = canvas.Canvas(f"pdfs/{save_file}")
    a4_width, a4_height = PDFConfigs.PDF_PAGE_WIDTH, PDFConfigs.PDF_PAGE_HEIGHT

    pdf.setPageSize((a4_width, a4_height))
    pdf.drawImage(
        f"results/max_height/{png_file}",
        PDFConfigs.MAX_HEIGHT_POS_X,
        PDFConfigs.MAX_HEIGHT_POS_Y,
    )
    pdf.drawImage(
        f"results/average_velocity/{png_file}",
        PDFConfigs.AVERAGE_VELOCITY_POS_X,
        PDFConfigs.AVERAGE_VELOCITY_POS_Y,
    )  # noqa
    pdf.drawImage(
        f"results/parallel_velocity_sum/{png_file}",
        PDFConfigs.PARALLEL_VELOCITY_SUM_POS_X,
        PDFConfigs.PARALLEL_VELOCITY_SUM_POS_Y,
    )  # noqa

    pdf.showPage()

    pdf.drawImage(
        f"results/{png_file}",
        PDFConfigs.SENSOR_DATA_POS_X,
        PDFConfigs.SENSOR_DATA_POS_Y,
    )
    pdf.drawImage(
        f"results/tank_data/{png_file}",
        PDFConfigs.TANK_DATA_POS_X,
        PDFConfigs.TANK_DATA_POS_Y,
    )
    pdf.save()


if __name__ == "__main__":
    image_files = os.listdir("results/max_height")

    for image_file in image_files:
        convert_png_to_pdf(image_file)
