# demo-document-indexer
This is an Azure Functions app triggered by an Event Grid event. It logs the event data and performs a sanity check to ensure the event type is valid. It uses PyPDF2 to chunk a PDF file into pages and uploads each page as a separate blob to a destination Azure Storage account.

## Getting Started
To get started with this project, you'll need to have the following prerequisites installed:

- Python 3.6 or later
- Azure Functions Core Tools
- PyPDF2 library


## Contributing
Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.