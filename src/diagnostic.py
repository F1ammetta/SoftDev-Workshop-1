class DiagnosticImages:
    def __init__(self):
        self.images = []

    def add(self, image):
        self.images.append(image)

    def remove(self, image):
        self.images.remove(image)

    def __str__(self):
        str = ''
        for image in self.images:
            str += f'{image}\n'
        return str
