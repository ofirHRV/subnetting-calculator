# printing IP address and prefix length
def show_address(decimal_ip, decimal_subnet_mask, prefix_length, binary_ip, binary_subnet_mask):
    print(f"\nDecimal IP: \t\t\t{decimal_ip}")
    print(f"Decimal subnet mask: \t{decimal_subnet_mask}")
    print(f"Prefix Length: \t\t\t/{prefix_length}")
    print()
    print(f"Binary IP: \t\t\t\t{binary_ip}")
    print(f"Binary Subnet Mask: \t{binary_subnet_mask}")
    print()


# Function to convert decimal IP address to binary
def decimal_to_binary(ip_address):
    # Split the IP address into four octets
    octets = ip_address.split('.')

    # Initialize an empty list to store binary octets
    binary_octets = []

    # Convert each octet to binary and append it to the list
    for octet in octets:
        binary_octet = bin(int(octet))[2:].zfill(8)  # Convert to binary and pad with zeros
        binary_octets.append(binary_octet)

    # Join the binary octets with dots to form the binary IP address
    binary_ip_address = '.'.join(binary_octets)

    return binary_ip_address


# Function to convert prefix length to decimal subnet mask
def prefix_length_to_decimal(prefix_length):
    # Ensure prefix_length is an integer
    prefix_length = int(prefix_length)

    # Create a binary string with '1's for the prefix length followed by '0's
    binary_string = '1' * prefix_length + '0' * (32 - prefix_length)

    # Split the binary string into four octets
    octets = [binary_string[i:i + 8] for i in range(0, 32, 8)]

    # Convert each octet to decimal and join them with dots
    decimal_subnet_mask = '.'.join([str(int(octet, 2)) for octet in octets])

    return decimal_subnet_mask


# calculations of the user for finding the net ID and broadcast
def calculations():
    while True:
        # Get user input for a binary number
        binary_number = input("Enter a binary number to calculate (or 'q' to exit and enter the results): ")

        # Check if the user wants to quit
        if binary_number.lower() == 'q':
            print("Exiting...")
            break

        try:
            # Convert the binary number to decimal
            decimal_number = int(binary_number, 2)

            # Display the result
            print(f"Binary Number: \t\t\t{binary_number}")
            print(f"Decimal Number: \t\t{decimal_number}")
        except ValueError:
            print("Invalid input. Please enter a valid binary number or 'q' to quit.")


def calculate_network_id(ip_address, prefix_length):
    # Split the IP address into octets
    octets = ip_address.split('.')

    # Convert the octets to integers
    ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

    # Calculate the network address
    network_int = ip_int & ((2 ** prefix_length - 1) << (32 - prefix_length))

    # Convert the network address back to octets
    network_octets = [(network_int >> 24) & 0xFF,
                      (network_int >> 16) & 0xFF,
                      (network_int >> 8) & 0xFF,
                      network_int & 0xFF]

    # Join octets to form the network address
    network_address = '.'.join(map(str, network_octets))

    return network_address


def calculate_broadcast_address(ip_address, prefix_length):
    # Split the IP address into octets
    octets = ip_address.split('.')

    # Convert the octets to integers
    ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])

    # Calculate the network address
    network_int = ip_int & ((2 ** prefix_length - 1) << (32 - prefix_length))

    # Calculate the number of hosts in the network
    num_hosts = 2 ** (32 - prefix_length) - 1

    # Calculate the broadcast address
    broadcast_int = network_int + num_hosts

    # Convert the broadcast address back to octets
    broadcast_octets = [(broadcast_int >> 24) & 0xFF,
                        (broadcast_int >> 16) & 0xFF,
                        (broadcast_int >> 8) & 0xFF,
                        broadcast_int & 0xFF]

    # Join octets to form the broadcast address
    broadcast_address = '.'.join(map(str, broadcast_octets))

    return broadcast_address


# Function to compare the network ID provided by the user with the calculated network ID
def enter_net_ID(net_ID):
    while True:
        print("Enter the net ID ")
        print("(or 'c' to calculate again, 'q' to quit)")
        user_net_ID = input()
        if user_net_ID == "q":
            print("better luck next time!")
            break
        if user_net_ID == "c":
            calculations()
        elif user_net_ID == net_ID:
            print("Great! the net ID is " + net_ID)
            break
        else:
            print("wrong net ID. Try again")


# Function to compare the broadcast address provided by the user with the calculated broadcast address
def enter_broadcast(broadcast):
    while True:
        print("Enter the broadcast address ")
        print("(or 'c' to calculate again, 'q' to quit)")
        user_broadcast = input()
        if user_broadcast == "q":
            print("better luck next time!")
            break
        if user_broadcast == "c":
            calculations()
        elif user_broadcast == broadcast:
            print("Great! the broadcast address is " + broadcast)
            break
        else:
            print("wrong broadcast address. Try again")


def main():
    # Get user input for the decimal IP address
    decimal_ip = input("Enter a decimal IP address (e.g., 192.168.1.1): ")

    # Call the function to convert the input IP address to binary
    binary_ip = decimal_to_binary(decimal_ip)

    # Get user input for the prefix length
    prefix_length = int(input("Enter a prefix length (e.g., 23): "))

    # Call the functions to convert the prefix length to a binary subnet mask
    decimal_subnet_mask = prefix_length_to_decimal(prefix_length)
    binary_subnet_mask = decimal_to_binary(decimal_subnet_mask)

    # Call the function to find the net ID and the broadcast address
    net_ID = calculate_network_id(decimal_ip, prefix_length)
    broadcast = calculate_broadcast_address(decimal_ip, prefix_length)

    # Display the results
    show_address(decimal_ip, decimal_subnet_mask, prefix_length, binary_ip, binary_subnet_mask)

    # User calculations to determine network ID and broadcast addresses
    print()
    calculations()

    # compare the net ID provided by the user with the calculated net ID
    print()
    enter_net_ID(net_ID)

    # compare the broadcast address provided by the user with the calculated broadcast address
    print()
    enter_broadcast(broadcast)


if __name__ == "__main__":
    main()
