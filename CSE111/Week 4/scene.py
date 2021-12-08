import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Draw sky
    canvas.create_rectangle(0, 0, 800, 600,
            fill="#699AE0")

    # Draw sun
    canvas.create_oval(500,200,700,400, fill="#FFDC00")

    # Draw Clouds
    canvas.create_oval(25, 125, 250, 50, fill="#FFFFFF")
    canvas.create_oval(600, 100, 300, 200, fill="#FFFFFF")
    canvas.create_oval(700, 50, 400, 150, fill="#FFFFFF")

    # Draw middle mountain in the background
    points = [100, 450, 100, 300, 300, 100, 500,
    250, 600, 300]
    canvas.create_polygon(points, outline='#000000',
    fill='#838383', width=1)

    # Draw the water on the right scene
    canvas.create_rectangle(0, 300, 800, 600,
            fill="#61D6EC")

    # Draw the ground on the right scene
    canvas.create_rectangle(0, 350, 800, 600,
            fill="#185C33")

    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    i = 0
    k = 0
    while i < 300:
        tree_center = scene_left + i
        tree_top = scene_top + k +160
        tree_height = 200
        draw_pine_tree(canvas, tree_center, tree_top, tree_height)
        i += 100
        k += 50

    i = 0
    k = 0
    while i < 300:
        tree_center = scene_left + i
        tree_top = scene_top + k +160
        tree_height = 250
        draw_pine_tree(canvas, tree_center, tree_top, tree_height)
        i += 70
        k += 50

    # i = 1
    # while i < 6:
    points = [200,600,500,100]
    canvas.create_polygon(points, fill='#FFFFFF')
        # i += 1


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

# def draw_background()

def draw_sky(canvas, peak_x,peak_y,height):
    canvas.create_rectangle(canvas, peak_x, peak_y, height,fill="blue1s")

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()