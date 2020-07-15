from __future__ import print_function
from pydoc_markdown.contrib.processors.pydocmd import PydocmdProcessor
import re

RE_PARAM = re.compile(r"^(\w+\s{2,}:.*?)$", flags=re.M)
RE_H2 = re.compile(r"^(.+?)\n[-]{4,}$", flags=re.M)
RE_REPL = re.compile(r"^(>>>|\.\.\.)(.*?)$", flags=re.M)
RE_REPL_MLINE = re.compile(
    r"^(>>>|\.\.\.)(.*?)\n```\n```\n(>>>|\.\.\.)", flags=re.M)
RE_REPL_BLOCK = re.compile(r"^(```)(\n>>>)", flags=re.M)
# RE_H1 = re.compile(r'^(<h1 id=".*?">)(.*?)(</h1>)$', flags=re.M)


class TqdmProcessor(PydocmdProcessor):
    def _process(self, node):
        if not getattr(node, 'docstring', None):
            return

        # convert parameter lists to markdown list
        node.docstring = RE_PARAM.sub(r"* \1  ", node.docstring)
        # convert REPL code blocks to code
        node.docstring = RE_REPL.sub(r"```\n\1\2\n```", node.docstring)
        node.docstring = RE_REPL_MLINE.sub(r"\1\2\n\3", node.docstring)
        node.docstring = RE_REPL_MLINE.sub(r"\1\2\n\3", node.docstring)
        node.docstring = RE_REPL_BLOCK.sub(r"\1python\2", node.docstring)
        # hide <h2> from `nav`
        node.docstring = RE_H2.sub(r"<h2>\1</h2>", node.docstring)

        return super()._process(node)
