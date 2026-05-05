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
            return self.format(self.bad_message, temperature, humidity)
        return self.format(self.message, temperature, humidity)

    def format(self, text, temperature, humidity):
        text = text.replace("%t", f"{temperature:.2f}")
        return text.replace("%h", f"{humidity:.2f}")
