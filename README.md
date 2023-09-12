# demo-document-indexer
This is an Azure Functions app triggered by an Event Grid event. It logs the event data and performs a sanity check to ensure the event type is valid. It uses PyPDF2 to chunk a PDF file into pages and uploads each page as a separate blob to a destination Azure Storage account.
