[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22502140&assignment_repo_type=AssignmentRepo)
# Caesar Cipher

Here's how Caesar Cipher works:

https://docs.google.com/presentation/d/1e4DIhg4GoHrQ3CcEM8_aiyiyrdenIt9bURQ8-s_dKuU/edit?slide=id.g3bf7752d4be_0_1483#slide=id.g3bf7752d4be_0_1483

Implement a Caesar Cipher in `main.py`

For an extra challenge you could try:

* wrap everything in an `encrypt` function that takes in plaintext and returns ciphertext, with a `key` as a parameter that says how many letters forward or back you will shift the alphabet
* make a corresponding `decrypt` function that also takes a `key` as input, that takes in ciphertext and returns plaintext
* write an automatic code breaker for a Caesar cipher that uses a `for` loop to try out lots of keys --- if you do this, try sending each other secret messages
* implement a [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) were you use a different `key` for each position in the plaintext