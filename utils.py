"""
    :author: pbouillon  [https:/pbouillon.github.io/]
    :license: Unlicense [See LICENSE.txt]
"""


class Mail:
    """References useful data for mail sending

    Attributes

        Recipient       Destination mailbox
        Sender          Sender's address
        Server_addr     SMTP server's addr
        Server_port     SMTP server's port
        Subject         Mail subject
    """

    class Credentials:
        """ References the user's credentials
        """
        LOGIN = 'mathieu.dreyer@sii.fr'
        PASSWORD = 'ImNotDumbEnoughToPublishThat'

    RECIPIENT = 'mathieu.dreyer@sii.fr'
    SENDER = 'secret-santa@sii.fr'
    SERVER_ADDR = 'smtp.gmail.com'
    SERVER_PORT = 587
    SUBJECT = '🎁 [Secret Santa] Nom de la personne à qui faire plaisir !'
