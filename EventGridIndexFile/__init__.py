import json
import os
import tempfile
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from urllib.parse import urlparse
import PyPDF2

def main(event: func.EventGridEvent):
    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })
    logging.info('Python EventGrid trigger processing an event: %s', result)

    # Sanity check
    event_data = event.get_json()
    if event.event_type!= "Microsoft.Storage.BlobCreated":
        logging.error("Invalid event type")
        return
    # Get the storage account connection strings from environment variables
    source_connection_string = os.environ["SOURCESTORAGE_CONNECTIONSTRING"]
    dest_connection_string = os.environ["DESTSTORAGE_CONNECTIONSTRING"]

    # Get the blob URL from the event data
    blob_url = event_data["url"]
    blob_name = os.path.basename(urlparse(blob_url).path)

    # Create a BlobServiceClient for the source storage account
    source_blob_service_client = BlobServiceClient.from_connection_string(source_connection_string)

    # Get the blob client for the PDF file
    source_blob_client = source_blob_service_client.get_blob_client(container="enterprisedata", blob=blob_name)

    # Download the PDF file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        download_stream = source_blob_client.download_blob()
        temp_file.write(download_stream.readall())

    with open(temp_file.name, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            # Get the page as a PDF object
            pdf_page = pdf_reader.pages[page_num]

            # Create a new PDF file with just this page
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(pdf_page)

            # Write the new PDF file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False) as page_file:
                pdf_writer.write(page_file)

            # Upload the new PDF file to the destination storage account
            dest_blob_service_client = BlobServiceClient.from_connection_string(dest_connection_string)
            dest_blob_client = dest_blob_service_client.get_blob_client(container="pages", blob=f"{blob_name}_page{page_num}.pdf")
            with open(page_file.name, "rb") as page_data:
                dest_blob_client.upload_blob(page_data)

    # Delete the temporary file
    os.unlink(temp_file.name)

    return result