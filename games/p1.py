
import optparse

parser = optparse.OptionParser()

def summation(number):
    numbers_total = sum([i for i in range(1, number) if i%3==0 or i%5==0])
    print(numbers_total)


if __name__ == "__main__":
    parser.add_option(
        '-n', '--number',
        action="store",
        dest="number",
        help="Max number in range",
        default="10"
    )
    options, args = parser.parse_args()
    number = int(options.number)
    summation(number)
