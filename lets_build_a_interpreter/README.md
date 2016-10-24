# References
[Website](https://ruslanspivak.com/lsbasi-part1/)

# To Run Unit Tests

    pip install -r build_requires

then

    pytest tests.py

# Order Of Features Added

1. Tokens
2. Tokens `__repr__` and `__str__`
3. Blank Program Parsers
4. Interpreter Error Method
5. EOF token lexes
    * `-` token lexes
    *  `+` token lexes
6 Single digit integer token lexes
7. consume validates expected token
8. consume errors on unexpected token
9. consume produces EOF if no more tokens
10. `1+1` lexes and parsers to 2
11. multi-digit integers are lexed correctly
12. whitespace is ignored until new token found.
13. `*` lexes and parsers
14. `/` lexes and parsers
15. Arbitrary number of operations lex and parse correctly.
16. `()` lexes and parsers
17. parens around signle statement lexes and parsers
18. parens can arbitrarily nest
19. Parens change the order of operations.
