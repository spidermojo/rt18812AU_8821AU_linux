const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
	console.log('I am ready!');
});

client.on('message', message =>
{
	if (message.startsWith('Woodhouse') || message.startsWith('woodhouse'))
	{
		switch (message)
		{
			case 'help':
			{
				message.reply('I support the following commands:\n\n\t echo');
				break;
			}
			case 'echo':
			{
				message.reply(message.replace('echo', ''));
				break;
			}
		}
	}
});

client.login('MzMzNzEzNjIyNjQxNjcyMTky.DEQqyA.iiPTJAgNkZAT1cJtqGIvdHlHIQ0');
