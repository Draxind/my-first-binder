from PIL import Image
import matplotlib.pyplot as plt

R = 0   # red, green, blue indices in a pixel
G = 1
B = 2

# the 16 standard web colours

WHITE = (255, 255, 255)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
YELLOW = (255, 255, 0)
OLIVE = (128, 128, 0)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
ACQUA = (0, 255, 255)
TEAL = (0, 128, 128)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)

def load_image(filename: str) -> list:
    """Load the given file and return the image as a pixel grid.

    Preconditions: The file name has extension .bmp, .png, .jpg, or .jpeg
    Postconditions:
    The pixel grid is a list of columns, each a list of pixels.
    Each column has the same length.
    Each pixel is a tuple of three integers from 0 to 255 (inclusive),
    representing the red-green-blue components of the pixel.
    """
    image = Image.open(filename)
    pixels = []
    for row in range(image.height):
        row_pixels = []
        for column in range(image.width):
            pixel = image.getpixel((column, row))
            if image.mode == 'RGBA':
                pixel = (pixel[R], pixel[G], pixel[B])
            elif image.mode == 'L':
                pixel = (pixel,) * 3
            elif image.mode == '1':
                pixel = (255 * pixel,) * 3
            elif image.mode != 'RGB':
                raise ValueError('image is not in RGB format')
            row_pixels.append(pixel)
        pixels.append(row_pixels)
    return pixels

def new_image(width: int, height: int, pixel: tuple) -> list:
    """Return a monochromatic rectangle as a pixel grid.

    Preconditions:
    - width and height are positive
    - pixel is an RGB triple: three integers from 0 to 255 (inclusive)
    Postconditions:
    The pixel grid is a list of `width` columns.
    Each column is a list of `height` copies of `pixel`.
    """
    pixels = []
    for row in range(height):
        pixels.append([pixel] * width)
    return pixels

def width(image: list) -> int:
    """Return how many columns of pixels the image has.

    Preconditions: the image is a pixel grid (see load_image)
    """
    return len(image[0])

def height(image: list) -> int:
    """Return how many rows of pixels the image has.

    Preconditions: the image is a pixel grid (see load_image)
    """
    return len(image)

def show_image(image: list) -> None:
    """Show the image in the notebook, resized to not be too large or small.

    Preconditions: the image is a pixel grid (see load_image)
    """
    plt.axis('off')
    plt.imshow(image)

def save_image(image: list, filename: str) -> None:
    """Save the image to the given file.

    Preconditions:
    - the image is a pixel grid (see load_image)
    - the file name has extension .bmp, .png, .jpg, or .jpeg
    - if the file already exists, it's overwritten
    """
    img = Image.new('RGB', (width(image), height(image)))
    for column in range(width(image)):
        for row in range(height(image)):
            # print(row, column)
            img.putpixel((column, row), image[row][column])
    img.save(filename)
