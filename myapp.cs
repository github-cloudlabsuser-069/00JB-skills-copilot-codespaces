// See https://aka.ms/new-console-template for more information
using Azure;
using Azure.AI.OpenAI;
Console.WriteLine("Hello, World!");

// Initialize the Azure OpenAI client
OpenAIClient client = new OpenAIClient(new Uri("https://oaivenkatcaeast.openai.azure.com/"), new AzureKeyCredential("7aa876218e904ad19e310f46d2d90b48"));

// System message to provide context to the model
string systemMessage = "I am a hiking enthusiast named Forest who helps people discover hikes in their area. If no area is specified, I will default to near Rainier National Park. I will then provide three suggestions for nearby hikes that vary in length. I will also share an interesting fact about the local nature on the hikes when making a recommendation.";

// Ask the user for input text
Console.WriteLine("Please enter your input text:");
string inputText = Console.ReadLine();

// Add the prompt
string prompt = inputText;

// Build completion options object
ChatCompletionsOptions chatCompletionsOptions = new ChatCompletionsOptions()
{
    Messages =
     {
         new ChatRequestSystemMessage(systemMessage),
         new ChatRequestUserMessage(prompt),
     },
    MaxTokens = 400,
    Temperature = 0.7f,
    DeploymentName = "35Turbo"
};

// Send request to Azure OpenAI model
ChatCompletions response = client.GetChatCompletions(chatCompletionsOptions);

// Print the response
string completion = response.Choices[0].Message.Content;
Console.WriteLine("Response: " + completion + "\n");

