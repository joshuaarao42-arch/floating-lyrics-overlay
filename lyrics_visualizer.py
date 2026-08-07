import tkinter as tk
import random
import time
import threading

LYRICS = [
    ("Say you want the moon",              48.4),
    ("Watch me learn to fly",              51.5),
    ("Ain't no mountain you could point to", 53.7),
    ("I wouldn't climb",                    57.2),
    ("It's crazy, but it's true",           59.4),
    ("There's nothing I won't do",          62.2),
    ("I'd risk it ALLLLLLLL FOOOOOOOOORR YOUUUUUUUUUUU",    64.9),
]

BG_COLOR = "#0d0d0d"
TEXT_COLOR = "#111111"
BOX_BG = "#f5f5f5"
FONT = ("Helvetica Neue", 28, "bold")
TYPE_SPEED = 45          
WINDOW_LIFETIME = 4500   
FADE_SPEED = 25         
DRIFT_SPEED = 16         
DRIFT_AMOUNT = 0.4      

def spawn_lyric_window(root, text, x, y, delay):
    """Create a floating toplevel window with typewriter text effect."""

    def create():
        win = tk.Toplevel(root)
        win.overrideredirect(True)
        win.attributes("-topmost", True)
        win.attributes("-transparentcolor", BG_COLOR)
        win.configure(bg=BG_COLOR)

        # Estimate how many lines this text will wrap to at this font/width,
        # so the window can grow instead of clipping longer lyrics.
        approx_chars_per_line = 24  # rough fit for 28pt bold at wraplength 540
        num_lines = max(1, -(-len(text) // approx_chars_per_line))  # ceil div
        win_height = 80 + (num_lines * 40)  # 80px padding/base + 40px per line

        win.geometry(f"600x{win_height}+{x}+{y}")

        frame = tk.Frame(win, bg=BOX_BG, padx=30, pady=20)
        frame.pack(expand=True, fill="both")

        shadow = tk.Frame(win, bg="#222222")
        shadow.place(x=6, y=6, width=600, height=win_height)
        shadow.lower(frame)


        label = tk.Label(
            frame,
            text="",
            font=FONT,
            bg=BOX_BG,
            fg=TEXT_COLOR,
            justify="center",
            wraplength=540
        )
        label.pack(expand=True)

        char_index = [0]

        def type_next():
            if char_index[0] <= len(text):
                label.config(text=text[:char_index[0]])
                char_index[0] += 1
                win.after(TYPE_SPEED, type_next)
            else:
                # Start fade-out after lifetime
                win.after(WINDOW_LIFETIME, start_fade)

        # ─── Fade Out ───
        def start_fade():
            alpha = [1.0]
            def fade_step():
                alpha[0] -= 0.03
                if alpha[0] <= 0:
                    win.destroy()
                else:
                    win.attributes("-alpha", alpha[0])
                    win.after(FADE_SPEED, fade_step)
            fade_step()

        def drift():
            try:
                current_geo = win.geometry()
                # Parse "WxH+X+Y"
                parts = current_geo.split("+")
                curr_x = int(parts[1])
                curr_y = int(parts[2])
                win.geometry(f"600x{win_height}+{curr_x}+{curr_y - 1}")
                win.after(DRIFT_SPEED, drift)
            except:
                pass  

        win.after(100, drift)
        type_next()

    root.after(delay, create)


def main():
    root = tk.Tk()
    root.withdraw() 

    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()

    for line, start_seconds in LYRICS:
        x = random.randint(100, screen_w - 700)
        y = random.randint(150, screen_h - 250)

        delay_ms = int(start_seconds * 1000)
        spawn_lyric_window(root, line, x, y, delay_ms)

    last_text, last_start_seconds = LYRICS[-1]
    last_start = last_start_seconds * 1000
    type_duration = len(last_text) * TYPE_SPEED
    total_time = int(last_start + type_duration + WINDOW_LIFETIME + (FADE_SPEED * 34) + 500)
    root.after(total_time, root.destroy)

    root.mainloop()


if __name__ == "__main__":
    main()