import cairo
import math

def handle_task_two(width: int, height: int, path: str) -> None:
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(surface)

    # Set the background color to white
    context.set_source_rgb(1, 1, 1)
    context.paint()

    # Draw the black rectangle
    context.rectangle(200, 200, 400, 400)
    context.set_source_rgb(0.1, 0.1, 0.1)
    context.stroke()

    # Draw the red arc
    context.set_source_rgb(1, 0, 0)
    context.arc(200, 400, 200, 3 * math.pi / 2, math.pi / 2)
    context.stroke()

    # Draw the blue arc
    context.set_source_rgb(0, 0, 1)
    context.arc(600, 400, 200, math.pi / 2, 3 * math.pi / 2)
    context.stroke()

    # Save the image to a PNG file
    surface.write_to_png(f'{path}curves.png')

if __name__ == "__main__":
    # Specify the file path where the PNG file will be saved
    file_path = "output/"

    # Call the function to draw the shape and save it
    handle_task_two(800, 800, file_path)

    print(f"Image saved at: {file_path}curves.png")
