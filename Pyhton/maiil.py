import keyring
keyring.set_password('yagmail', 'sreerammaram2@gmail.com', 'sreeramM31@')

import yagmail
FROM = "sreerammaram2@gmail.com"
TO = "sreerammaram@rocketmail.com"
SUBJECT = "test email"
TEXT = "details go here"

yagmail.SMTP(FROM).send(TO, SUBJECT, TEXT)