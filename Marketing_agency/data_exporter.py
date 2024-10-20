import csv

class DataExporter:
    def export_to_csv(self, data_manager, filename, data_type):
        data = []
        if data_type == "employees":
            data = data_manager.employees
        elif data_type == "clients":
            data = data_manager.clients
        elif data_type == "products":
            data = data_manager.products
        elif data_type == "sales":
            data = data_manager.sales
        if not data:
            print("No data to export.")
            return

        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"{data_type.capitalize()} data exported to {filename}.")
