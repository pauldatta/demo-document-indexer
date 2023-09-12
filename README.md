# demo-document-indexer
This is an Azure Functions app triggered by an Event Grid event. It logs the event data and performs a sanity check to ensure the event type is valid. It uses PyPDF2 to chunk a PDF file into pages and uploads each page as a separate blob to a destination Azure Storage account.

## Getting Started
To get started with this project, you'll need to have the following prerequisites installed:

- Python 3.6 or later
- Azure Functions Core Tools
- PyPDF2 library

## Deploy to Azure using VS Code

You can use the Azure Functions extension for VS Code to deploy your function app to Azure. Before you start, make sure you have the following prerequisites:

- Visual Studio Code installed on your machine.
- Azure Functions extension for VS Code installed.
- An active Azure subscription. If you don't have one, you can create a free account.
- Azure Functions Core Tools version 3.x or later installed.

To deploy your function app, follow these steps:

1. Open the demo-document-indexer folder in VS Code.
2. Sign in to your Azure account and select the subscription that you want to use.
3. In the Azure view, expand the Function Apps node and select the + button. Choose Create New Function App in Azure (Advanced).
4. Enter a globally unique name for your function app and press Enter.
5. Choose Python 3.9 as the runtime stack and press Enter.
6. Choose Linux as the OS and press Enter.
7. Choose Consumption (Serverless hosting plan) as the hosting plan and press Enter.
8. Choose Create new resource group and enter a name for your resource group and press Enter.
9. Choose Create new storage account and enter a name for your storage account and press Enter.
10. Choose Skip for now when asked to create an Application Insights resource.
11. Wait for the deployment to complete. You can see the progress in the Output window.
12. After the deployment is done, you can see your function app in the Azure view under the Function Apps node.



## Contributing
Contributions to this project are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.