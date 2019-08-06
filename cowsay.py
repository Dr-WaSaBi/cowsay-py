# A python implementation of cowsay <http://www.nog.net/~tony/warez/cowsay.shtml>
# Copyright 2011 Jesse Chan-Norris <jcn@pith.org>
# Licensed under the GNU LGPL version 3.0

# Updating to support more cow types, maybe eyes, etc.
# Russell R. Riker
# Thanks to Jesse Chan-Norris for publishing the base code that I'm 
# starting from.

import sys
import textwrap
import cowtypes

def cowsay(cowType, str, length=40):
    if cowType == "mad":
        return build_bubble(str, length) + build_oddcow()

    elif cowType == "cow":
        return build_bubble(str, length) + build_cow()


def build_oddcow():
    return """
         \   <__> 
          \  (db)\_______
             (__)\       )\/\\
                 ||----W |
                 ||     ||
    """

def build_cow():
    return """
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

def build_bubble(str, length=40):
    bubble = []

    lines = normalize_text(str, length)

    bordersize = len(lines[0])

    bubble.append("  " + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalize_text(str, length):
    lines  = textwrap.wrap(str, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]

    elif index == 0:
        return [ "/", "\\" ]
    
    elif index == len(lines) - 1:
        return [ "\\", "/" ]
    
    else:
        return [ "|", "|" ]


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: '%s cow type string'" % sys.argv[0])
        sys.exit(0)

    print(cowsay(sys.argv[1],sys.argv[2]))
