#Task-8-4
class TV:
    def __init__(self, brand, price, inches):
        self.brand = brand
        self.channel = 1
        self.volume = 50
        self.price = price
        self.inches = inches
        self.on = False  # Initial is Off

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LED(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Viewing angle is 178 degrees"

    def backlight(self):
        return "LED backlight feature"

    def display_details(self):
        return (f"LED TV - Thickness: {self.screen_thickness} cm, "
                f"Energy Usage: {self.energy_usage} W, "
                f"Lifespan: {self.lifespan} hours, "
                f"Refresh Rate: {self.refresh_rate} Hz")


class Plasma(TV):
    def __init__(self, brand, price, inches, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, price, inches)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

    def viewing_angle(self):
        return "Viewing angle is 160 degrees"

    def backlight(self):
        return "Plasma technology does not use backlight"

    def display_details(self):
        return (f"Plasma TV - Thickness: {self.screen_thickness} cm, "
                f"Energy Usage: {self.energy_usage} W, "
                f"Lifespan: {self.lifespan} hours, "
                f"Refresh Rate: {self.refresh_rate} Hz")

