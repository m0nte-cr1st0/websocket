from django.http import HttpResponse
from channels.handler import AsgiHandler


def http_comsumer_request(message):
    response = HttpResponse('Hello world! %s' % message.content['path'])
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
