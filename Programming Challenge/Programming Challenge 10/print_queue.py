def ValidateUserID(ThisUserID):
    prefix = "2015_"
    if len(ThisUserID) != 9:
        return 1
    elif ThisUserID[:5] != prefix:
        return 2
    else:
        return 0


class PrintJob:
    def __init__(self, user_id, terminal_number, file_size):
        self.__user_id = user_id
        self.__terminal_number = terminal_number
        self.__file_size = file_size

    def get_user_id(self):
        return self.__user_id

    def get_terminal_number(self):
        return self.__terminal_number

    def get_file_size(self):
        return self.__file_size

    def set_user_id(self, new_user_id):
        self.__user_id = new_user_id

    def set_terminal_number(self, new_terminal_number):
        self.__terminal_number = new_terminal_number

    def set_file_size(self, new_file_size):
        self.__file_size = new_file_size


class PrintQueue:
    def __init__(self, max_size=5):
        self.__front = 0
        self.__rear = 0
        self.__max_size = max_size
        self.__print_queue = [
            PrintJob(None, None, None) for i in range(self.__max_size)
        ]

    def size(self):
        if self.__rear >= self.__front:
            qSize = self.__rear - self.__front
        else:
            qSize = self.__max_size - (self.__front - self.__rear)
        # return the size of the queue
        return qSize

    def add_print_job(self, print_job):
        if self.size() == self.__max_size - 1:
            print("Queue is Full!")
            return False
        self.__print_queue[self.__rear] = print_job
        self.__rear = (self.__rear + 1) % self.__max_size
        return True

    def output_print_job(self):
        if self.size() == 0:

            return "Print Queue is empty!"
        else:
            print_job = self.__print_queue[self.__front]
            self.__front = (self.__front + 1) % self.__max_size
            return print_job

    def display_print_job(self):
        if self.size() == 0:
            print("Queue is empty!", end="\n\n")
            return False
        else:
            print(
                "                  |{0:^25}|{1:^20}|{2:^20}|".format(
                    "USER ID", "TERMINAL NUMBER", "FILE SIZE"
                )
            )

            print("")
            print(
                "Current queue is: |{0:^25}|{1:^20}|{2:^20}|".format(
                    str(self.__print_queue[self.__front].get_user_id()),
                    str(self.__print_queue[self.__front].get_terminal_number()),
                    str(self.__print_queue[self.__front].get_file_size()),
                )
            )
            print()


def display_menu():
    print("1. New print job added to print queue")
    print("2. Next print job output from printer")
    print("3. Current print queue displayed")
    print("4. End")
    print("\n")


def main():
    Room16 = PrintQueue()
    while True:
        display_menu()
        user_choice = input("Enter a choice: ")

        if user_choice == "1":
            while True:
                print("----------Add a print queue----------", end="\n\n")
                user_id_choice = input("Enter your user ID: ")
                terminal_number_choice = input("Enter your terminal number(1-172): ")
                file_size_choice = input("Enter your file size: ")
                print()
                if ValidateUserID(user_id_choice) == 0:
                    Room16.add_print_job(
                        PrintJob(
                            user_id_choice, terminal_number_choice, file_size_choice
                        )
                    )
                    print("*-----Print Job added-----*", end="\n\n\n")
                    break
                else:
                    print("Please enter the correct user ID", end="\n\n")
                    continue
        elif user_choice == "2":
            print()
            print(
                "You have removed the print job from the print queue: {0}".format(
                    Room16.output_print_job()
                )
            )
            print()

        elif user_choice == "3":
            print("\n\n")
            Room16.display_print_job()

        elif user_choice == "4":
            break
        else:
            print("\n\n")
            print("Please enter a valid option")
            continue


main()
