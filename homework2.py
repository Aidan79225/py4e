
class Record:
    def __init__(self, id: int, name: str, temperature: float, unit: str, date: str):
        self.id = id
        self.name = name
        self.temperature = temperature
        self.unit = unit
        self.date = date

import time

class Main:
    def __init__(self):
        self.records = []
        self.max_id = 0

    def read_file(self):
        file_name = input("Please enter filename: ")
        source = open(file_name)
        self.records.clear()
        for line in source:
            data = line.strip().split(',')
            self.records.append(Record(int(data[0]), data[1], float(data[2]), data[3], data[4]))
            self.max_id = max(int(data[0]), self.max_id)

    def print_datas(self, records: list):
        print("-------------Data-------------")
        print("id   | name	| temperature 	|   Unit	| date")
        for record in records:
            print(record.id, "  |   ", record.name, "   |   ", record.temperature, "    |  ", record.unit, "    |  ", record.date)
        print("------------------------------")

    def add_a_record(self):
        name = input("Please enter name: ")
        temperature = input("Please enter temperature: ")
        unit = input("Please enter unit: ")
        date = time.strftime("%Y/%m/%d")
        self.max_id += 1
        self.records.append(Record(self.max_id, name, float(temperature), unit, date))

    def remove_a_record(self):
        record_id = int(input("Please enter a id: "))
        record = None
        for r in self.records:
            if r.id == record_id:
                record = r
                break
        if record != None:
            self.records.remove(record)

    def save_file(self):
        file_name = input("Please enter filename: ")
        fp = open(file_name, "w")
        for r in self.records:
            fp.write("{},{},{},{},{}\n".format(r.id, r.name, r.temperature, r.unit, r.date))
        fp.close()
    
    def search_records_by_name(self):
        name = input("Please enter search key name: ")
        selected = []
        for r in self.records:
            if name in r.name:
                selected.append(r)
        self.print_datas(selected)

    def print_command(self):
        print("-----------Commands-----------")
        print("1. Read records from file")
        print("2. Add a record")
        print("3. Remove a record")
        print("4. Save records to a file")
        print("5. Search by name from records")
        print("6. Print all records")
        print("7. Exit")
        print("------------------------------")

    def exit(self):
        print("Have a nice day!")

    def start(self):
        while True:
            self.print_command()
            command = int(input("Please enter a command: "))
            
            if command == 1:
                self.read_file()
            elif command == 2:
                self.add_a_record()
            elif command == 3:
                self.remove_a_record()
            elif command == 4:
                self.save_file()
            elif command == 5:
                self.search_records_by_name()
            elif command == 6:
                self.print_datas(self.records)
            elif command == 7:
                self.exit()
                break

Main().start()