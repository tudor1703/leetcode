def tenth_line(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if len(lines) >= 10:
                print(lines[9].strip())
            else:
                print("there are not 10 lines")
    except FileNotFoundError:
        print(f"file '{filename}' doesn't exist!")

filename = "pr.195.txt"
tenth_line(filename)