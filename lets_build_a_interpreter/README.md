# References
[Website](https://ruslanspivak.com/lsbasi-part1/)

# To Run Unit Tests

    pip install -r build_requires

then

    pytest tests.py

# Order Of Features Added

1. Tokens
2. Tokens `__repr__` and `__str__`
3. Interpreter Error Method
4. EOF token lexes
5. `-` token lexes
6. `+` token lexes
7. Blank Program Parsers
9. Single digit integer token lexes
10. consume validates expected token
11. consume errors on unexpected token
12. consume produces EOF if no more tokens
13. `1+1` lexes and parsers to 2
14. multi-digit integers are lexed correctly
15. whitespace is ignored until new token found.
16. `*` lexes and parsers
17. `/` lexes and parsers
18. Arbitrary number of operations lex and parse correctly.
19. `()` lexes and parsers
20. parens around signle statement lexes and parsers
21. parens can arbitrarily nest
22. Parens change the order of operations.
