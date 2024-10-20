import csv


class DataExporter:
    """
    The DataExporter class handles exporting data to CSV files.
    """


    def export_to_csv(self, data_manager, filename, data_type):
        """
        Exports specified data to a CSV file.

        Parameters:
        - data_manager: An instance of the DataManager class that contains the data.
        - filename: The name of the file to which the data will be exported.
        - data_type: The type of data to export
        """
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
