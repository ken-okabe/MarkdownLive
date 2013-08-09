(function()
{
	// This is for node.js Server Setttings, after the configration,
	// You need to restart MarkdownLive plugin;

	// To restart the plugin, 
	// Restart SublimeText3 or
	// Save action for MarkdownLive.py
	exports.markedSettings = function()
	{
		return {
			gfm: true,
			breaks: true,
			tables: true,
			pedantic: false,
			sanitize: false,
			smartLists: true,
			smartypants: true,
			langPrefix: 'lang-',
			highlight: function(code)
			{
				var hljs = require('highlight.js');
				return hljs.highlightAuto(code)
					.value;
			}
		};
	};

	exports.newlinesAsIs = function()
	{
		return true;
	};

}());