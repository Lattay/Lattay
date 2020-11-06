#!/usr/bin/env python3

logos = [
    ('python', 'https://python.org'),
    ('chicken', 'https://call-cc.org'),
    ('ocaml', 'https://ocaml.org'),
    ('c', 'https://fr.wikipedia.org/wiki/C_(langage)'),
    ('fortran', 'https://en.wikipedia.org/wiki/Fortran#Fortran_2003'),
    ('bash', 'https://en.wikipedia.org/wiki/Bash_(Unix_shell)'),
    ('javascript', 'https://developer.mozilla.org/fr/docs/Web/JavaScript'),
    ('neovim', 'https://neovim.io/'),
    ('docker', 'https://docker.com'),
    ('drone', 'https://drone.io/'),
]


def gen_link(name, link):
    return f'<a href="{link}" ><img src="assets/{name}/{name}.png" width="64" alt="{name} logo"></a>'


def gen_links(logos):
    return '\n'.join(gen_link(name, link) for name, link in logos)


content = f'''\
### Hi there 👋

I am a hobbyist programmers passionate about programming languages and open source.
I have coded for the ❤ of it since 2012 and I am happy to share my experience and ideas with anyone !

I am a recently graduated engineer (specialized in computational solid state physics) and to become theoretical chemistry 🧪 PhD student.

I like working on ephemeral projects for the love of problem solving, but also more durable open source projects.

My interests includes:

* Vim/Neovim plugin
* programming languages design and experimentation
* 👾 game development

{gen_links(logos)}

<a href=https://github.com/anuraghazra/github-readme-stats>
<img alt="Theo's Github stats" src="https://github-readme-stats.vercel.app/api?username=lattay&show_icons=true">
</a>
'''

with open('README.md', 'w') as f:
    f.write(content)
