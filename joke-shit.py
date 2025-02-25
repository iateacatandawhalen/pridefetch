class PrideFlagPrinter:
    @staticmethod
    def rgb_to_hex(r, g, b):
        """Convert RGB to HEX format."""
        return f"#{r:02x}{g:02x}{b:02x}".upper()

    # Pride flag color definitions
    GAY_FLAG_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130)]
    RAINBOW_FLAG_COLORS = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (139, 0, 255)]
    BISEXUAL_FLAG_COLORS = [(206, 0, 122), (0, 56, 168), (222, 119, 255)]
    PANSEXUAL_FLAG_COLORS = [(255, 20, 147), (255, 223, 0), (0, 132, 255)]
    TRANSGENDER_FLAG_COLORS = [(55, 160, 255), (255, 217, 255), (255, 255, 255), (255, 217, 255), (55, 160, 255)]
    FINSEXUAL_FLAG_COLORS = [(241, 167, 193), (0, 168, 255), (240, 160, 160), (240, 240, 240), (255, 215, 0)]
    FEMBOY_FLAG_COLORS = [(255, 102, 255), (255, 153, 255), (255, 255, 255), (102, 153, 255), (102, 102, 255)]
    NONBINARY_FLAG_COLORS = [(255, 244, 48), (255, 255, 255), (156, 89, 209), (0, 0, 0)]
    AESTHETIC_FLAG_COLORS = [(138, 43, 226), (255, 99, 71), (255, 215, 0), (173, 216, 230), (60, 179, 113)]
    WEEBSEXUAL_FLAG_COLORS = [(255, 182, 193), (255, 20, 147), (230, 230, 250), (147, 112, 219), (75, 0, 130)]

    # NEW FLAGS
    GENDERFLUX_FLAG_COLORS = [
        (255, 182, 193),  # Pink
        (255, 105, 180),  # Hot Pink
        (255, 255, 255),  # White
        (173, 216, 230),  # Light Blue
        (0, 0, 0)         # Black
    ]

    SAPPHIC_FLAG_COLORS = [
        (255, 175, 201),  # Soft Pink
        (255, 203, 217),  # Light Pink
        (255, 255, 255),  # White
        (255, 203, 217),  # Light Pink
        (255, 175, 201)   # Soft Pink
    ]

    ANTI_TRANS_EXEC_ORDER_FLAG_COLORS = [
        (55, 160, 255),  # Transgender Flag colors as base
        (255, 217, 255),
        (255, 255, 255),
        (255, 217, 255),
        (55, 160, 255)
    ]

    @staticmethod
    def print_flag(flag_colors, flag_name, slogans=[]):
        """Prints the pride flag using ANSI escape codes for color and adds anti-DOGE slogans."""
        print(f"{flag_name} Flag:")
        for line, rgb in enumerate(flag_colors, start=1):
            hex_color = PrideFlagPrinter.rgb_to_hex(*rgb)
            print(f"\033[48;2;{rgb[0]};{rgb[1]};{rgb[2]}m{' ' * 30}\033[0m {hex_color}")
        
        # Adding slogans
        for slogan in slogans:
            print(f"\033[38;2;255;0;0m{slogan}\033[0m")

    # Functions to print each flag
    @staticmethod
    def print_rainbow_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.RAINBOW_FLAG_COLORS, "Rainbow", slogans=["DOGE is a joke."])

    @staticmethod
    def print_gay_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.GAY_FLAG_COLORS, "Gay", slogans=["DOGE is outdated."])

    @staticmethod
    def print_bisexual_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.BISEXUAL_FLAG_COLORS, "Bisexual", slogans=["DOGE for bureaucratic inefficiency."])

    @staticmethod
    def print_pansexual_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.PANSEXUAL_FLAG_COLORS, "Pansexual", slogans=["DOGE, the government’s mascot."])

    @staticmethod
    def print_trans_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.TRANSGENDER_FLAG_COLORS, "Transgender", slogans=["End the DOGE madness."])

    @staticmethod
    def print_finsexual_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.FINSEXUAL_FLAG_COLORS, "Finsexual", slogans=["The DOGE government is inefficient."])

    @staticmethod
    def print_femboy_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.FEMBOY_FLAG_COLORS, "Femboy", slogans=["DOGE: wasted potential."])

    @staticmethod
    def print_nonbinary_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.NONBINARY_FLAG_COLORS, "Nonbinary", slogans=["DOGE is nothing more than a meme."])

    @staticmethod
    def print_aesthetic_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.AESTHETIC_FLAG_COLORS, "Aesthetic", slogans=["DOGE needs to be put out to pasture."])

    @staticmethod
    def print_weebsexual_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.WEEBSEXUAL_FLAG_COLORS, "Weebsexual", slogans=["DOGE isn't even funny anymore."])

    @staticmethod
    def print_genderflux_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.GENDERFLUX_FLAG_COLORS, "Genderflux", slogans=["DOGE is a scam."])

    @staticmethod
    def print_sapphic_flag():
        PrideFlagPrinter.print_flag(PrideFlagPrinter.SAPPHIC_FLAG_COLORS, "Sapphic", slogans=["DOGE has been exposed."])

    @staticmethod
    def print_anti_trans_exec_order_flag():
        slogans = [
            "Trans Rights are Human Rights!",
            "Not a Dictator, Just a Meme!",
            "Transphobia is a Joke. So Is DOGE!",
            "Stop the Executive Order, Start Supporting Trans People!",
            "Trump is an executive joke; his orders are worse."
        ]
        PrideFlagPrinter.print_flag(PrideFlagPrinter.ANTI_TRANS_EXEC_ORDER_FLAG_COLORS, "Anti Anti-Trans Executive Order", slogans)

# Now print all the flags with the anti-DOGE slogans
pride_flag_printer = PrideFlagPrinter()
pride_flag_printer.print_rainbow_flag()
pride_flag_printer.print_gay_flag()
pride_flag_printer.print_bisexual_flag()
pride_flag_printer.print_pansexual_flag()
pride_flag_printer.print_trans_flag()
pride_flag_printer.print_finsexual_flag()
pride_flag_printer.print_femboy_flag()
pride_flag_printer.print_nonbinary_flag()
pride_flag_printer.print_aesthetic_flag()
pride_flag_printer.print_weebsexual_flag()
pride_flag_printer.print_genderflux_flag()
pride_flag_printer.print_sapphic_flag()
pride_flag_printer.print_anti_trans_exec_order_flag()  # Here is the new flag mocking the executive order
