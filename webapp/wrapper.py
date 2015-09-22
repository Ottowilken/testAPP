ZENDESK_URL='https://otto.zendesk.com/api/v2/users/me.json'
ZENDESK_KEY='otto@epinion.co.za/token:ROsCPf9YoDkzpW8CX0C3Im53o9nVbkleDttpZeib'

__author__ = 'Otto'


def zendesk_api_post(url, meth, data):
    from io import BytesIO
    import pycurl
    import json
    try:
        data=json.dumps(data)
        c = pycurl.Curl()
        cred = ZENDESK_KEY
        pUrl = ZENDESK_URL + str(url)
        c.setopt(c.URL, pUrl)
        buf = BytesIO()
        c.setopt(c.WRITEDATA, buf)
        c.setopt(c.CONNECTTIMEOUT, 5)
        c.setopt(c.TIMEOUT, 8)
        if not data == "null":
         c.setopt(c.POSTFIELDS, data)
        c.setopt(c.FOLLOWLOCATION, True)
        c.setopt(c.MAXREDIRS, 10)
        c.setopt(c.USERPWD, cred)
        c.setopt(c.CUSTOMREQUEST, meth)
        c.setopt(c.HTTPHEADER, ['Content-type: application/json'])
        c.perform()
        result = buf.getvalue().decode('utf-8')
        buf.close()
    except Exception as e:
        raise e