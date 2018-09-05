from disco.bot import Plugin

class TutorialPlugin(Plugin):
    @Plugin.command('ping')
    def command_ping(self, event):
        event.msg.reply('Pong!')

class KickSagnik(Plugin):
    @Plugin.command('kicksagnik')
    def command_kicksagnik(self,event):
        event.msg.reply('{} kicked Sagnik'.format(event.author.username))