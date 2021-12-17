"""
Mailinator Ulauncher Extension
Generate a fake email address and open it for you in Mailinator website
See: https://ext.ulauncher.io/-/github-brpaz-ulauncher-mailinator
"""

import logging
import random
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.ActionList import ActionList
from faker import Faker

LOGGER = logging.getLogger(__name__)
MAILINATOR_URL = "https://mailinator.com/v3/index.jsp?zone=public&query=%s"
FAKE = Faker()

class MailinatorExtension(Extension):
    """ Main extension class """

    def __init__(self):
        LOGGER.info('init Mailinator Extension')
        super(MailinatorExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    """ Query Event listener """

    def on_event(self, event, extension):
        """ Event handler """
        items = []

        if event.get_argument() is not None:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=event.get_argument(),
                    description="Press enter to open on mailinator.com",
                    on_enter=OpenUrlAction(MAILINATOR_URL %
                                           event.get_argument())))
        else:
            email = extension.preferences.get("prefix") + FAKE.user_name( # pylint: disable=no-member
            ) + str(random.randint(1000, 9999))

            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name="%s@mailinator.com" % email,
                    description=
                    "Press enter to copy to the cliboard. Alt+Enter to copy and open",
                    highlightable=False,
                    on_enter=CopyToClipboardAction(email + "@mailinator.com"),
                    on_alt_enter=ActionList([
                        OpenUrlAction(MAILINATOR_URL % email),
                        CopyToClipboardAction(email + "@mailinator.com")])))

        return RenderResultListAction(items)

if __name__ == '__main__':
    MailinatorExtension().run()
