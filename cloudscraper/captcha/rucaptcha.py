import twocaptcha
import requests

class captchaSolver(twocaptcha.captchaSolver):
    def __init__(self):
        super(twocaptcha.captchaSolver, self).__init__('rucaptcha')
        self.host = 'https://rucaptcha.com'
        self.session = requests.Session()
        self.captchaType = {
            'reCaptcha': 'userrecaptcha',
            'hCaptcha': 'hcaptcha',
            'turnstile': 'turnstile'
        }
