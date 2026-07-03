This Embedding layer means converting the converted text into tokens which has no meaning on its own, 
and converting them into a meaningful vectos that consits semantic information, where neural network can understand the language easily.


## interview question

## What is an embedding?

polished version - The embedding layer converts token IDs (produced by the tokenizer) into dense numerical vectors called embeddings. These vectors capture semantic meaning learned during training, allowing the neural network to process relationships and patterns in language. Token IDs themselves have no semantic meaning—they are simply identifiers.


## Why do we need embeddings?
we need embidding coz the neural network can directly understand the tokens directly coz the tokens dosen't have the meaning directly, to add a semantic meaning to the text that we have where neural network can understand easily we need embiddings.

poloshed version - We need embeddings because token IDs are simply numerical identifiers and do not contain semantic meaning. The embedding layer converts these IDs into dense vectors that capture semantic relationships, allowing the neural network to perform meaningful mathematical computations on language.

## What is an embedding layer?
the layer which take the input as tokens from tokenizer and convert them into embidding vectors are known as embedding layer.

polished version - The embedding layer is the first learned layer of a language model. It takes token IDs as input and converts them into dense embedding vectors that are used by the transformer.

## What is an embedding vector?
the vectors which consists embedded tokens which is ready to use by a neural network

polished version - An embedding vector is a dense numerical representation of a token. It contains learned semantic information that enables the neural network to understand relationships between different tokens.

## How does the embedding layer work internally?
Token ID
↓
Use it as an index
↓
Look up the corresponding row
↓
Return the embedding vector
Internally, the embedding layer performs a lookup in the embedding matrix using the token ID as the index.

## Are embeddings hardcoded?
No.
They start randomly and are learned during training.
 
## Can embeddings change during training?
Yes.
Every training step updates the embedding vectors through backpropagation.

## What does "semantic meaning" mean in embeddings?
semantic meaning mean the tokens which has the meaning that consists of words where neural network cna understand 

polished version - Semantic meaning refers to the information about a token's meaning and its relationship to other tokens. Similar words, such as "king" and "queen" or "dog" and "puppy", tend to have similar embedding vectors because they often appear in similar contexts during training.

## What is the difference between one-hot encoding and embeddings?

A favorite interview question.

Expected idea:

One-hot:

Dog

↓

[0 0 0 1 0 0]

Embedding:

Dog

↓

[0.42 -0.13 ...]

Embeddings capture similarity; one-hot vectors do not.
