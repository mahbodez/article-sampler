# this script takes in an EndNote XML file and outputs a random sample of the references
# by writing YES/NO in the "custom3" field of the XML file
import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm
import random


def parse_args():
    parser = argparse.ArgumentParser(
        description="Process XML file and sample references"
    )
    parser.add_argument("--xml_file", type=str, help="path to EndNote XML file")
    parser.add_argument("--output_file", type=str, help="path to output XML file")
    parser.add_argument(
        "--sample_size", type=int, default=200, help="number of references to sample"
    )
    parser.add_argument(
        "--ratingfield",
        type=str,
        default="custom3",
        help='field to store rating in, default: "custom3"',
    )
    parser.add_argument("--seed", type=int, default=42, help="random seed")
    return parser.parse_args()


args = parse_args()


with open(args.xml_file, "r", encoding="utf-8") as f:
    xml_data = f.read()

soup = BeautifulSoup(xml_data, "xml")
# find all the article records in the XML data
article_records = soup.find_all("record")

random.seed(args.seed)
indices = random.sample(range(len(article_records)), args.sample_size)


# loop through each article and add the rating and the answer as a new tag
for i, record in tqdm(enumerate(article_records)):
    # create a new 'custom3' tag (the default is 'custom3')
    rating_tag = soup.new_tag(args.ratingfield)
    if i in indices:
        rating_tag.string = "Yes"  # set the text of the tag to the rating
    else:
        rating_tag.string = "No"
    record.append(rating_tag)  # add the new tag to the article record

outfilepath = ""
if "." in args.output_file:
    outfilepath = args.output_file[: args.output_file.rfind(".")]
else:
    outfilepath = args.output_file

try:
    with open(outfilepath + ".xml", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print(f"results saved to {outfilepath}.xml.")
except OSError:
    print("an error occured during saving.\nsaving to relative path...")
    with open("newfile.xml", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("results saved to newfile.xml.")
