class Event:
    expression = ""
    message = ""
    
    def __init__(self, expression, message, bad_message = ""):
        self.expression = expression
        self.message = message
        self.bad_message = bad_message
    
    def evaluate(self, reading):
        temperature = reading.temperature
        humidity = reading.humidity
        if not eval(self.expression):
            return self.format(self.bad_message, reading)
        return self.format(self.message, reading)

    def format(self, text, reading):
        text = text.replace("%r", f"{reading}")
        text = text.replace("%t", f"{reading.temperature:.2f}")
        return text.replace("%h", f"{reading.humidity:.2f}")
