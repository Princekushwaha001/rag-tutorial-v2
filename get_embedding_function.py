from langchain_ollama import OllamaEmbeddings

# from langchain_community.embeddings.bedrock import BedrockEmbeddings

def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    embeddings = OllamaEmbeddings(model="mistral")
    return embeddings
