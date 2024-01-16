import argparse

parser = argparse.ArgumentParser()

parser.add_argument("url", help="Url of the file to download")
# parser.add_argument("output", help="Which name you want to give file?")
parser.add_argument("-o", "--output", help="Which name you want to give file?")

args = parser.parse_args()

print(args.url)
print(args.output)