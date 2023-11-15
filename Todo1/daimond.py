import cairo
import math

def draw_playing_card(output_path, width, height, corner_radius, symbol):
    # Create a Cairo surface
    surface = cairo.ImageSurface(cairo.Format.RGB24, 600, 600)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(0.8,0.8,0.8)
    ctx.paint()

    # Set line width and color (black)
    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 0, 0)

    # Draw the rounded rectangle
    ctx.arc(width - corner_radius, corner_radius, corner_radius, -0.5 * math.pi, 0)
    ctx.arc(width - corner_radius, height - corner_radius, corner_radius, 0, 0.5 * math.pi)
    ctx.arc(corner_radius, height - corner_radius, corner_radius, 0.5 * math.pi, math.pi)
    ctx.arc(corner_radius, corner_radius, corner_radius, math.pi, 1.5 * math.pi)
    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()
    ctx.close_path()

    # Fill the rectangle
    ctx.fill_preserve()

    # Stroke the outline
    ctx.stroke()

    # Draw the symbol (letter 'A' for Ace in this case)
    ctx.set_source_rgb(1, 0, 0)  # Red color for the symbol
    ctx.set_font_size(40)
    ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    text_extents = ctx.text_extents(symbol)
    x = (width - text_extents.width) / 2
    y = (height + text_extents.height) / 2
    ctx.move_to(x, y)
    ctx.show_text(symbol)

    # Save the PNG file
    surface.write_to_png(output_path)

if __name__ == "__main__":
    output_path = "daimond.png"
    width = 200
    height = 300
    corner_radius = 20
    symbol = "A"

    draw_playing_card(output_path, width, height, corner_radius, symbol)
