## Random Article Sampler Script
This script is designed to randomly sample N articles from a given EndNote XML file. The script will output a new XML file containing the randomly sampled articles.
### Arguments
- **--xml_file**: The path to the EndNote XML file to be sampled.
- **--output_file**: The path to the output XML file.
- **--sample_size**: The number of articles to sample.
- **ratingfield**: The field in the EndNote XML file to store sampling information. This field will be set to YES for sampled articles and NO for non-sampled articles. default: "custom3"
- **--seed**: The random seed to use for sampling. If not provided, the script will use 42 as the default seed.
### Example Usage
```bash
"path/to/python3.exe" sampler.py --xml_file "path/to/input.xml" --output_file "path/to/output.xml" --sample_size 200 --ratingfield "custom3" --seed 42
```