import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from faker import Faker
import random

logger = logging.getLogger(__name__)
fake = Faker()

MAILINATOR_URL = "https://www.mailinator.com/v2/inbox.jsp?zone=public&query="


class MailinatorExtension(Extension):

    def __init__(self):
        logger.info('init Mailinator Extension')
        super(MailinatorExtension, self).__init__()
        self.subscribe(
            KeywordQueryEvent,
            KeywordQueryEventListener()
        )


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []

        if (event.get_argument() is not None):
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=event.get_argument(),
                    description="Press enter to open on mailinator.com",
                    on_enter=OpenUrlAction(
                        '{}{}'.format(MAILINATOR_URL, event.get_argument())
                    )
                )
            )
        else:
            email = '{}{}{}'.format(
                extension.preferences.get("prefix"),
                fake.user_name(),
                str(random.randint(1000, 9999))
            )

            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name='{}@mailinator.com'.format(email),
                    description="Press enter to copy to the cliboard. Alt+Enter to open",
                    highlightable=False,
                    on_enter=CopyToClipboardAction(email),
                    on_alt_enter=OpenUrlAction('{}{}'.format(
                            MAILINATOR_URL,
                            email
                        )
                    )
                )
            )

        return RenderResultListAction(items)

if __name__ == '__main__':
    MailinatorExtension().run()
