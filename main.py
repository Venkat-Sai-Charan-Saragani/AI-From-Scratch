import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1-mini")
tokens = encoding.encode("venkata sai charan")

print(tokens)

print(encoding.decode(tokens))


# this will split each thing and then encode it
# for token_id in tokens:
#     token_text = encoding.decode([token_id])
#     print(f"{token_id} -> {token_text}")