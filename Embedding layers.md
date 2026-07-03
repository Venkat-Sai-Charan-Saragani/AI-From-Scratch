This Embedding layer means converting the converted text into tokens which has no meaning on its own, 
and converting them into a meaningful vectos that consits semantic information, where neural network can understand the language easily.


## interview question

What is an embedding?
polished version - The embedding layer converts token IDs (produced by the tokenizer) into dense numerical vectors called embeddings. These vectors capture semantic meaning learned during training, allowing the neural network to process relationships and patterns in language. Token IDs themselves have no semantic meaning—they are simply identifiers.


Why do we need embeddings?
we need embidding coz the neural network can directly understand the tokens directly coz the tokens dosen't have the meaning directly, to add a semantic meaning to the text that we have where neural network can understand easily we need embiddings.

What is an embedding layer?
the layer which take the input as tokens from tokenizer and convert them into embidding vectors are known as embedding layer.

What is an embedding vector?
the vectors which consists embedded tokens which is ready to use by a neural network

How does the embedding layer work internally?
Token ID
↓
Use it as an index
↓
Look up the corresponding row
↓
Return the embedding vector

Are embeddings hardcoded?
No.
They start randomly and are learned during training.


Can embeddings change during training?
Yes.
Every training step updates the embedding vectors through backpropagation.
