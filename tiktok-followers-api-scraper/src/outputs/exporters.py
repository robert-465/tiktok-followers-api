thonimport json

class Exporter:
    def __init__(self, data):
        self.data = data

    def export_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=4)