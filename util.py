def saveUserChoices(isReply, format, tone):
    class UserChoices:
        def __init__(self, isReply, format, tone):
            self.reply = True if isReply == 'yes' else False
            self.email = True if format == 'email' else False
            self.text =True if format == 'text' else False
            self.review =True if format == 'review' else False
            self.casual=True if tone == 'casual' else False
            self.professional=True if tone == 'professional' else False

    userChoices = UserChoices(isReply, format, tone)
    return userChoices
