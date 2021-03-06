# -*- coding: utf-8 -*-
import urllib

from pipobot.lib.module_test import ModuleTest
from pipobot.lib.modules import SyncModule, defaultcmd


class CmdCmdFu(SyncModule):
    def __init__(self, bot):
        desc = """Commandline tips
cmdfu : Retourne une commande aléatoire"""
        SyncModule.__init__(self,
                            bot,
                            desc=desc,
                            name="cmdfu",
                            )

    @defaultcmd
    def answer(self, sender, message):
        url = "http://www.commandlinefu.com/commands/random/plaintext"
        url = urllib.urlopen(url)
        contenu = url.read()
        return "\n".join(contenu.strip().split("\n")[2:])


class TestCmdfu(ModuleTest):
    def test_cmdfu(self):
        self.assertNotEqual(self.bot_answer("!cmdfu"), "")
