str = "             c\n" \
      "             o\n" \
      "             m\n" \
      "             prudent\n" \
      "             l\n" \
      "     w       y\n" \
      "     r   l   w\n" \
      "  accountability\n" \
      "     n   w   t\n" \
      "     g   f f h\n" \
      "     d   u r  \n" \
      "    comeclean \n" \
      "     i     u  \n" \
      "     n     d  t\n" \
      "pleadguilty h a\n" \
      "        a   e k\n" \
      "        w   p e\n" \
      "        s w o t\n" \
      "        u h t h\n" \
      "     legitimize\n" \
      "        t s s h\n" \
      "          t m e\n" \
      "          l   legitimate\n" \
      "          e   m\n" \
      " tocookthebook \n" \
      "          l    \n" \
      "          o    \n" \
      "          w    \n" \
      "          e    \n" \
      "          r\n"

res = "[\n["
for char in str:
    if char == ' ':
        res += "{isBlank: 1, char: ' '},"
    elif char == '\n':
        res += "],\n["
    else:
        res += "{isBlank: 0, char: '" + char + "'},"

res = res[:-1] + ']'

print(res)
