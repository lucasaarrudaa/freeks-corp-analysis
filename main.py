import src.current_data
import src.forecast_data
import sys

print("*******************************************************************************************")
print("You are in the data analysis environment of the digital marketing department of Freeks Corp")
print("*******************************************************************************************")

while True:
    choice = int(input("Do you want to analyze current data or forecast for the next month?\
                         \nCURRENT DATA[1]  FORECAST[2]  EXIT[3]\n"))

    while choice == 1 or choice == 2:
        if choice == 1:
            src.current_data.show()
        elif choice == 2:
            src.forecast_data.show()
        option = input(
            "Do you still want to analyze the data?\nOptions: [Y] Yes [N] No\n").lower()

        while option != "y" and option != "n":
            option = input(
                "Invalid option. Please enter 'Y' to continue or 'N' to exit.\n").lower()

        if option == "n":
            print("Thank you for using the program. See you next time!")
            sys.exit(0)

        while True:
            choice = int(input("Do you want to analyze current data or forecast for the next month?\
                                \nCURRENT DATA[1]  FORECAST[2]  EXIT[3]\n"))
            if choice == 1 or choice == 2 or choice == 3:
                choice = int(choice)
                break
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
    if choice == 3:
        print("Thank you for using the program. See you next time!")
        sys.exit(0)

    print("Invalid option. Please enter '1', '2', or '3'.\n")
