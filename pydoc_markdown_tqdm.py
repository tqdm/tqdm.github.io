from pydoc_markdown.contrib.processors.pydocmd import PydocmdProcessor
import re
from functools import partial

compile = partial(re.compile, flags=re.M)
RE_PARAM_ANY = compile(r"^(\w+\s{2,}:.*?)\*(.*?)$")
RE_PARAM = compile(r"^(\w+)\s{2,}(:.*?)$")
RE_H2 = compile(r"^(.+?)\n[-]{4,}$")
RE_REPL = compile(r"^(>>>|\.\.\.)(.*?)$")
RE_REPL_MLINE = compile(r"^(>>>|\.\.\.)(.*?)\n```\n```\n(>>>|\.\.\.)")
RE_REPL_BLOCK = compile(r"^(```)(\n>>>)")
RE_LONG_LINE = compile(r"\\\n\s*")


class TqdmProcessor(PydocmdProcessor):
    def _process(self, node):
        if not getattr(node, "docstring", None):
            return

        # join long lines ending in escape (\)
        node.docstring = RE_LONG_LINE.sub("", node.docstring)
        # escape literal `*`
        node.docstring = RE_PARAM_ANY.sub(r"\1\\*\2", node.docstring)
        # convert parameter lists to markdown list
        node.docstring = RE_PARAM.sub(r"* __\1__*\2*  ", node.docstring)
        # convert REPL code blocks to code
        node.docstring = RE_REPL.sub(r"```\n\1\2\n```", node.docstring)
        node.docstring = RE_REPL_MLINE.sub(r"\1\2\n\3", node.docstring)
        node.docstring = RE_REPL_MLINE.sub(r"\1\2\n\3", node.docstring)
        node.docstring = RE_REPL_BLOCK.sub(r"\1python\2", node.docstring)
        # hide <h2> from `nav`
        node.docstring = RE_H2.sub(r"__\1__\n", node.docstring)

        return super()._process(node)
