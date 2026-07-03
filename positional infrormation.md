positional infromation means taking the infromation are input according to the positions they are in.

polished version - Positional information provides the model with the position of each token in the input sequence. Since transformer attention does not inherently know token order, positional information is combined with token embeddings so the model can learn both the meaning of tokens and their order in the sequence.

Sentence 1:

The dog chased the cat

Sentence 2:

The cat chased the dog

The embeddings tell the model what "dog", "cat", and "chased" mean, but they don't tell it where those words appear.

## Interview questions

What is positional information?

Positional information tells the model the position of each token in the sequence.

Why do we need positional information?

Because the transformer's self-attention mechanism doesn't inherently know the order of tokens. Positional information allows the model to distinguish between sentences with the same words in different orders.

When is positional information added?

After the embedding layer and before the embeddings are passed into the first transformer block.
