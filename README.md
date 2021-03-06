# wedding-helper
A suite of scripts and tools to help us plan our wedding easier

## Setup and usage

### Setting up the environment

Copy the `template.env` file to `.env` and fill in the values:

```bash
cp template.env .env
# Edit the .env file
```

Setup python virtual environment:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```


### Running the scripts

| Script       | Description                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `./main.py`  | Script used to parse the Save the Dates google form spreadsheet and create a CSV file to import the data into a [withjoy](https://withjoy.com) guest list database. |


## References

- Importing guest information via CSV files in withjoy: https://help.withjoy.com/knowledge-base/inviting-guests-from-a-csv-file
- Exporting a Notion database to a CSV file: https://www.notion.so/Export-a-database-as-CSV-89654fbb61264d5eb2025a7606a8e3d4
