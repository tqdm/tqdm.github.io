from __future__ import print_function
from pydocmd.preprocessors.simple import Preprocessor as SimplePreprocessor
import re

RE_PARAM = re.compile(r"^(\w+\s{2,}:.*?)$", flags=re.M)
RE_H2 = re.compile(r"^(.+?)\n[-]{4,}$", flags=re.M)
RE_REPL = re.compile(r"^(>>>|\.\.\.)(.*?)$", flags=re.M)
RE_REPL_MLINE = re.compile(
    r"^(>>>|\.\.\.)(.*?)\n```\n```\n(>>>|\.\.\.)", flags=re.M)
RE_REPL_BLOCK = re.compile(r"^(```)(\n>>>)", flags=re.M)
# RE_H1 = re.compile(r'^(<h1 id=".*?">)(.*?)(</h1>)$', flags=re.M)


"""
class Section(pydocmd.document.Section)
    def render(self, stream):
        if self.depth != 1:
            super(Section, self).render(stream)
            return
        print('# {title}<h{depth} id="{id}"></h{depth}>\n'
            .format(depth=self.depth, id=self.identifier, title=self.title),
            file=stream)
        print(self.content, file=stream)
"""
def overloadSection(section):
    """Make section.render() show up in `nav` for h1"""
    if section.depth != 1:
        return

    def render(stream):
        print('# {title}<h{depth} id="{id}"></h{depth}>\n'.format(
            depth=section.depth, id=section.identifier, title=section.title),
            file=stream)
        print(section.content, file=stream)
    section.render = render


class Preprocessor(SimplePreprocessor):
    def preprocess_section(self, section):
        super(Preprocessor, self).preprocess_section(section)
        # convert parameter lists to markdown list
        section.content = RE_PARAM.sub(r"* \1  ", section.content)
        # convert REPL code blocks to code
        section.content = RE_REPL.sub(r"```\n\1\2\n```", section.content)
        section.content = RE_REPL_MLINE.sub(r"\1\2\n\3", section.content)
        section.content = RE_REPL_MLINE.sub(r"\1\2\n\3", section.content)
        section.content = RE_REPL_BLOCK.sub(r"\1python\2", section.content)
        # hide <h2> from `nav`
        section.content = RE_H2.sub(r"<h2>\1</h2>", section.content)
        # escape underscores in special methods
        if section.title[:2] == "__" == section.title[-2:]:
            section.title = r'\_\_' + section.title[2:-2] + r'\_\_'
        # expose <h1> in `nav`
        # section.content = RE_H1.sub(r"# `\2` \1\3", section.content)
        overloadSection(section)
