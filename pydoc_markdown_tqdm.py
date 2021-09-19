from pydoc_markdown.contrib.processors.pydocmd import PydocmdProcessor
import re
from functools import partial

sub = partial(re.sub, flags=re.M)


class TqdmProcessor(PydocmdProcessor):
    def _process(self, node):
        if not getattr(node, "docstring", None):
            return

        # join long lines ending in escape (\)
        node.docstring = sub(r"\\\n\s*", "", node.docstring)
        # escape literal `*`
        node.docstring = sub(r"^(\w+\s{2,}:.*?)\*(.*?)$", r"\1\\*\2", node.docstring)
        # convert parameter lists to markdown list
        node.docstring = sub(r"^(\w+)\s{2,}(:.*?)$", r"* __\1__*\2*  ", node.docstring)
        # convert REPL code blocks to code
        node.docstring = sub(r"^(>>>|\.\.\.)(.*?)$", r"```\n\1\2\n```", node.docstring)
        node.docstring = sub(r"^(>>>|\.\.\.)(.*?)\n```\n```\n(>>>|\.\.\.)", r"\1\2\n\3", node.docstring)
        node.docstring = sub(r"^(>>>|\.\.\.)(.*?)\n```\n```\n(>>>|\.\.\.)", r"\1\2\n\3", node.docstring)
        node.docstring = sub(r"^(```)(\n>>>)", r"\1python\2", node.docstring)
        # hide <h2> from `nav`
        node.docstring = sub(r"^(.+?)\n[-]{4,}$", r"__\1__\n", node.docstring)

        return super()._process(node)
