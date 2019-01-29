
from conans.tools import replace_in_file

def main():
    f = r'/Users/travis/.pyenv/versions/conan/lib/python3.4/site-packages/conans/model/manifest.py'

    replace_in_file(f, "the_time = int(tokens[0])", """print("*"*20)
        print(tokens)
        print("*"*20)""")

    f = r'/Users/travis/.pyenv/versions/conan/lib/python3.4/site-packages/conans/model/manifest.py'
    replace_in_file(f, "# Unroll generator and decode shas (plain text)", 
                    """print(urls)
        print(contents.keys())
        print(contents)""")


main()
